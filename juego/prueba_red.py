import ipaddress
import socket
import time
import uuid


def obtener_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        mi_ip = s.getsockname()[0]
    finally:
        s.close()
    return mi_ip

def broadcast():
    ip = obtener_ip()
    red = ipaddress.IPv4Network(ip + "/24", strict=False)
    return str(red.broadcast_address)


puerto = 4000
nombre = "Cris"
mi_id = str(uuid.uuid4())

estado = "ESPERANDO"
oponente = None

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(("", puerto))
sock.settimeout(1)

print("Mi ID:", mi_id)

mi_ip = obtener_ip()
broadcast = broadcast()
print(mi_ip)
print(broadcast)

while True:
    if estado == "ESPERANDO":
        # Enviar DESCUBRIR
        msg = f"DESCUBRIR;{mi_id};{nombre}"
        sock.sendto(msg.encode(), (broadcast, puerto))

    try:
        data, addr = sock.recvfrom(1024)
        msg = data.decode()
        ip, _ = addr

        partes = msg.split(";")

        if partes[0] == "DESCUBRIR" and estado == "ESPERANDO":
            otro_id, otro_nombre = partes[1], partes[2]

            if otro_id == mi_id:
                continue

            #  solo acepta el ID menor para que no acepten los dos a la vez
            if mi_id < otro_id:
                print(f"Aceptando a {otro_nombre}")
                reply = f"ACEPTADO;{mi_id};{nombre}"
                sock.sendto(reply.encode(), addr)
                oponente = (otro_nombre, ip)
                estado = "JUGANDO"

        elif partes[0] == "ACEPTADO" and estado == "ESPERANDO":
            otro_id, otro_nombre = partes[1], partes[2]

            print(f"{otro_nombre} me ha aceptado")
            oponente = (otro_nombre, ip)
            estado = "JUGANDO"

    except socket.timeout:
        pass

    if estado == "JUGANDO":
        print("Emparejado con", oponente)
        break

    time.sleep(2)
