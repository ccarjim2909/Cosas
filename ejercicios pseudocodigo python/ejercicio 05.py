#Cálculo del importe total de un servicio
#escripción: Calcula el importe total multiplicando horas trabajadas por el precio por hora.
#Entrada: Horas (número), coste_por_hora (número).
#Salida: Importe total.


horas = int(input("Introduce el número de horas trabajadas: "))
coste = float(input("Introduce el coste por hora: "))

sueldo = horas * coste

print("El sueldo seria de:", sueldo)