import ipaddress
import socket
import time
import uuid
import os
from hundirflota import *
from pprint import pprint
tocado_agua = ("TOCADO", "AGUA", "HUNDIDO", "YA DISPARADO", "DERROTA")

posiciones_barco_actual = []

def obtener_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        s.connect(("8.8.8.8", 80))
        mi_ip = s.getsockname()[0]
    finally:
        s.close()
    return mi_ip

def calcular_broadcast():
    # RED
    return str(ipaddress.IPv4Network(obtener_ip() + "/24", strict=False).broadcast_address)


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
    s.connect((rival[1], puerto))  # rival[1] es la IP del host
    print("Conectado al servidor")
    return s


def servidor(conn, mi_turno : bool, tablero_jugador1 : list[list[str]],tablero_jugador2 : list[list[str]], contador_barcos_hundidos : int, posiciones_barco_actual: list[tuple[int, int]]):
    """
    Servidor cuando es MI TURNO: disparamos al enemigo
    Servidor cuando NO es MI TURNO: recibimos disparo del enemigo
    """
    resultado = None
    nuevo_contador = contador_barcos_hundidos
    if mi_turno:
        if len(posiciones_barco_actual) == 0: # Si aún no hemos tocado -> paridad
            disparo, fila, columna = paridad(tablero_jugador2)
        else: # Si ya hemos tocado -> target
            resultado_target = target(tablero_jugador2, posiciones_barco_actual)
            if resultado_target is not None:
                disparo, fila, columna = resultado_target
            else:
                disparo, fila, columna = paridad(tablero_jugador2)
        fila = int(disparo[1]) - 1
        columna = desparsear_letra(disparo[0])

        conn.sendall(disparo.encode()) # Envío de coordenadas

        respuesta = conn.recv(1024).decode().strip() # Respuesta que recibimos

        match respuesta:
            case "AGUA":
                tablero_jugador2[fila][columna] = "O"
                mi_turno = False  # Se pierde el turno

            case "YA DISPARADO":
                mi_turno = False # Se pierde el turno

            case "TOCADO":
                tablero_jugador2[fila][columna] = "X"
                posiciones_barco_actual.append((fila, columna))
                mi_turno = True

            case "HUNDIDO":
                tablero_jugador2[fila][columna] = "X"
                posiciones_barco_actual.append((fila, columna))  # Última posición
                marcar_zona_muerta(tablero_jugador2, posiciones_barco_actual)
                posiciones_barco_actual.clear()  # Reiniciar para el próximo barco
                mi_turno = True

        resultado = respuesta
    else:
        # El disparo que recibo
        disparo_recibido = conn.recv(1024).decode().strip()
        print(f"Disparo enemigo: {disparo_recibido}")

        # El mensaje que voy a devolver
        resultado = recibir_disparo(tablero_jugador1, disparo_recibido)
        conn.sendall(resultado.encode())

        nuevo_contador = contador_barcos_hundidos
        if resultado == "HUNDIDO":
            nuevo_contador += 1
            if nuevo_contador == NUM_BARCOS:
                resultado = "DERROTA"

        # Mirar si me sigue tocando o no
        if resultado == "TOCADO" or resultado == "HUNDIDO":
            mi_turno = False
        else:
            mi_turno = True

    return mi_turno, resultado, nuevo_contador


