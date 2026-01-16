fun main() {
    val alfabeto = ('a'..'z').toSet()

    val vocales = setOf('a', 'e', 'i', 'o', 'u')

    val consonantes = alfabeto.subtract(vocales)

    val letras_comunes = vocales.intersect(consonantes)

    println("Vocales: $vocales")
    println("\nConsonantes (${consonantes.size} letras):")
    println(consonantes)

    println("\n--- RESULTADO DE LA INTERSECCIÓN ---")
    if (letras_comunes.isEmpty()) {
        println("Letras comunes: $letras_comunes (Conjunto vacío)")
        println("Explicación: No hay letras comunes porque las vocales y las consonantes son conjuntos disjuntos.")
    } else {
        println("Letras comunes: $letras_comunes")
    }
}