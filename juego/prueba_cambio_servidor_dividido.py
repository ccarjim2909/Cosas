import ipaddress
import socket
import time
import uuid
# from hundirflota import paridad,target


import random
tocado_agua = ("tocado", "agua")



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


    # TODO [GONZALO]: Posible mejora:
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
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((obtener_ip(), puerto))
        s.listen(1)
        print("Esperando jugador...")

        conn, addr = s.accept()
        print("Conectado:", addr)

    return conn


def socket_cliente_para_jugar(rival, puerto):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((rival[1], puerto))  # rival[1] es el host
        print("Conectado al servidor")

        return s


def servidor(conn, mi_turno):
    #TODO: Mirar que sea aleatorio
    #TODO: Aqui hay que añadir una forma de que no empieze uno siempre, o no dado k el host es aleatorio de momento
    #TODO: [GONZALO] Esto habria que discutirlo con el otro grupo



    # with conn:
        if mi_turno:
            disparo = input("Tu disparo (ej A,1): ")
            mensaje = f"disparo,{disparo}"
            conn.sendall((mensaje + "\n").encode())

            respuesta = conn.recv(1024).decode().strip()
            accion, resultado = respuesta.split(",")
            # esto hay que mirarlo para mirar la accion
            print("Resultado:", resultado)

            if resultado == "tocado":
                mi_turno = True

                return mi_turno,resultado
            else:
                mi_turno = False

                return mi_turno,resultado
        else:
            data = conn.recv(1024).decode().strip()
            accion, letra, numero = data.split(",")

            print(f"Disparo recibido: {letra},{numero}")

            # lógica del juego
            resultado = random.choice(tocado_agua)
            conn.sendall(f"respuesta,{resultado}\n".encode())

            if resultado == "tocado":
                mi_turno = False

                return mi_turno, resultado
            else:
                mi_turno = True

                return mi_turno, resultado





def cliente(s, mi_turno: bool):

    # with s:
        if mi_turno:
            disparo = input("Tu disparo (ej A,1): ")
            s.sendall(f"disparo,{disparo}\n".encode())

            respuesta = s.recv(1024).decode().strip()
            accion, resultado = respuesta.split(",")

            # esto hay que mirarlo para mirar la accion
            print("Resultado:", resultado)

            if resultado == "tocado":
                mi_turno = True

                return mi_turno, resultado
            else:
                mi_turno = False

                return mi_turno, resultado
        else:
            datos_mensaje = s.recv(1024).decode().strip()
            accion, letra, numero = datos_mensaje.split(",")

            print(f"Disparo recibido: {letra},{numero}")

            resultado = random.choice(tocado_agua)
            # Mirar
            s.sendall(f"respuesta,{resultado}\n".encode())

            if resultado == "tocado":
                mi_turno = False

                return mi_turno, resultado
            else:
                mi_turno = True

                return mi_turno, resultado

        # TODO: [GONZALO] No faltaria romper el bucle en funcion de una variable?





def main():
    puerto = 4000
    nombre = "Cris"

    # cliente(rival, puerto)

    (nombre_rival, ip_rival), soy_el_host = buscar_oponente(nombre, puerto)

    print(f"PARTIDA ENCONTRADA: {nombre} VS {nombre_rival}\n")

    partida_activa = True

    if soy_el_host:
        print(f"[HOST]: {nombre} {obtener_ip()} (YO)")
        print(f"[CLIENTE]: {nombre_rival} {ip_rival}")
        conexion = abrir_socket_servidor_para_jugar(puerto)
        mi_turno = True
        while partida_activa:
            mi_turno, mensaje = servidor(conexion, mi_turno)

            print(mi_turno, mensaje)

    else:
        print(f"[HOST]: {nombre_rival} {ip_rival}")
        print(f"[CLIENTE]: {nombre} {obtener_ip()} (YO)")
        time.sleep(1)
        socket_aceptado = socket_cliente_para_jugar((nombre_rival, ip_rival), puerto)
        mi_turno = False
        while partida_activa:
            mi_turno,  mensaje = cliente(socket_aceptado, mi_turno)

            print (mi_turno, mensaje)


    # TODO: [GONZALO]
    # Hay que hacer una estructura de ejecucion correcta, posiblemente reste nota. Ademas he simplificado diversas funciones
    # porque habia variables que solo se usaban 1 vez o se asignaban a si mismas, eso a Jose no le gusta.


if __name__ == "__main__":
    main()