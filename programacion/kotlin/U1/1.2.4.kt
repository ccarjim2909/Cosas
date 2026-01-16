fun main() {
    println("Escribe la temperatura en grados Celsius: ")

    val celsius = readln().toDouble()

    val fahrenheit = (celsius * 9 / 5) + 32

    println("$celsius ºC equivalen a $fahrenheit ºF.")
}