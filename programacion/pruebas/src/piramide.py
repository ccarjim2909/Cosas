numero_lineas = int(input('dime un numero de lineas: '))

for linea in range(numero_lineas+1):
    for numero in range(linea):
        print("*", end="")

    print("\n")

