fun main() {
    val bonificacionBase = 2400

    println("Introduce tu puntuación (0.0, 0.4, 0.6 o más): ")
    val puntuacion = readln().toDouble()

    val nivel = when {
        puntuacion == 0.0 -> "Inaceptable"
        puntuacion == 0.4 -> "Aceptable"
        puntuacion >= 0.6 -> "Meritorio"
        else -> "Invalido"
    }

    if (nivel == "Invalido") {
        println("Esa puntuación no es válida según los criterios de la empresa.")
    } else {
        val dineroRecibido = bonificacionBase * puntuacion

        println("Tu nivel de rendimiento es: $nivel")
        println("Recibirás una bonificación de: ${"%.2f".format(dineroRecibido)}€")
    }
}