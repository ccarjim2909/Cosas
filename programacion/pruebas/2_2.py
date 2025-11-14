
def calculo():

    # lectura de datos
    numero = input("Introduzca un número: ")
    contador = 0
    total = 0
    media = 0


    # calculo
    while numero != "fin":
        if numero.isdigit():
            numero = int(numero)
            contador = contador + 1
            total = numero + total
            numero = input("Introduzca un número: ")
        else:
            print("Entrada inválida")
            numero = input("Introduzca un número: ")


    if contador > 0:
        media = total / contador

    # resultado
    print(total, contador, media)


def __main__():
    calculo()


if __name__ == '__main__':
    __main__()




