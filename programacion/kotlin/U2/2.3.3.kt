fun main() {
    var esValido = false
    var n = 0

    while (!esValido) {
        print("Introduce un número entero positivo para la cuenta atrás: ")
        val entrada = readln()

        try {
            n = entrada.toInt()

            if (n >= 0) {
                esValido = true
            } else {
                println("Error: Por favor, introduce un número que no sea negativo.")
            }
        } catch (e: NumberFormatException) {
            println("Error: '${entrada}' no es un número entero válido.")
        }
    }

    println("\nIniciando cuenta atrás:")
    for (i in n downTo 0) {
        if (i > 0) {
            print("$i, ")
        } else {
            print(i)
        }
    }
    println()
}