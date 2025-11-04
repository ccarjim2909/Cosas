def pedir_edad():
    edad = int(input("Ingrese la edad del cliente: "))
    return edad


def calcular_precio(edad: int) -> str:
    if edad < 4:
        precio = 0
    elif 4 <= edad <= 18:
        precio = 5
    else:
        precio = 10

    return "El precio de la entrada es: " + str(precio) + " €"


def main():
    edad = pedir_edad()
    resultado = calcular_precio(edad)
    print(resultado)


if __name__ == "__main__":
    main()