def prueba():
    intento = input("Escribeme la contraseña: ")
    return str(intento)

def comparacion(intento:str):
    contraseña_real = "contraseña"
    if intento.lower() == contraseña_real:
        return True
    else:
        return False


def main():
    intento = prueba()

    if comparacion(intento):
        print("El resultado es correcto")
    else:
        print("El resultado no es correcto")




if __name__ == '__main__':
    main()
