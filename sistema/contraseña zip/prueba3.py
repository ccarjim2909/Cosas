import itertools
import pyzipper
import time


def formatear_tiempo(segundos):
    if segundos < 60:
        return round(segundos,2),"segundos"
    else:
        minutos = int(segundos // 60)
        segundos = segundos % 60
        return minutos, "minutos", round(segundos,2), "segundos"


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

    letras_mayus = list("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ")
    letras_minus = list("abcdefghijklmnñopqrstuvwxyz")
    numeros = list("0123456789")

    caracteres = letras_mayus + letras_minus + numeros

    longitud = 4

    inicio = time.time()
    contraseña = crack_zip(ruta_zip, caracteres, longitud)
    fin = time.time()

    abrir_archivo(ruta_zip, salida, contraseña)

    #esto devuelve una tupla mirar para que suelte todo sin tupla
    tiempo = fin - inicio
    print("Tiempo:", formatear_tiempo(tiempo))


if __name__ == "__main__":
    main()
