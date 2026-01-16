fun main() {
    for (i in 1..10) {
        println("TABLA DEL $i")
        println("----------")

        for (j in 1..10) {
            val resultado = i * j
            println("$i x $j = $resultado")
        }

        println()
    }
}