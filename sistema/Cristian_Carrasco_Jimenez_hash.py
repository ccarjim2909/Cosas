import sys
import hashlib
import itertools
import time



def validar_entradas():
    if len(sys.argv) != 3:
        return False, "Error, el uso normal es asi: python Cristian_Carrasco_Jimenez_hash.py <hash_a_buscar> <longitud_palabra>", None

    hash_palabra = sys.argv[1]
    longitud_arg = sys.argv[2]


    if len(hash_palabra) != 64:
        return False, ("Error: El hash SHA-256 debe tener 64 caracteres. Se proporcionaron",len(hash_palabra)),None
    if not all(c in "0123456789abcdefABCDEF" for c in hash_palabra):
        return False, "Error: El hash debe contener solo caracteres hexadecimales (0-9, a-f)", None


    try:
        longitud = int(longitud_arg)
    except ValueError:
        return False, "Error: La longitud debe ser un numero valido.", None
    if longitud <= 0:
        return False, "Error: La longitud de la palabra debe ser un numero entero positivo.", None


    return True, hash_palabra, longitud


def buscar_por_hash(listas: list, longitud: int, hash_buscado: str):
    for caracter in itertools.product(listas, repeat=longitud):
        combinacion = ''.join(caracter)
        hash_combinacion = hashlib.sha256(combinacion.encode()).hexdigest()

        if hash_combinacion == hash_buscado:
            return combinacion, hash_combinacion
    return None, None


def main():
    valido, dato1, dato2 = validar_entradas()

    if not valido:
        print(dato1)
        return

    hash_palabra = dato1
    longitud = dato2

    letras_mayus = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S",
                    "T", "U", "V", "W", "X", "Y", "Z"]
    letras_minus = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s",
                    "t", "u", "v", "w", "x", "y", "z"]
    numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    caracteres_especiales = ["!", "@", "#", "$", "%", "&", "/", "(", ")", "=", "?", "¿", "*", "+", "-", "_", ",", "."]

    listas = letras_minus + letras_mayus + numeros + caracteres_especiales


    inicio = time.time()
    resultado, hash_encontrado = buscar_por_hash(listas, longitud, hash_palabra)
    fin = time.time()

    segundos = round(fin - inicio,2)


    if resultado:
        print("Encontrado:" ,resultado, "->" ,hash_encontrado)
        print("Tiempo de ejecucion:" ,segundos, "segundos")
    else:
        print("No se encontro la palabra para el hash dado con la longitud especificada,\n"
              "tal vez la palabra cifrada no tiene la longitud que pusiste.")



if __name__ == "__main__":
    main()