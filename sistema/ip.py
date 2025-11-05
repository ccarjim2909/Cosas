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

    if primer_octeto >= 0 and primer_octeto <= 126:
        return "Clase A"
    elif primer_octeto >= 128 and primer_octeto <= 191:
        return "Clase B"
    elif primer_octeto >= 192 and primer_octeto <= 223:
        return "Clase C"
    elif primer_octeto >= 224 and primer_octeto <= 239:
        return "Clase D"
    else:
        return "Clase E"



def main():
    ip = pedir_ip()

    if validar_ip(ip):
        clase = clase_ip(ip)
        print("La IP es valida.")
        print("Pertenece a la clase:", clase)
    else:
        print("La IP no es valida.")


if __name__ == "__main__":
    main()

