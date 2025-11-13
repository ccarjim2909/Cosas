import sys
import hashlib
import itertools
import time


def buscar_por_hash(listas:list, longitud:int, hash:str):
    for caracter in itertools.product(listas, repeat=longitud):
        combinacion = ''.join(caracter)
        hash_combinacion = hashlib.sha256(combinacion.encode()).hexdigest()
        if hash_combinacion == hash:
            return combinacion, hash_combinacion
    return None, None




def main():
    inicio = time.time()
    letras_mayus = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S",
                    "T", "U", "V", "W", "X", "Y", "Z"]
    letras_minus = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s",
                    "t", "u", "v", "w", "x", "y", "z"]
    numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    caracteres_especiales = ["!", "@", "#", "$", "%", "&", "/", "(", ")", "=", "?", "¿", "*", "+", "-", "_", ",", "."]

    listas = letras_mayus + letras_minus + numeros + caracteres_especiales


    hash_palabra = sys.argv[1]
    longitud = int(sys.argv[2])
    # hash_palabra = hashlib.sha256(palabra.encode()).hexdigest()
    # hash_palabra = "5e01d7a18db038714fcbb6de5708f3f3c36ef61c206c72ce5dd91c149ecc910c"

    resultado, hash_encontrado = buscar_por_hash(listas, longitud, hash_palabra)

    fin = time.time()
    segundos = round(fin - inicio)
    if resultado:
        print("Encontrado:", resultado, "->", hash_encontrado)
        print("Tiempo de ejecucion:", segundos, "segundos")
    else:
        print("No se encontro.")
        print("Tiempo de ejecucion:", segundos, "segundos")



if __name__ == "__main__":
    main()