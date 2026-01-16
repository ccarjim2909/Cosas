fun main() {
    println("Escribe lo que quieras (escribe 'salir' para terminar):")

    var continuar = true

    while (continuar) {
        print("> ")
        val entrada = readln()

        if (entrada.lowercase() == "salir") {
            continuar = false
            println("¡Adiós!")
        } else {
            println("Eco: $entrada")
        }
    }
}