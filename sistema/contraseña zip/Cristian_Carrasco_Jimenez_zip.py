import itertools
import pyzipper
import zlib
from pyzipper import BadZipFile
import time

def buscar_por_hash(listas: list, longitud: int):
    ruta_zip = r"C:\Users\UsuarioM\Desktop\Sistema informatico\contraseña zip\asd.zip"
    salida   = r"C:\Users\UsuarioM\Desktop\Sistema informatico\contraseña zip\salida"

    # tengo que abrir el archivo aqui

    for caracteres in itertools.product(listas, repeat=longitud):
        password = ''.join(caracteres)
        pwd = password.encode()

        try:
            with pyzipper.ZipFile(ruta_zip) as z:
                z.extractall(salida, pwd=pwd)

            print("Contraseña correcta encontrada:", password)
            return "extraído"

        except (RuntimeError, zlib.error, BadZipFile):
            print("Incorrecta:", password)
            # time.sleep(0.001)
            continue

    return "no extraído"





def main():
    longitud = 4

    letras_mayus = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S",
                    "T", "U", "V", "W", "X", "Y", "Z"]
    letras_minus = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s",
                    "t", "u", "v", "w", "x", "y", "z"]
    numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    listas = letras_minus + letras_mayus + numeros

    buscar_por_hash(listas, longitud)



if __name__ == '__main__':
    main()
