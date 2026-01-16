fun main() {
    println("Introduce tu fecha de nacimiento (dd/mm/aaaa): ")
    val fechaInput = readln()

    val partes = fechaInput.split("/")

    if (partes.size == 3) {
        val dia = partes[0]
        val mes = partes[1]
        val anio = partes[2]

        println("Día: $dia")
        println("Mes: $mes")
        println("Año: $anio")
    } else {
        println("El formato de fecha no es válido. Recuerda usar el formato dd/mm/aaaa.")
    }
}