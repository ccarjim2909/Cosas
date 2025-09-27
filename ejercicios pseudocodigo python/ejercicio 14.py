#Índice de masa corporal (IMC)
#Descripción: Calcula el IMC a partir del peso (kg) y la altura (m).
#Entrada: peso (kg), altura (m).
#Salida: IMC.


peso = float(input("Introduce tu peso: "))
altura = float(input("Introduce tu altura: "))

imc = peso / (altura * altura)
print("Tu índice de masa corporal es", imc)
