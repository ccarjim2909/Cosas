#Generar la tabla de multiplicar de un número
#Descripción: Genera la tabla de multiplicar del número introducido, desde 1 hasta 10.
#Entrada: Número entero X.
#Salida: Series de líneas “X x i = resultado”.

numero = int(input("Introduce un número: "))

for i in range(1, 11):
    print(numero, "*", i, "=", numero * i)