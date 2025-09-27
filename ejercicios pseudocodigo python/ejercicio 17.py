#Peso de un pedido de payasos y muñecas
#Descripción: Calcula el peso total de un pedido (112 g por payaso, 75 g por muñeca).
#Entrada: Nº de payasos, nº de muñecas.
#Salida: Peso total en gramos.

capital = float(input("Introduce el capital inicial: "))

interes = 0.04

año1 = capital * (1 + interes)
año2 = capital * (1 + interes) ** 2
año3 = capital * (1 + interes) ** 3

print("El saldo dentro de un año sería", año1)
print("El saldo dentro de dos años sería", año2)
print("El saldo dentro de tres años sería", año3)

