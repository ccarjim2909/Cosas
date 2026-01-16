fun main() {
    println("Introduce una palabra: ")
    val palabra = readln().lowercase()

    val caracteres = palabra.toList()

    val caracteresAlReves = caracteres.reversed()

    if (caracteres == caracteresAlReves) {
        println("La palabra '$palabra' es un palíndromo.")
    } else {
        println("La palabra '$palabra' no es un palíndromo.")
    }
}