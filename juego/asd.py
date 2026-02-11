"""TODO: Tablero 8x8. Barcos: 5 (Portaaviones), 4 (Acorazado), 3 (Submarino), 3 (Crucero), 3 (Destructor) 2 Coordenadas (letra,numero), numero: fila, letra, columna"""
from random import randint, choice
from pprint import pprint
"""
TODO: 
--- Funciones mínimas ---
- colocar_barcos(tablero_jugador1 : list[list[Any]]
- recibir_disparo(tablero,fila,col) : String --> "AGUA" , "TOCADO" o "HUNDIDO"

*** A implementar ***
- El juego se acaba cuando el contador de barcos hundidos sea igual al número de barcos a hundir.
- Símbolos:
    - "~" : agua
    - numeros identificativos barcos
    - X : tocado --> cuando todas las coordenadas de un barco sean igual a "X" se retornará "HUNDIDO"
    - O : disparo al agua
"""

DIRECCIONES = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1), (0, 1),
    (1, -1), (1, 0), (1, 1),
]

DIRECCIONES_ADYACENTES = [
    (-1, 0),
    (0, -1), (0, 1),
    (1, 0),
]

TAMAÑO_TABLERO = 8
NUM_BARCOS = 5

AGUA = "~"
TOCADO = "X"
FALLO = "O"


def zona_adyacente_libre(tablero_jugador1 : list[list],fila : int, columna : int) -> bool:
    if tablero_jugador1[fila][columna] != "~":
        return False
    for direccion_fila,direccion_columna in DIRECCIONES:
        nueva_fila = fila + direccion_fila
        nueva_columna = columna + direccion_columna
        if 0 <= nueva_fila < TAMAÑO_TABLERO and 0 <= nueva_columna < TAMAÑO_TABLERO:
            if tablero_jugador1[nueva_fila][nueva_columna] != "~":
                return False
    return True
def colocar_un_barco(tablero_jugador1: list[list], tamaño_barco : int, id_barco : str):
    orientaciones = ["Horizontal", "Vertical"]
    colocado = False

    while not colocado:
        orientacion = choice(orientaciones)
        max_inicio_barco = TAMAÑO_TABLERO - tamaño_barco
        inicio_barco = randint(0,max_inicio_barco)
        if orientacion == "Horizontal":
            fila = randint(0,TAMAÑO_TABLERO - 1)
            tramo_libre = True
            for columna in range(inicio_barco,inicio_barco + tamaño_barco):
                if not zona_adyacente_libre(tablero_jugador1,fila,columna):
                    tramo_libre = False
            if tramo_libre:
                for columna in range(inicio_barco,inicio_barco + tamaño_barco):
                    tablero_jugador1[fila][columna] = id_barco
                colocado = True
        else:
            columna = randint(0, TAMAÑO_TABLERO - 1)
            tramo_libre = True
            for fila in range(inicio_barco, inicio_barco + tamaño_barco):
                if not zona_adyacente_libre(tablero_jugador1, fila, columna):
                    tramo_libre = False
            if tramo_libre:
                for fila in range(inicio_barco, inicio_barco + tamaño_barco):
                    tablero_jugador1[fila][columna] = id_barco
                colocado = True

def desparsear_letra(letra : str) -> int:
    match letra:
        case "A":
            return 0
        case "B":
            return 1
        case "C":
            return 2
        case "D":
            return 3
        case "E":
            return 4
        case "F":
            return 5
        case "G":
            return 6
        case "H":
            return 7

def parsear_letra(coordenada_y: int) -> str:
    match coordenada_y:
        case 0:
            return "A"
        case 1:
            return "B"
        case 2:
            return "C"
        case 3:
            return "D"
        case 4:
            return "E"
        case 5:
            return "F"
        case 6:
            return "G"
        case 7:
            return "H"


def comprobar_hundimiento(tablero_jugador1 : list[list[str]], id_barco : str) -> bool:
    """
    Verifica que todas las casillas del barco con id_barco están tocadas
    """
    for fila in range(TAMAÑO_TABLERO):
        for columna in range(TAMAÑO_TABLERO):
            if tablero_jugador1[fila][columna] == id_barco:
                return False
    return True

def recibir_disparo(tablero_jugador1: list[list[str]], coord: str) -> str:
    fila = int(coord[1]) - 1
    columna = desparsear_letra(coord[0])
    casilla = tablero_jugador1[fila][columna]

    if casilla == FALLO or casilla == TOCADO:
        return "YA DISPARADO"
    elif casilla == AGUA:
        tablero_jugador1[fila][columna] = FALLO
        return "AGUA"
    else:
        id_barco = casilla
        tablero_jugador1[fila][columna] = TOCADO
        if comprobar_hundimiento(tablero_jugador1, id_barco):
            return "HUNDIDO"
        return "TOCADO"

