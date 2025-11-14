lista = [3,7,2,9,4,1]
lista_ordenada = []

for numero in lista:
    contador = 0
    while contador < len(lista_ordenada) and lista_ordenada[contador] < numero:
        contador = contador + 1
    lista_ordenada.insert(contador, numero)

print(lista_ordenada)












