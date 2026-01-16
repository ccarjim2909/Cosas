fun main() {
    print("Introduce un número entero positivo: ")
    val n = readln().toInt()

    for (i in n downTo 0) {

        if (i > 0) {
            print("$i, ")
        } else {
            print(i)
        }
    }
}