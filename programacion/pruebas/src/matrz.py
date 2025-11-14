numero = int(input("elemento a buscar: "))

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


i = 0

while i < len(matriz):
    j = 0
    while j < len(matriz[i]):
        if matriz[i][j] == numero:
            i_encontrado = i
            j_encontrado = j
        j = j + 1
    i = i + 1

print(i_encontrado, j_encontrado)
