import sys
from sys import argv



#mirar longitud, mirar puntos, mirar rango, mirar clase

def leer_ip():
    ip = argv[1]
    partes = ip.split(".")
    lista_puntos = []
    contador = 0

    if len(ip) > 15 or len(ip) < 7:  #mal
        print("Lo que has escrito se pasa de la longitud maxima o minima")
    else:
        for i in partes:
            lista_puntos.append(i)
            contador = contador + 1
            if contador < len(partes):
                lista_puntos.append(".")

        for i in lista_puntos:
            if i % 2 == 0:
                if i < "0" and i > "255":
                    print("Tu ip se pasa del rango maximo posible")
                else:




    if partes[0] >= "0" and partes[0] < "127":
        print("Tu ip es de clase A")
    elif partes[0] >= "128" and partes[0] < "191":
        print("Tu ip es de clase B")
    elif partes[0] >= "192" and partes[0] < "223":
        print("Tu ip es de clase C")
    elif partes[0] >= "224" and partes[0] < "239":
        print("Tu ip es de clase D")
    else:
        print("Tu ip es de clase E")


