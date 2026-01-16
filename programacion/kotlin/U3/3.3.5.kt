fun main() {
    val numeros = setOf(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

    val pares = numeros.filter { it % 2 == 0 }.toSet()

    val multiplos_de_tres = numeros.filter { it % 3 == 0 }.toSet()

    val pares_y_multiplos_de_tres = pares.intersect(multiplos_de_tres)

    println("Conjunto Original: $numeros")
    println("Pares: $pares")
    println("Múltiplos de tres: $multiplos_de_tres")
    println("---")
    println("Intersección (Pares y Múltiplos de 3): $pares_y_multiplos_de_tres")
}