def paridad(tablero_jugador2 : list[list[str]]):
    for i in range(TAMAÑO_TABLERO):
        for j in range(TAMAÑO_TABLERO):
            preferente = (i + j) % 2 == 0
            if preferente and tablero_jugador2[i][j] == AGUA:
                disparo = parsear_letra(j) + str(i + 1) # Coordenada a mandar (y,x)
                return disparo,i,j




def target(tablero_jugador2 : list[list[str]],posiciones_barco_actual : list[tuple[int,int]]) -> tuple[str,int,int] | None:
    """
    posiciones_barco_actual : list[tuple[int,int]])
    Estrategia inteligente de disparo:
    1. Si solo hay 1 posición tocada -> probar las 4 direcciones adyacentes
    2. Si hay 2+ posiciones -> detectar el eje y disparar en ese eje en ambos sentidos

    Retorna: (coordenada_disparo, fila, columna) o None si no hay casillas válidas
    """
    hundido = False

    if len(posiciones_barco_actual) == 0:
        return None

    if len(posiciones_barco_actual) == 1:
        col_base, fila_base = posiciones_barco_actual[0]
        for direccion in DIRECCIONES_ADYACENTES:
            fila_disparo = fila_base + direccion[0]
            col_disparo = col_base + direccion[1]
            if 0 <= fila_disparo < TAMAÑO_TABLERO and 0 <= col_disparo < TAMAÑO_TABLERO:
                if tablero_jugador2[fila_disparo][col_disparo] == AGUA:
                    disparo = parsear_letra(col_disparo) + str(fila_disparo + 1)
                    return disparo,fila_disparo,col_disparo
        return None

    posiciones_ordenadas = sorted(posiciones_barco_actual)

    filas = [pos[0] for pos in posiciones_ordenadas]
    columnas = [pos[1] for pos in posiciones_ordenadas]

    es_horizontal = len(set(filas)) == 1  # Todas las filas son iguales -> Horizontal
    es_vertical = len(set(columnas)) == 1  # Todas las columnas son iguales -> Vertical

    if es_horizontal:
        # Barco horizontal -> disparar a izquierda y derecha
        fila = filas[0]
        col_min = min(columnas)
        col_max = max(columnas)
        # Intentar disparar a la izquierda (col_min - 1)
        if col_min - 1 >= 0:
            if tablero_jugador2[fila][col_min - 1] == AGUA:
                disparo = parsear_letra(col_min - 1) + str(fila + 1)
                return disparo, fila, col_min - 1

        # Intentar disparar a la derecha (col_max + 1)
        if col_max + 1 < TAMAÑO_TABLERO:
            if tablero_jugador2[fila][col_max + 1] == AGUA:
                disparo = parsear_letra(col_max + 1) + str(fila + 1)
                return disparo, fila, col_max + 1
    elif es_vertical:
        # Barco vertical → disparar arriba y abajo
        columna = columnas[0]
        fila_min = min(filas)
        fila_max = max(filas)
        # Intentar disparar arriba (fila_min - 1)
        if fila_min - 1 >= 0:
            if tablero_jugador2[fila_min - 1][columna] == AGUA:
                disparo = parsear_letra(columna) + str(fila_min)  # fila_min (no +1 porque es index 0)
                return disparo, fila_min - 1, columna
        # Intentar disparar abajo (fila_max + 1)
        if fila_max + 1 < TAMAÑO_TABLERO:
            if tablero_jugador2[fila_max + 1][columna] == AGUA:
                disparo = parsear_letra(columna) + str(fila_max + 2)  # +2 porque es index y display
                return disparo, fila_max + 1, columna

    return None

def marcar_zona_muerta(tablero_jugador2: list[list[str]],posiciones_barco_actual: list[tuple[int, int]]):
    """
    Marca como 'O' todas las casillas de agua (~) adyacentes
    (8 direcciones) a las posiciones del barco hundido.
    """
    for fila, columna in posiciones_barco_actual:
        for direccion_fila, direccion_columna in DIRECCIONES:
            nueva_fila = fila + direccion_fila
            nueva_columna = columna + direccion_columna
            if 0 <= nueva_fila < TAMAÑO_TABLERO and 0 <= nueva_columna < TAMAÑO_TABLERO:
                if tablero_jugador2[nueva_fila][nueva_columna] == AGUA:
                    tablero_jugador2[nueva_fila][nueva_columna] = FALLO
