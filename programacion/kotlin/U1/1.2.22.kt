fun main() {
    println("Introduce una frase: ")
    val frase = readln()

    println("Introduce una vocal: ")
    val vocal = readln()

    val fraseModificada = frase.replace(vocal, vocal.uppercase(), ignoreCase = true)

    println("La nueva frase es: $fraseModificada")
}