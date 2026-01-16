fun main() {
    print("Introduce una palabra: ")
    val palabra = readln().lowercase()

    val vocales = listOf('a', 'e', 'i', 'o', 'u')

    for (vocal in vocales) {
        var contador = 0

        for (letra in palabra) {
            if (letra == vocal) {
                contador++
            }
        }

        println("La vocal '$vocal' aparece $contador veces")
    }
}