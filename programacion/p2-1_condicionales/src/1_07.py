def pregunta_renta():
    renta = int(input("Ingresa tus renta anual: "))
    return renta

def tipo_impositivo(renta:int):
    if renta > 60000:
        porcentaje = 45
        return porcentaje
    elif renta < 60000 and renta > 35000:
        porcentaje = 30
        return porcentaje
    elif renta < 35000 and renta > 20000:
        porcentaje = 20
        return porcentaje
    elif renta < 20000 and renta > 10000:
        porcentaje = 15
        return porcentaje
    else:
        porcentaje = 5
        return porcentaje


def main():
    renta = pregunta_renta()
    tipo = str(tipo_impositivo(renta))
    print("El tipo impositivo que tienes que te corresponde es del " + tipo + "%")


if __name__ == "__main__":
    main()