fun main() {
    println("¿Cuántos años tienes? ")


    val edad = readln().toInt()


    for (año in 1..edad) {
        println("Has cumplido $año años")
    }
}