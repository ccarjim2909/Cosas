#Panadería: barras no frescas
#Descripción: Calcula el precio de barras con 60% de descuento sobre el precio habitual de 3,49€.
#Entrada: Nº de barras no frescas.
#Salida: Precio habitual, descuento aplicado, coste total.

barras = int(input("Introduce el número de barras no frescas: "))

habitual = 3.49
descuento = habitual * 60 / 100
final = habitual - descuento

print("El precio habitual de la barra es", habitual, "€")
print("Con el descuento aplicado del 60% sería", final, "€ por barra")
print("El coste total sería", final * barras, "€")
