fun main() {
    val persona = mutableMapOf<String, String>()

    var continuar = "si"

    while (continuar.lowercase() == "si") {

        print("¿Qué dato quieres introducir? (ej. Nombre, Edad, Sexo...): ")
        val clave = readln().trim()

        print("Introduce el valor para '$clave': ")
        val valor = readln().trim()

        persona[clave] = valor

        println("\nContenido actual del diccionario:")
        for ((k, v) in persona) {
            println("- $k: $v")
        }

        print("\n¿Quieres añadir más información? (si/no): ")
        continuar = readln()
    }

    println("\nProceso finalizado. Información completa de la persona:")
    println(persona)
}