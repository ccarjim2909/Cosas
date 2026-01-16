fun main() {
    var contadorPares = 0

    println("Ingresa un número entero positivo (-1 para salir): ")
    var numero = readln().toInt()

    while (numero != -1) {

        if (numero % 2 == 0) {
            contadorPares++
        }

        var sumaDigitos = 0
        var auxiliar = numero

        while (auxiliar > 0) {
            sumaDigitos += auxiliar % 10
            auxiliar /= 10
        }

        println("La suma de los dígitos de $numero es: $sumaDigitos")


        println("Ingresa otro número entero positivo (-1 para salir): ")
        numero = readln().toInt()
    }

    println("\nCantidad de números pares ingresados: $contadorPares")
}