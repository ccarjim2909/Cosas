fun main() {
    println("Escribe tu nombre completo: ")
    val nombre = readln()

    println(nombre.lowercase())

    println(nombre.uppercase())


    val nombreFormateado = nombre.split(" ").joinToString(" ") { palabra ->
        palabra.lowercase().replaceFirstChar { it.uppercase() }
    }
    println(nombreFormateado)
}