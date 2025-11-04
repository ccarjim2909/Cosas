def pedir_numeros():
    numero1 = int(input("Ingresa un numero: "))

    return numero1

def par_impar(numero:int)->bool:
    if numero % 2 == 0:
        return True
    else:
        return False



def main():
    numero = pedir_numeros()
    if par_impar(numero):
        print("El numero es par")
    else:
        print("El numero es impar")


if __name__ == '__main__':
    main()