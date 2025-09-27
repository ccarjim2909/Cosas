#Calcular importe sin IVA e IVA pagado
#Descripción: Dado el precio final (con IVA), calcula el precio sin IVA y el IVA pagado (asume 10%).
#Entrada: precio_final (número).
#Salida: precio_sin_iva, iva_pagado.


precio_final = float(input("Introduce el precio final: "))

iva_pagado = precio_final * 0.10
precio_sin_iva = precio_final - iva_pagado

print("El precio del producto sin IVA es", precio_sin_iva, "€ y el IVA pagado fue", iva_pagado, "€")
