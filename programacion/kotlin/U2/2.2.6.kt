fun main() {
    println("Introduce la altura del triángulo (número entero): ")
    val altura = readln().toInt()

    for (i in 1..altura) {

        for (j in 1..i) {
            print("*")
        }

        println()
    }
}