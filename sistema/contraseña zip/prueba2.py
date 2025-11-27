import itertools
import pyzipper
import zlib
from pyzipper import BadZipFile

def buscar_contraseña(chars, longitud):
    ruta_zip = r"C:\Users\UsuarioM\Desktop\Sistema informatico\contraseña zip\diccionario.zip"
    salida   = r"C:\Users\UsuarioM\Desktop\Sistema informatico\contraseña zip\salida2"

    with pyzipper.AESZipFile(ruta_zip) as zip:
        # Tomamos sólo un archivo para probar más rápido
        nombre_archivo = zip.namelist()[0]

        for combo in itertools.product(chars, repeat=longitud):
            pwd = "".join(combo).encode()

            try:
                # Intentamos leer SOLO un archivo, no todo el ZIP
                zip.read(nombre_archivo, pwd=pwd)

                print("Contraseña encontrada:", pwd.decode())
                zip.extractall(salida, pwd=pwd)
                return pwd.decode()

            except:
                pass  # nada de prints ni sleep

    return None


def main():
    longitud = 4

    letras_mayus = list("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ")
    letras_minus = list("abcdefghijklmnñopqrstuvwxyz")
    numeros = list("0123456789")

    chars = letras_mayus + letras_minus + numeros

    buscar_contraseña(chars, longitud)


if __name__ == '__main__':
    main()

