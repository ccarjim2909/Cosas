




def main():
    palabra = "patata"

    lista = ["hala","adios","mañana","otro","delfin","gamba","siete","pescado","alcachofa","diez"]



    for palabra2 in lista:
        aciertos = 0
        for letra2 in palabra2:
            for letra in palabra:
                if letra == letra2:
                    aciertos += 1

        print(palabra2, aciertos)



if __name__ == "__main__":
    main()