def cliente(s, mi_turno: bool, tablero_jugador1: list[list[str]], tablero_jugador2: list[list[str]],
            contador_barcos_hundidos: int, posiciones_barco_actual: list[tuple[int, int]]) -> tuple[bool, str, int]:
    """
    Cliente cuando es MI TURNO: disparamos al enemigo
    Cliente cuando NO es MI TURNO: recibimos disparo del enemigo
    """
    resultado = None
    nuevo_contador = contador_barcos_hundidos

    if mi_turno:
        if len(posiciones_barco_actual) == 0:  # Si aún no hemos tocado -> paridad
            disparo, fila, columna = paridad(tablero_jugador2)
        else:  # Si ya hemos tocado -> target
            resultado_target = target(tablero_jugador2, posiciones_barco_actual)
            if resultado_target is not None:
                disparo, fila, columna = resultado_target
            else:
                disparo, fila, columna = paridad(tablero_jugador2)

        fila = int(disparo[1]) - 1
        columna = desparsear_letra(disparo[0])

        s.sendall(disparo.encode())

        respuesta = s.recv(1024).decode().strip()

        match respuesta:
            case "AGUA":
                tablero_jugador2[fila][columna] = "O"
                mi_turno = False  # Se pierde el turno

            case "YA DISPARADO":
                mi_turno = False  # Se pierde el turno

            case "TOCADO":
                tablero_jugador2[fila][columna] = "X"
                posiciones_barco_actual.append((fila, columna))  # Añadir posición
                mi_turno = True

            case "HUNDIDO":
                tablero_jugador2[fila][columna] = "X"
                posiciones_barco_actual.append((fila, columna))  # Última posición
                marcar_zona_muerta(tablero_jugador2, posiciones_barco_actual)
                posiciones_barco_actual.clear()  # Reiniciar
                mi_turno = True

        resultado = respuesta

    else:
        disparo_recibido = s.recv(1024).decode().strip()
        print(f"Disparo enemigo: {disparo_recibido}")

        resultado = recibir_disparo(tablero_jugador1, disparo_recibido)
        s.sendall(resultado.encode())

        nuevo_contador = contador_barcos_hundidos
        if resultado == "HUNDIDO":
            nuevo_contador += 1
            if nuevo_contador == NUM_BARCOS:
                resultado = "DERROTA"

        if resultado == "TOCADO" or resultado == "HUNDIDO":
            mi_turno = False
        else:
            mi_turno = True

    return mi_turno, resultado, nuevo_contador

def main():
    barcos = {
        "1": 5,
        "2": 4,
        "3": 3,
        "4": 3,
        "5": 2
    }

    contador_barcos_hundidos = 0

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

    for id_barco, tamaño_barco in barcos.items():
        colocar_un_barco(tablero_jugador1, tamaño_barco, id_barco)
    pprint(tablero_jugador1)

    puerto = 4000
    nombre = "Equipo pescadilla"


    (nombre_rival, ip_rival), soy_el_host = buscar_oponente(nombre, puerto)

    print(f"PARTIDA ENCONTRADA: {nombre} VS {nombre_rival}")

    if soy_el_host:
        print(f"[HOST]: {nombre} {obtener_ip()} (YO)")
        print(f"[CLIENTE]: {nombre_rival} {ip_rival}")
        conexion = abrir_socket_servidor_para_jugar(puerto)
        mi_turno = True
        while contador_barcos_hundidos < NUM_BARCOS:
            mi_turno, mensaje, contador_barcos_hundidos = servidor(conexion, mi_turno, tablero_jugador1, tablero_jugador2, contador_barcos_hundidos, posiciones_barco_actual)

            print(mi_turno, mensaje)

            if mensaje == "DERROTA":
                conexion.close()
                print("Ganamos")


    else:
        print(f"[HOST]: {nombre_rival} {ip_rival}")
        print(f"[CLIENTE]: {nombre} {obtener_ip()} (YO)")
        time.sleep(1)
        socket_aceptado = socket_cliente_para_jugar((nombre_rival, ip_rival), puerto)
        mi_turno = False
        while contador_barcos_hundidos < NUM_BARCOS:
            mi_turno, mensaje, contador_barcos_hundidos = cliente(socket_aceptado, mi_turno, tablero_jugador1, tablero_jugador2, contador_barcos_hundidos, posiciones_barco_actual)

            print (mi_turno, mensaje)

            if mensaje == "DERROTA":
                socket_aceptado.close()
                print("Ganamos")




if __name__ == "__main__":
    main()
