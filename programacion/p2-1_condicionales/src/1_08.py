def pedir_puntuacion():
    puntuacion = float(input("Ingrese la puntuacion del empleado: "))
    return puntuacion


def calcular_rendimiento(puntuacion: float) -> str:
    base = 2400

    if puntuacion == 0.0:
        nivel = "Inaceptable"
    elif puntuacion == 0.4:
        nivel = "Aceptable"
    elif puntuacion >= 0.6:
        nivel = "Meritorio"
    else:
        return "Puntuación inválida. Debe ser 0.0, 0.4 o 0.6 en adelante."

    dinero = base * puntuacion
    total = base + dinero
    return "Nivel de rendimiento: " + nivel + ("\n"
            "Dinero extra: ") + str(dinero) + (" €\n"
            "Dinero recibido: ") + str(total) + " €\n"



def main():
    puntuacion = pedir_puntuacion()
    resultado = calcular_rendimiento(puntuacion)
    print(resultado)


if __name__ == "__main__":
    main()