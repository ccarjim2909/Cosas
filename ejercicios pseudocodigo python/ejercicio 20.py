#Nombre en minúsculas, mayúsculas y capitalizado
#Descripción: Muestra un nombre completo en minúsculas, mayúsculas y con mayúsculas iniciales.
#Entrada: nombre completo (texto).
#Salida: Tres variantes del nombre.


nombre = input("Introduce tu nombre completo: ")

print("Tu nombre en minúsculas es", nombre.lower())
print("Tu nombre en mayúsculas es", nombre.upper())
print("Tu nombre con la mayúscula inicial es", nombre.title())
