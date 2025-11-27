import itertools
import pyzipper
import time


def formatear_tiempo(segundos):
    if segundos < 60:
        return str(round(segundos,2)) + " segundos"
    else:
        minutos = int(segundos // 60)
        segs = round(segundos % 60, 2)
        return str(minutos) + " minutos y " + str(segs) + " segundos"


def crack_zip(ruta_zip, caracteres, longitud):
    with pyzipper.ZipFile(ruta_zip) as zip:
        archivo = zip.namelist()[0]

        for combinacion in itertools.product(caracteres, repeat=longitud):
            contraseña = "".join(combinacion)

            try:
                with zip.open(archivo, pwd=contraseña.encode()) as f:
                    f.read(1)

                print("\nContraseña encontrada:", contraseña)
                return contraseña

            except:
                continue

    print("\nNo encontrada")
    return None


def abrir_archivo(ruta_zip, ruta_salida, contraseña):
    if contraseña is None:
        print("No se puede extraer: no se encontró la contraseña.")
        return

    with pyzipper.ZipFile(ruta_zip) as zip:
        zip.extractall(path=ruta_salida, pwd=contraseña.encode())

    print("Archivo extraído correctamente.")


def main():
    ruta_zip = r"C:\Users\UsuarioM\Desktop\Sistema informatico\contraseña zip\diccionario.zip"
    salida = r"C:\Users\UsuarioM\Desktop\Sistema informatico\contraseña zip\salida"

    letras_mayus = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S",
                    "T", "U", "V", "W", "X", "Y", "Z"]
    letras_minus = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s",
                    "t", "u", "v", "w", "x", "y", "z"]
    numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    caracteres = letras_mayus + letras_minus + numeros

    longitud = 4

    inicio = time.time()
    contraseña = crack_zip(ruta_zip, caracteres, longitud)
    fin = time.time()

    abrir_archivo(ruta_zip, salida, contraseña)

    tiempo = fin - inicio

    print("Tiempo:", formatear_tiempo(tiempo))

if __name__ == "__main__":
    main()
