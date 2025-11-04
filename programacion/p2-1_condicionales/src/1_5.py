def pregunta_edad():
    edad = int(input("Ingresa tu edad: "))
    return edad

def pregunta_ingresos():
    ingresos = int(input("Ingresa tus ingresos mensuales: "))
    return ingresos

def tributa(edad:int,ingresos:int) ->bool:
    if edad >= 16 and ingresos >= 1000:
        return True
    else:
        return False


def main():
    edad = pregunta_edad()
    ingresos = pregunta_ingresos()

    if tributa(edad,ingresos):
        print("Esta persona tiene que tributar")
    else:
        print("Esta persona no tiene que tributar")


if __name__ == "__main__":
    main()