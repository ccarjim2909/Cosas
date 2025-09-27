#Repetir nombre del usuario
#Descripción: Imprime el nombre del usuario tantas veces como indique un entero n.
#Entrada: nombre (texto), n (entero).
#Salida: nombre repetido n veces (una por línea).

nombre = input("Introduce tu nombre: ")
numero = int(input("Introduce el número de veces que quieres que se repita: "))

for i in range(numero):
    print(nombre)