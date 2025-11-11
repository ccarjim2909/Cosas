import sys
import os
import platform
import threading
import time

def pedir_ip():
    ip = sys.argv[1]
    return ip


def validar_ip(ip: str) -> bool:
    partes = ip.split(".")

    if len(partes) != 4:
        return False

    for parte in partes:
        if not parte.isdigit():
            return False
        numero = int(parte)
        if numero <= 0 or numero >= 255:
            return False

    return True


def clase_ip(ip: str) -> str:
    partes = ip.split(".")
    primer_octeto = int(partes[0])

    if primer_octeto >= 0 and primer_octeto <= 127:
        return "Clase A"
    elif primer_octeto >= 128 and primer_octeto <= 191:
        return "Clase B"
    elif primer_octeto >= 192 and primer_octeto <= 223:
        return "Clase C"
    elif primer_octeto >= 224 and primer_octeto <= 239:
        return "Clase D"
    else:
        return "Clase E"


def comprobar_sistema() -> str:
    sistema = platform.system()
    return sistema



procesando = True

def animacion():
    while procesando:
        for puntos in ["   ", ".  ", ".. ", "..."]:
            print(f"\rVerificando IP{puntos}", end="")
            time.sleep(0.5)
    print("\rProceso finalizado.")


def comprobar_ordenador(ip: str, sistema: str) -> bool:
    global procesando

    hilo = threading.Thread(target=animacion)
    hilo.start()

    if sistema == "Windows":
        ping = os.system("ping " + ip + " > NUL")
    else:
        ping = os.system("ping " + ip + " > /dev/null")


    procesando = False
    hilo.join()

    return ping == 0


def leer_mac(ip: str, sistema: str) -> str:
    mac = "No encontrada"

    if sistema == "Windows":
        comando = os.popen("arp -a " + ip)
        salida = comando.read()
        for linea in salida.splitlines():
            if ip in linea:
                mac = linea.split()[1]
    else:
        comando = os.popen("ip neigh show " + ip)
        salida = comando.read()
        if salida:
            mac = salida.split()[4]

    return mac


def main():
    ip = pedir_ip()
    sistema = comprobar_sistema()

    if validar_ip(ip):
        clase = clase_ip(ip)
        print("La IP es valida.")
        print("Pertenece a la clase:", clase)


        ping = comprobar_ordenador(ip, sistema)
        if ping:
            print("La IP esta en tu red.")
            mac = leer_mac(ip, sistema)
            print("La MAC es:", mac)
        else:
            print("La IP no esta en tu red.")
    else:
        print("La IP no es valida.")


if __name__ == "__main__":
    main()