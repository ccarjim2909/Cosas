fun main() {
    println("Introduce el dividendo (número a dividir): ")
    val n1 = readln().toDouble()

    println("Introduce el divisor (número que divide): ")
    val n2 = readln().toDouble()

    if (n2 == 0.0) {
        println("Error: No se puede dividir por cero.")
    } else {
        val resultado = n1 / n2
        println("El resultado de dividir $n1 entre $n2 es: $resultado")
    }
}