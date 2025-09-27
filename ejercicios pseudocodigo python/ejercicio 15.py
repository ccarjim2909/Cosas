#Cociente y resto de una división
#Descripción: Pide dos enteros y muestra el cociente y el resto de su división entera.
#Entrada: n, m (enteros).
#Salida: cociente, resto.

num1 = int(input("Introduce el primer número entero: "))
num2 = int(input("Introduce el segundo número entero: "))

cociente = num1 // num2
resto = num1 % num2

print("El cociente de estos dos números es", cociente)
print("El resto de estos dos números es", resto)
