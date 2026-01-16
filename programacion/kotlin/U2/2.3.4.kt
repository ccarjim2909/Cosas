fun main() {
    print("Introduce un número entero: ")
    val entrada = readln()

    try {
        val numero = entrada.toInt()
        println("Has introducido el número: $numero")

    } catch (e: NumberFormatException) {
        println("La entrada no es correcta")
        throw e
    }
}