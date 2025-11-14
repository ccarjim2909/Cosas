
def saca_vocales(palabra: str)  -> str:
    resultado = ""
    for letra in palabra:
        if letra == "a" or letra == "A" or letra == "á" or letra == "Á":
            resultado = resultado + letra
        elif letra == "e" or letra == "E" or letra == "é" or letra == "É":
            resultado = resultado + letra
        elif letra == "i" or letra == "I" or letra == "í" or letra == "Í":
            resultado = resultado + letra
        elif letra == "o" or letra == "O" or letra == "ó" or letra == "Ó":
            resultado = resultado + letra
        elif letra == "u" or letra == "U" or letra == "ú" or letra == "Ú":
            resultado = resultado + letra


    #resultado
    return resultado

def saca_vocales2(palabra: str)  -> str:
    vocales = "aeiouAEIOUáéíóúÁÉÍÓÚ"
    resultado = ""
    for letra in palabra:
        if letra in vocales:
            resultado = resultado + letra


    #resultado
    return resultado