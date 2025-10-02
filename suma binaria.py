binario1 = input("Ingresa el primer numero binario que quieras sumar: ")

while not set(binario1) <= {"1","0"} or not len(binario1) == 8:
    binario1 = input("Lo que has escrito no es un numero binario o no tiene 8 bits, vuelve a intentarlo: ")

binario1 = int(binario1)


binario2 = input("Ingresa el segundo numero binario que quieras sumar: ")

while not set(binario2) <= {"1","0"} or not len(binario2) == 8:
    binario2 = input("Lo que has escrito no es un numero binario o no tiene 8 bits, vuelve a intentarlo: ")

binario2 = int(binario2)



lista1 = [binario1]

lista2 = [binario2]

acarreo = [000000000]


resultado_invertido = []

for i in len(lista1-1, 0, -1):
    if i[lista1] == 0 and i[lista2] == 0:
        if i[lista1] == 0 and i[lista2] == 0 and i[acarreo] == 0:
            resultado_invertido.append(0)
        else:
            resultado_invertido.append(1)
    elif i[lista1] == 0 and i[lista2] == 1 or i[lista1] == 1 and i[lista2] == 0:
        if i[lista1] == 1 and i[lista2] == 0 and i[acarreo] == 0 or i[lista1] == 0 and i[lista2] == 1 and i[acarreo] == 0:
            resultado_invertido.append(1)
        else:
            resultado_invertido.append(0)
            #acarreo = acarreo[i-1] + 1 + acarreo[i]
    else:
        if i[lista1] == 1 and i[lista2] == 1:
            if i[lista1] == 1 and i[lista2] == 1 and i[acarreo] == 0:
                resultado_invertido.append(0)
                #acarreo = acarreo[i - 1] + 1 + acarreo[i]
            else:
                resultado_invertido.append(1)

resultado = resultado_invertido[::-1]

print(resultado)


