fun main() {
    println("Introduce las traducciones en formato 'español:inglés' separadas por comas")
    println("(Ejemplo: hola:hello,casa:house,perro:dog)")
    print("> ")
    val entradaDiccionario = readln()

    val traductor = mutableMapOf<String, String>()

    val pares = entradaDiccionario.split(",")

    for (par in pares) {
        val partes = par.split(":")
        if (partes.size == 2) {
            val espanol = partes[0].trim()
            val ingles = partes[1].trim()
            traductor[espanol] = ingles
        }
    }

    println("\nIntroduce una frase en español para traducir:")
    print("> ")
    val fraseEspanol = readln()

    val palabrasFrase = fraseEspanol.split(" ")
    val fraseTraducida = mutableListOf<String>()

    for (palabra in palabrasFrase) {

        val traduccion = traductor.getOrDefault(palabra, palabra)
        fraseTraducida.add(traduccion)
    }

    println("\nFrase traducida:")
    println(fraseTraducida.joinToString(" "))
}