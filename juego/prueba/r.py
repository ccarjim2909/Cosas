import ipaddress
import socket
import time
import uuid
from j import *
from pprint import pprint

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

    while estado == "ESPERANDO":
        msg = f"DESCUBRIR;{mi_id};{nombre}"
        sock.sendto(msg.encode(), (dir_broadcast, puerto))

        try:
            data, addr = sock.recvfrom(1024)
            ip, _ = addr
            modo, otro_id, otro_nombre = data.decode().split(";")

            if modo == "DESCUBRIR":
                if otro_id != mi_id and mi_id < otro_id:
                    sock.sendto(f"ACEPTADO;{mi_id};{nombre}".encode(), addr)
                    oponente = (otro_nombre, ip)
                    estado = "JUGANDO"
                    soy_host = True

            elif modo == "ACEPTADO":
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
    conn, addr = s.accept()
    return conn

def socket_cliente_para_jugar(rival, puerto):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((rival[1], puerto))
    return s

# -------------------------------
# LÓGICA DE TURNO
# -------------------------------

def procesar_turno_envio(sock, tablero_enemigo, posiciones_barco_actual,
                          contador_barcos_hundidos):

    if len(posiciones_barco_actual) == 0:
        disparo, fila, columna = paridad(tablero_enemigo)
    else:
        resultado_target = target(tablero_enemigo, posiciones_barco_actual)
        if resultado_target:
            disparo, fila, columna = resultado_target
        else:
            disparo, fila, columna = paridad(tablero_enemigo)

    fila = int(disparo[1:]) - 1
    columna = desparsear_letra(disparo[0])

    sock.sendall(disparo.encode())
    respuesta = sock.recv(1024).decode().strip()

    if respuesta == "AGUA":
        tablero_enemigo[fila][columna] = "O"
        return False, contador_barcos_hundidos, respuesta

    if respuesta == "TOCADO":
        tablero_enemigo[fila][columna] = "X"
        posiciones_barco_actual.append((fila, columna))
        return True, contador_barcos_hundidos, respuesta

    if respuesta == "HUNDIDO":
        tablero_enemigo[fila][columna] = "X"
        posiciones_barco_actual.append((fila, columna))
        marcar_zona_muerta(tablero_enemigo, posiciones_barco_actual)
        posiciones_barco_actual.clear()
        contador_barcos_hundidos += 1
        return True, contador_barcos_hundidos, respuesta

    if respuesta == "DERROTA":
        print("🎉 Ganamos")
        return False, NUM_BARCOS, respuesta

    return False, contador_barcos_hundidos, respuesta


def procesar_turno_recepcion(sock, tablero_propio,
                             contador_nuestros_barcos_hundidos):

    disparo = sock.recv(1024).decode().strip()
    resultado = recibir_disparo(tablero_propio, disparo)

    if resultado == "HUNDIDO":
        contador_nuestros_barcos_hundidos += 1
        if contador_nuestros_barcos_hundidos == NUM_BARCOS:
            sock.sendall("DERROTA".encode())
            print("💀 Hemos perdido")
            return False, NUM_BARCOS
    sock.sendall(resultado.encode())

    if resultado in ("TOCADO", "HUNDIDO"):
        return False, contador_nuestros_barcos_hundidos

    return True, contador_nuestros_barcos_hundidos

# -------------------------------
# MAIN
# -------------------------------

def main():

    contador_barcos_hundidos = 0
    contador_nuestros_barcos_hundidos = 0

    tablero_jugador1 = [[AGUA]*8 for _ in range(8)]
    tablero_jugador2 = [[AGUA]*8 for _ in range(8)]

    barcos = {"1":5,"2":4,"3":3,"4":3,"5":2}

    for id_barco, tamaño in barcos.items():
        colocar_un_barco(tablero_jugador1, tamaño, id_barco)

    puerto = 4000
    nombre = "Equipo pescadilla"

    (nombre_rival, ip_rival), soy_host = buscar_oponente(nombre, puerto)

    if soy_host:
        conexion = abrir_socket_servidor_para_jugar(puerto)
        sock = conexion
        mi_turno = True
    else:
        sock = socket_cliente_para_jugar((nombre_rival, ip_rival), puerto)
        mi_turno = False

    while contador_barcos_hundidos < NUM_BARCOS and contador_nuestros_barcos_hundidos < NUM_BARCOS:

        if mi_turno:
            mi_turno, contador_barcos_hundidos, _ = procesar_turno_envio(
                sock, tablero_jugador2,
                posiciones_barco_actual,
                contador_barcos_hundidos
            )
        else:
            mi_turno, contador_nuestros_barcos_hundidos = procesar_turno_recepcion(
                sock, tablero_jugador1,
                contador_nuestros_barcos_hundidos
            )

    sock.close()


if __name__ == "__main__":
    main()
