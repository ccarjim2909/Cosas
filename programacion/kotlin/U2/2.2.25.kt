fun main() {
    println("Introduce una frase: ")
    val entrada = readln().trim()

    if (entrada.isEmpty()) {
        println("No has introducido ninguna frase.")
    } else {
        val palabras = entrada.split(Regex("\\s+"))

        var palabraMasLarga = ""
        val totalPalabras = palabras.size

        for (palabra in palabras) {
            if (palabra.length > palabraMasLarga.length) {
                palabraMasLarga = palabra
            }
        }

        println("\nResultados:")
        println("Número total de palabras: $totalPalabras")
        println("La palabra más larga es: \"$palabraMasLarga\"")
    }
}