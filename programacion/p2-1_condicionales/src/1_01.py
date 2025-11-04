def recoge_datos():
    edad = input("Ingrese su edad: ")

    return int(edad)

def calculo(edad:int)->bool:
    if edad >= 18:
        return True
    else:
        return False



def main():
    # recibe
    edad = recoge_datos()

    # calculo
    if calculo(edad):
        print("Esta persona es mayor de edad")
    else:
        print("Esta persona es menor de edad")




if __name__ == '__main__':
    main()