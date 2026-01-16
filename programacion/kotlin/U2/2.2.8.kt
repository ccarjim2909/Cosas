fun main() {
    println("Introduce la altura del triángulo (número de filas): ")
    val n = readln().toInt()

    for (i in 1..n) {


        val inicioFila = 2 * i - 1

        for (j in inicioFila downTo 1 step 2) {
            print("$j ")
        }

        println()
    }
}