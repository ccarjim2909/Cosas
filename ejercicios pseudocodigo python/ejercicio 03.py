#Determinar si un número es primo
#Descripción: Indica si un número entero es primo (solo divisible entre 1 y él mismo).
#Entrada: Número entero X.
#Salida: Mensaje indicando si X es primo o no.


numero = int(input("Introduce un número: "))

es_primo = True

if numero <= 1:
    es_primo = False
else:
    for i in range(2, x):
        if numero % i == 0:
            es_primo = False
            break

if es_primo:
    print("El número es primo")
else:
    print("El número no es primo")
