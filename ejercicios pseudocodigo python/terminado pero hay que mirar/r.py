import ipaddress
import socket
import time
import uuid
from j import *
from pprint import pprint

tocado_agua = ("TOCADO", "AGUA", "HUNDIDO", "YA DISPARADO", "DERROTA")
posiciones_barco_actual = []

# -------------------------------
# RED
# -------------------------------
def obtener_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        mi_ip = s.getsockname()[0]
    finally:
        s.close()
    return mi_ip

def calcular_broadcast():
    return str(ipaddress.IPv4Network(obtener_ip() + "/24", strict=False).broadcast_address)

# -------------------------------
# DESCUBRIR OPONENTE
# -------------------------------
def buscar_oponente(nombre: str, puerto: int = 4000):
    mi_id = str(uuid.uuid4())
    dir_broadcast = calcular_broadcast()

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(("", puerto))
    sock.settimeout(1.0)

    estado = "ESPERANDO"
    soy_host = False

    print(f"Buscando en red... Mi IP: {obtener_ip()}")

    while estado == "ESPERANDO":
        msg = f"DESCUBRIR;{mi_id};{nombre}"
        sock.sendto(msg.encode(), (dir_broadcast, puerto))

        try:
            data, addr = sock.recvfrom(1024)
            ip, _ = addr
            modo, otro_id, otro_nombre = data.decode().split(";")

            if modo == "DESCUBRIR":
                if otro_id != mi_id and mi_id < otro_id:
                    print(f"ACEPTADO: {otro_nombre}")
                    sock.sendto(f"ACEPTADO;{mi_id};{nombre}".encode(), addr)
                    oponente = (otro_nombre, ip)
                    estado = "JUGANDO"
                    soy_host = True
                    print(f"Aceptando a {otro_nombre}...")
                else:
                    print(f"Esperando respuesta {nombre}")

            elif modo == "ACEPTADO":
                print(f"{otro_nombre} me ha aceptado")
                oponente = (otro_nombre, ip)
                estado = "JUGANDO"
                soy_host = False

        except socket.timeout:
            pass

        if estado == "ESPERANDO":
            time.sleep(1)

    sock.close()
    return oponente, soy_host

# -------------------------------
# SOCKETS TCP
# -------------------------------
def abrir_socket_servidor_para_jugar(puerto):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((obtener_ip(), puerto))
    s.listen(1)
    print("Esperando jugador...")
    conn, addr = s.accept()
    print("Conectado:", addr)
    return conn

def socket_cliente_para_jugar(rival, puerto):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((rival[1], puerto))
    print("Conectado al servidor")
    return s

# -------------------------------
# LÓGICA DE TURNO (Servidor/Cliente separadas)
# -------------------------------
def servidor(conn, mi_turno, tablero_propio, tablero_enemigo, contador_barcos_hundidos, contador_nuestros_barcos_hundidos):
    resultado = None
    nuevo_contador = contador_barcos_hundidos
    nuevo_contador_nuestros = contador_nuestros_barcos_hundidos

    if mi_turno:
        if len(posiciones_barco_actual) == 0:
            disparo, fila, columna = paridad(tablero_enemigo)
        else:
            target_res = target(tablero_enemigo, posiciones_barco_actual)
            if target_res is not None:
                disparo, fila, columna = target_res
            else:
                disparo, fila, columna = paridad(tablero_enemigo)

        fila = int(disparo[1:]) - 1
        columna = desparsear_letra(disparo[0])
        conn.sendall(disparo.encode())
        respuesta = conn.recv(1024).decode().strip()

        match respuesta:
            case "AGUA":
                tablero_enemigo[fila][columna] = "O"
                mi_turno = False
            case "YA DISPARADO":
                mi_turno = False
            case "TOCADO":
                tablero_enemigo[fila][columna] = "X"
                posiciones_barco_actual.append((fila, columna))
                mi_turno = True
            case "HUNDIDO":
                tablero_enemigo[fila][columna] = "X"
                posiciones_barco_actual.append((fila, columna))
                marcar_zona_muerta(tablero_enemigo, posiciones_barco_actual)
                posiciones_barco_actual.clear()
                nuevo_contador += 1
                mi_turno = True
            case "DERROTA":
                nuevo_contador = NUM_BARCOS
                tablero_enemigo[fila][columna] = "X"


        resultado = respuesta
    else:
        disparo_recibido = conn.recv(1024).decode().strip()
        print(f"Disparo enemigo: {disparo_recibido}")
        resultado_local = recibir_disparo(tablero_propio, disparo_recibido)

        if resultado_local == "HUNDIDO":
            nuevo_contador_nuestros += 1
            if nuevo_contador_nuestros == NUM_BARCOS:
                resultado_local = "DERROTA"

        conn.sendall(resultado_local.encode())
        resultado = resultado_local

        if resultado in ("TOCADO", "HUNDIDO", "DERROTA"):
            mi_turno = False
        else:
            mi_turno = True

    time.sleep(1)
    print("\n--- TABLERO Enemigo ---")
    pprint(tablero_enemigo)
    return mi_turno, resultado, nuevo_contador, nuevo_contador_nuestros

