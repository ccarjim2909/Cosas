#Contar letras del nombre
#Descripción: Convierte el nombre a mayúsculas y muestra cuántas letras tiene.
#Entrada: nombre (texto).
#Salida: nombre en mayúsculas y número de letras.

nombre = input("Introduce tu nombre: ")

nombre_mayu = nombre.upper()
numero_letras = len(nombre)

print("Tu nombre en mayúsculas sería", nombre_mayu, "y contiene", numero_letras, "letras.")
