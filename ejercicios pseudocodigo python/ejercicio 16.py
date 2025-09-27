#Peso de un pedido de payasos y muñecas
#Descripción: Calcula el peso total de un pedido (112 g por payaso, 75 g por muñeca).
#Entrada: Nº de payasos, nº de muñecas.
#Salida: Peso total en gramos.



payasos = int(input("Introduce el número de payasos: "))
muñecas = int(input("Introduce el número de muñecas: "))

gramos_payasos = payasos * 112
gramos_muñecas = muñecas * 75
total = gramos_payasos + gramos_muñecas

print("El peso total en gramos sería de", total)