def cliente(s, mi_turno, tablero_propio, tablero_enemigo, contador_barcos_hundidos, contador_nuestros_barcos_hundidos):
    resultado = None
    nuevo_contador = contador_barcos_hundidos
    nuevo_contador_nuestros = contador_nuestros_barcos_hundidos

    if mi_turno:
        if len(posiciones_barco_actual) == 0:
            disparo, fila, columna = paridad(tablero_enemigo)
        else:
            target_res = target(tablero_enemigo, posiciones_barco_actual)
            if target_res is not None:
                disparo, fila, columna = target_res
            else:
                disparo, fila, columna = paridad(tablero_enemigo)

        fila = int(disparo[1:]) - 1
        columna = desparsear_letra(disparo[0])
        s.sendall(disparo.encode())
        respuesta = s.recv(1024).decode().strip()

        match respuesta:
            case "AGUA":
                tablero_enemigo[fila][columna] = "O"
                mi_turno = False
            case "YA DISPARADO":
                mi_turno = False
            case "TOCADO":
                tablero_enemigo[fila][columna] = "X"
                posiciones_barco_actual.append((fila, columna))
                mi_turno = True
            case "HUNDIDO":
                tablero_enemigo[fila][columna] = "X"
                posiciones_barco_actual.append((fila, columna))
                marcar_zona_muerta(tablero_enemigo, posiciones_barco_actual)
                posiciones_barco_actual.clear()
                nuevo_contador += 1
                mi_turno = True
            case "DERROTA":
                nuevo_contador = NUM_BARCOS
                tablero_enemigo[fila][columna] = "X"

        resultado = respuesta
    else:
        disparo_recibido = s.recv(1024).decode().strip()
        print(f"Disparo enemigo: {disparo_recibido}")
        resultado_local = recibir_disparo(tablero_propio, disparo_recibido)

        if resultado_local == "HUNDIDO":
            nuevo_contador_nuestros += 1
            if nuevo_contador_nuestros == NUM_BARCOS:
                resultado_local = "DERROTA"

        s.sendall(resultado_local.encode())
        resultado = resultado_local

        if resultado in ("TOCADO", "HUNDIDO", "DERROTA"):
            mi_turno = False
        else:
            mi_turno = True

    time.sleep(1)
    print("\n--- TABLERO Enemigo ---")
    pprint(tablero_enemigo)
    return mi_turno, resultado, nuevo_contador, nuevo_contador_nuestros

# -------------------------------
# MAIN
# -------------------------------
def main():
    contador_barcos_hundidos = 0
    contador_nuestros_barcos_hundidos = 0

    tablero_jugador1 = [
        ["~", "~", "~", "~", "~", "~", "~", "~"],
        ["~", "~", "~", "~", "~", "~", "~", "~"],
        ["~", "~", "~", "~", "~", "~", "~", "~"],
        ["~", "~", "~", "~", "~", "~", "~", "~"],
        ["~", "~", "~", "~", "~", "~", "~", "~"],
        ["~", "~", "~", "~", "~", "~", "~", "~"],
        ["~", "~", "~", "~", "~", "~", "~", "~"],
        ["~", "~", "~", "~", "~", "~", "~", "~"],

    ]

    tablero_jugador2 = [
        ["~", "~", "~", "~", "~", "~", "~", "~"],
        ["~", "~", "~", "~", "~", "~", "~", "~"],
        ["~", "~", "~", "~", "~", "~", "~", "~"],
        ["~", "~", "~", "~", "~", "~", "~", "~"],
        ["~", "~", "~", "~", "~", "~", "~", "~"],
        ["~", "~", "~", "~", "~", "~", "~", "~"],
        ["~", "~", "~", "~", "~", "~", "~", "~"],
        ["~", "~", "~", "~", "~", "~", "~", "~"],
    ]

    barcos = {"1":5,"2":4,"3":3,"4":3,"5":2}
    for id_barco, tamaño in barcos.items():
        colocar_un_barco(tablero_jugador1, tamaño, id_barco)

    pprint(tablero_jugador1)

    puerto = 4000
    nombre = "El trio lalala"
    (nombre_rival, ip_rival), soy_host = buscar_oponente(nombre, puerto)

    print(f"PARTIDA ENCONTRADA: {nombre} VS {nombre_rival}")

    if soy_host:
        print(f"[HOST]: {nombre} {obtener_ip()} (YO)")
        print(f"[CLIENTE]: {nombre_rival} {ip_rival}")
        conexion = abrir_socket_servidor_para_jugar(puerto)
        mi_turno = True
        while contador_barcos_hundidos < NUM_BARCOS and contador_nuestros_barcos_hundidos < NUM_BARCOS:
            mi_turno, mensaje, contador_barcos_hundidos, contador_nuestros_barcos_hundidos = servidor(
                conexion, mi_turno, tablero_jugador1, tablero_jugador2,
                contador_barcos_hundidos, contador_nuestros_barcos_hundidos
            )
            print(mi_turno, mensaje)


            if mensaje == "DERROTA":
                print("🎉 Ganamos")
                conexion.close()
                break
    else:
        print(f"[HOST]: {nombre_rival} {ip_rival}")
        print(f"[CLIENTE]: {nombre} {obtener_ip()} (YO)")
        time.sleep(1)
        s = socket_cliente_para_jugar((nombre_rival, ip_rival), puerto)
        mi_turno = False
        while contador_barcos_hundidos < NUM_BARCOS and contador_nuestros_barcos_hundidos < NUM_BARCOS:
            mi_turno, mensaje, contador_barcos_hundidos, contador_nuestros_barcos_hundidos = cliente(
                s, mi_turno, tablero_jugador1, tablero_jugador2,
                contador_barcos_hundidos, contador_nuestros_barcos_hundidos
            )
            print(mi_turno, mensaje)

            if mensaje == "DERROTA":
                print("🎉 Ganamos")
                s.close()
                break

    print("\n--- TABLERO FINAL PROPIO ---")
    pprint(tablero_jugador1)
    print("\n--- TABLERO FINAL ENEMIGO ---")
    pprint(tablero_jugador2)


if __name__ == "__main__":
    main()
