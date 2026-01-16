fun main() {
    print("Introduce un número entero positivo: ")
    val entrada = readln()

    try {
        val n = entrada.toInt()

        if (n <= 0) {
            println("Error: El número debe ser mayor que cero.")
        } else {
            for (i in 1..n step 2) {
                if (i + 2 > n) {
                    print(i)
                } else {
                    print("$i, ")
                }
            }
            println()
        }

    } catch (e: NumberFormatException) {
        println("Error: Lo que has introducido no es un número entero válido.")
    }
}