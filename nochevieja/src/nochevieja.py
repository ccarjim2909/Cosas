# programa.py
# -*- coding: utf-8 -*-
"""
Radares de tramo — Esqueleto para alumnos
- Lectura de fichero YA resuelta (función leer_casos).
- main() itera sobre las líneas y llama a procesar_linea(linea).
- procesar_linea(linea) está VACÍA; los alumnos deben implementarla.
"""

from typing import List
import sys
from pathlib import Path


def leer_casos(ruta_fichero: str) -> List[str]:
    """
    Lee un fichero de texto con casos de prueba, devolviendo
    una lista de líneas (str) ya limpias, sin la línea de terminación "0 0 0".
    Ignora líneas en blanco y comentarios que empiecen por '#'.
    """
    ruta = Path(ruta_fichero)
    if not ruta.exists():
        raise FileNotFoundError(f"No existe el fichero: {ruta_fichero}")

    casos: List[str] = []
    with ruta.open(encoding="utf-8") as f:
        for raw in f:
            linea = raw.strip()
            if not linea or linea.startswith("#"):
                continue
            if linea == "00:00":
                break
            casos.append(linea)
    return casos


def procesar_linea(linea: str) -> str:
    """
    TODO: Implementar por el alumnado.


    """
    # --- Implementación del alumnado aquí ---
    partes = linea.split(":")

    numero1 = partes[0]
    numero2 = partes[1]


    if not (numero1.isdigit() and numero2.isdigit()):
        return "ERROR"


    horas = int(numero1)
    minutos = int(numero2)

    if not (0 <= horas <= 23 and 0 <= minutos <= 59):
        return "ERROR"

    minutos_transcurridos = horas * 60 + minutos


    minutos_totales_dia = 24 * 60
    minutos_faltantes = minutos_totales_dia - minutos_transcurridos

    return str(minutos_faltantes)


     #raise NotImplementedError("Función aún no implementada por el alumnado.")

# a main se llama de la siguiente forma  main(sys.argv)
def main(argv: List[str]) -> None:
    if len(argv) < 2:
        print("Uso: python programa.py <ruta_entrada.txt>")
        sys.exit(1)

    ruta = argv[1]
    for linea in leer_casos(ruta):
        resultado = procesar_linea(linea)   # <- llamada a la función de los alumnos
        print(resultado)                     # <- impresión del resultado

