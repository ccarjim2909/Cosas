def pedir_numeros():
    numero1 = int(input("Ingresa el numero 1: "))
    numero2 = int(input("Ingresa el numero 2: "))

    return numero1, numero2

def division(numero1:int, numero2:int)->float:
    resultado = numero1 / numero2
    return resultado

def main():
    datos = pedir_numeros()
    if datos[1] == 0:
        print("El divisor no puede ser 0")
    else:
        resultado = division(datos[0], datos[1])
        print(resultado)

if __name__ == "__main__":
    main()