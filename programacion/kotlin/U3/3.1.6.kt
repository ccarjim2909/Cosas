fun main() {
    val asignaturas = mutableListOf("Matemáticas", "Física", "Química", "Historia", "Lengua")

    for (i in asignaturas.size - 1 downTo 0) {
        print("¿Qué nota has sacado en ${asignaturas[i]}? ")
        val nota = readln().toDouble()

        if (nota >= 5.0) {
            asignaturas.removeAt(i)
        }
    }

    println("\nTienes que repetir las siguientes asignaturas:")
    println(asignaturas)
}