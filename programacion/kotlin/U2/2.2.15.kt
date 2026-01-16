fun main() {
    var suma = 0
    var numero: Int


    do {
        println("Introduce un número entero (0 para terminar): ")
        numero = readln().toInt()

        if (numero > 0) {
            suma += numero
        }

    } while (numero != 0)

    println("La suma de los números positivos ingresados es: $suma")
}