fun main() {
    val numerosGanadores = mutableListOf<Int>()
    val cantidadTotal = 6

    println("Introduce los $cantidadTotal números de la combinación ganadora:")


    while (numerosGanadores.size < cantidadTotal) {
        print("Introduce el número ${numerosGanadores.size + 1}: ")
        val num = readln().toInt()

        numerosGanadores.add(num)
    }

    numerosGanadores.sort()

    println("\nLos números ganadores ordenados son: $numerosGanadores")
}