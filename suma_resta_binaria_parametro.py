import sys
from sys import argv

def lee_los_binarios():


    if len(argv) == 3:

        binario1 = sys.argv[1]

        if not set(binario1) <= {"1", "0"} or not len(binario1) == 8:
            print("El primer numero que has escrito no es un numero binario o no tiene 8 bits, vuelve a intentarlo.")
        else:
            binario2 = sys.argv[2]

            if not set(binario2) <= {"1", "0"} or not len(binario2) == 8:
                print("El segundo numero que has escrito no es un numero binario o no tiene 8 bits, vuelve a intentarlo.")
            else:
                binario1 = list(binario1)

                binario2 = list(binario2)

                return binario1, binario2

    elif len(argv) == 4:
        binario1 = sys.argv[1]
        operando = sys.argv[2]

        if not set(binario1) <= {"1", "0"} or not len(binario1) == 8:
            print("El primer numero que has escrito no es un numero binario o no tiene 8 bits, vuelve a intentarlo.")
        else:
            binario2 = sys.argv[3]

            if not set(binario2) <= {"1", "0"} or not len(binario2) == 8:
                print(
                    "El segundo numero que has escrito no es un numero binario o no tiene 8 bits, vuelve a intentarlo.")
            else:
                binario1 = list(binario1)

                binario2 = list(binario2)

                return binario1, operando, binario2

    else:
        print("El programa no se puede ejecutar como lo has escrito. \n"
              "Intenta escribirlo de esta manera: python suma_resta_binaria_parametro.py binario1 operando binario2. \n"
              "O si quieres hacer las dos operaciones no uses el operando: python suma_resta_binaria_parametro.py binario1 binario2")


def suma_binarios(binario1, binario2):
    acarreo = list("000000000")

    resultado_suma_invertido = []

    for i in range(len(binario1) - 1, -1, -1):
        if binario1[i] == '0' and binario2[i] == '0':
            if acarreo[i+1] == '0':
                resultado_suma_invertido.append('0')
            else:
                resultado_suma_invertido.append('1')
        elif binario1[i] == '0' and binario2[i] == '1' or binario1[i] == '1' and binario2[i] == '0':
            if acarreo[i+1] == '0':
                resultado_suma_invertido.append('1')
            else:
                resultado_suma_invertido.append('0')
                acarreo[i] = '1'
        else:
            if acarreo[i+1] == '0':
                resultado_suma_invertido.append('0')
                acarreo[i] = '1'
            else:
                resultado_suma_invertido.append("1")
    if acarreo[0] == '1':
        resultado_suma_invertido.append('1')

    resultado_suma = resultado_suma_invertido[::-1]
    return resultado_suma


def resta_binarios(binario1, binario2):
    quitar = list("000000000")

    resultado_resta_invertido = []


    for i in range(len(binario1) - 1, -1, -1):
        if binario1[i] == '0' and binario2[i] == '0':
            if quitar[i+1] == '0':
                resultado_resta_invertido.append('0')
            else:
                resultado_resta_invertido.append('1')
                quitar[i] = '1'
        elif binario1[i] == '1' and binario2[i] == '0':
            if quitar[i+1] == '0':
                resultado_resta_invertido.append('1')
            else:
                resultado_resta_invertido.append('0')
        elif binario1[i] == '0' and binario2[i] == '1':
            if quitar[i+1] == '0':
                resultado_resta_invertido.append('1')
                quitar[i] = '1'
            else:
                resultado_resta_invertido.append('0')
                quitar[i] = '1'
        else:
            if quitar[i+1] == '0':
                resultado_resta_invertido.append('0')
            else:
                resultado_resta_invertido.append('1')

    resultado_resta = resultado_resta_invertido[::-1]
    return resultado_resta



def main():
    datos = lee_los_binarios()

    if datos and len(datos) == 2:
        binario1, binario2 = datos

        resultado_suma = suma_binarios(binario1, binario2)
        print("El resultado la suma de estos dos numeros es: ", resultado_suma)

        resultado_resta = resta_binarios(binario1, binario2)
        print("El resultado la resta de estos dos numeros es: ", resultado_resta)

    elif datos and len(datos) == 3:
        binario1, operando, binario2 = datos

        if operando == '+':
            resultado = suma_binarios(binario1, binario2)
            print("El resultado la suma de estos dos numeros es: ", resultado)

        elif operando == '-':
            resultado = resta_binarios(binario1, binario2)
            print("El resultado la resta de estos dos numeros es: ", resultado)

        else:
            print("Operando no valido. Usa '+' o '-'.")

if __name__ == '__main__':
    main()