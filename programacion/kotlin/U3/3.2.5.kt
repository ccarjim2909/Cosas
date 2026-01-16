fun main() {
    val curso = mapOf(
        "Matemáticas" to 6,
        "Física" to 4,
        "Química" to 5
    )

    var totalCreditos = 0

    for ((asignatura, creditos) in curso) {
        println("$asignatura tiene $creditos créditos")

        totalCreditos += creditos
    }

    println("\nEl número total de créditos del curso es: $totalCreditos")
}