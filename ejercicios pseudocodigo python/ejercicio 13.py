#Suma de los n primeros enteros
#Descripción: Calcula la suma de los n primeros enteros positivos usando la fórmula n(n+1)/2.
#Entrada: n (entero positivo).
#Salida: Suma de 1 hasta n.

numero = int(input("Introduce un número entero positivo: "))

suma_total = numero * (numero + 1) / 2
print("La suma de 1 hasta", n, "es", suma_total)