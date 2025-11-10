import sys
from sys import argv

import os
from os import system

import platform

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
        if numero < 0 or numero > 255:
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


def comprobar_ordenador(ip: str, sistema: str) -> bool:
    if sistema == "Windows":
        print("Espere un poco mientras se verifica si la ip esta en tu red...")
        ping = os.system("ping " + ip + " > null")
        if ping == 0:
            return True
        else:
            return False
    elif sistema == "Linux":
        print("Espere un poco mientras se verifica si la ip esta en tu red...")
        ping = os.system("ping " + ip + " > null")
        if ping == 0:
            return True
        else:
            return False
    elif sistema == "Darwin":
        print("Espere un poco mientras se verifica si la ip esta en tu red...")
        ping = os.system("ping " + ip + " > null")
        if ping == 0:
            return True
        else:
            return False


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
        else:
            print("La IP no esta en tu red.")
    else:
        print("La IP no es valida.")


if __name__ == "__main__":
    main()