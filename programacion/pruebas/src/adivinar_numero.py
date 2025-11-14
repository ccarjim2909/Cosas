import random

#entrada
numero_aleatorio = random.randint(1, 100)

numero = int(input("tienes 6 intentos para acertar un numero del 1 al 100: "))
contador = 0

#procesamiento
while numero != numero_aleatorio and contador < 5:
    contador = contador + 1
    if numero > numero_aleatorio:
        numero = int(input("tu numero es mayor que el que quieres adivinar, di otro: "))
    else:
        numero = int(input("tu numero es menor que el que quieres adivinar, di otro: "))


#salida
if numero == numero_aleatorio:
    print("acertaste")
else:
    print("se te han acabado los intentos y no has acertado, el numero era", numero_aleatorio)

