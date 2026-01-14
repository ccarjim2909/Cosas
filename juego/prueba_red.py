import socket
import time
import uuid

PORT = 4000
NAME = input("Nombre: ")
MY_ID = str(uuid.uuid4())

state = "WAITING"
opponent = None

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(("", PORT))
sock.settimeout(1)

print("Mi ID:", MY_ID)

while True:
    if state == "WAITING":
        # Enviar DISCOVER
        msg = f"DISCOVER;{MY_ID};{NAME}"
        sock.sendto(msg.encode(), ("255.255.255.255", PORT))

    try:
        data, addr = sock.recvfrom(1024)
        msg = data.decode()
        ip, _ = addr

        parts = msg.split(";")

        if parts[0] == "DISCOVER" and state == "WAITING":
            other_id, other_name = parts[1], parts[2]

            if other_id == MY_ID:
                continue

            # Regla: solo acepta el ID menor
            if MY_ID < other_id:
                print(f"Aceptando a {other_name}")
                reply = f"ACCEPT;{MY_ID};{NAME}"
                sock.sendto(reply.encode(), addr)
                opponent = (other_name, ip)
                state = "PLAYING"

        elif parts[0] == "ACCEPT" and state == "WAITING":
            other_id, other_name = parts[1], parts[2]

            print(f"{other_name} me ha aceptado")
            opponent = (other_name, ip)
            state = "PLAYING"

    except socket.timeout:
        pass

    if state == "PLAYING":
        print("🎮 Emparejado con", opponent)
        break

    time.sleep(2)
