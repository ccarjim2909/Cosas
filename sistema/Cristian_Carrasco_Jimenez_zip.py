import itertools
import pyzipper
import time
import os


def formatear_tiempo(segundos):
    if segundos < 60:
        return str(round(segundos,2)) + " segundos"
    else:
        minutos = int(segundos // 60)
        segs = round(segundos % 60, 2)
        return str(minutos) + " minutos y " + str(segs) + " segundos"


def validar_archivo(ruta):
    if not os.path.isfile(ruta):
        print("Error: El archivo",ruta, "no existe.")
        return False
    return True


def validar_carpeta(ruta):
    if not os.path.exists(ruta):
        os.makedirs(ruta)
        print("Se creó la carpeta de salida:", ruta)





def crack_zip(ruta_zip, caracteres, longitud):
    if not validar_archivo(ruta_zip):
        return None

    try:
        with pyzipper.ZipFile(ruta_zip) as zip:
            archivo = zip.namelist()[0]

            for combinacion in itertools.product(caracteres, repeat=longitud):
                contraseña = "".join(combinacion)
                try:
                    with zip.open(archivo, pwd=contraseña.encode()) as fichero:
                        fichero.read(1)
                    print("\nContraseña encontrada:", contraseña)
                    return contraseña
                except:
                    continue
    except Exception as error:
        print("Error al abrir", ruta_zip,":", error)
        return None

    print("\nNo se encontró la contraseña por fuerza bruta.")
    return None




def crack_zip_diccionario(ruta_zip, ruta_diccionario):
    print("\nProbando contraseñas del diccionario...")

    if not validar_archivo(ruta_zip) or not validar_archivo(ruta_diccionario):
        return None

    try:
        with open(ruta_diccionario, "r", encoding="utf-8", errors="ignore") as fichero:
            contraseñas = [linea.strip() for linea in fichero if linea.strip()]
    except Exception as error:
        print("Error al abrir", ruta_zip,":", error)
        return None

    if not contraseñas:
        print("El diccionario", ruta_diccionario, "está vacío.")
        return None

    try:
        with pyzipper.ZipFile(ruta_zip) as zip:
            archivo = zip.namelist()[0]
            for contraseña in contraseñas:
                try:
                    with zip.open(archivo, pwd=contraseña.encode()) as fichero:
                        fichero.read(1)
                    print("\nContraseña encontrada:", contraseña)
                    return contraseña
                except:
                    continue
    except Exception as error:
        print("Error al abrir", ruta_zip,":", error)
        return None

    print("\nNo se encontró la contraseña en el diccionario.")
    return None


def abrir_archivo(ruta_zip, ruta_salida, contraseña):
    if contraseña is None:
        print("No se puede extraer: no se encontró la contraseña.")
        return

    validar_carpeta(ruta_salida)

    try:
        with pyzipper.ZipFile(ruta_zip) as zip:
            zip.extractall(path=ruta_salida, pwd=contraseña.encode())
        print("Archivo extraído correctamente en:", ruta_salida)
    except Exception as error:
        print("Error al abrir", ruta_zip,":", error)



def main():
    letras_mayus = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S",
                    "T", "U", "V", "W", "X", "Y", "Z"]
    letras_minus = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s",
                    "t", "u", "v", "w", "x", "y", "z"]
    numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    caracteres = letras_mayus + letras_minus + numeros
    longitud = 4



    # Archivo 1
    ruta_diccionario = r".\diccionario.zip"
    salida_diccionario = r".\diccionario"

    print("Descifrando el primer archivo (diccionario.zip)")
    inicio = time.time()
    contraseña = crack_zip(ruta_diccionario, caracteres, longitud)
    fin = time.time()

    if contraseña is None:
        print("No se pudo descifrar el archivo diccionario.zip. Cancelando ejecución.")
        return

    abrir_archivo(ruta_diccionario, salida_diccionario, contraseña)
    tiempo = fin - inicio
    print("Tiempo:", formatear_tiempo(tiempo))



    # Archivo 2
    ruta_zip_objetivo = r".\compress.zip"
    salida_final = r".\extraido_compress"

    if not os.path.exists(salida_diccionario):
        print("No se encontró la carpeta de salida del diccionario:", salida_diccionario)
        return

    ficheros = os.listdir(salida_diccionario)
    diccionario_txt = None
    for fichero in ficheros:
        if fichero.endswith(".txt"):
            diccionario_txt = os.path.join(salida_diccionario, fichero)
            break

    if not diccionario_txt:
        print("No se encontró ningún .txt dentro de la extracción del diccionario.")
        return


    inicio2 = time.time()
    contraseña2 = crack_zip_diccionario(ruta_zip_objetivo, diccionario_txt)
    fin2 = time.time()

    if contraseña2 is None:
        print("No se pudo descifrar 'compress.zip'. Cancelando ejecución.")
        return

    abrir_archivo(ruta_zip_objetivo, salida_final, contraseña2)

    tiempo2 = fin2 - inicio2
    print("Tiempo:", formatear_tiempo(tiempo2))

if __name__ == "__main__":
    main()