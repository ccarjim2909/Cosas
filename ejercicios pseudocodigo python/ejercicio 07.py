#Cálculo del precio final con IVA
#Descripción: Calcula el precio final sumando al precio sin IVA el porcentaje de IVA indicado.
#Entrada: precio_sin_iva (número), iva (%)
#Salida: precio_final.


precio_sin_iva = float(input("Introduce el precio sin IVA: "))
iva = float(input("Introduce el porcentaje de IVA: "))

precio_iva = precio_sin_iva * iva / 100
precio_final = precio_sin_iva + precio_iva

print("El precio final es:", precio_final, "€")