import kotlin.math.pow
import kotlin.math.sqrt

fun main() {
    print("Introduce una muestra de números separados por comas: ")
    val entrada = readln()


    val numeros = entrada.split(",").map { it.trim().toDouble() }

    val n = numeros.size

    val media = numeros.sum() / n

    var sumaCuadrados = 0.0
    for (numero in numeros) {
        sumaCuadrados += (numero - media).pow(2)
    }

    val desviacionTipica = sqrt(sumaCuadrados / n)

    println("\nEstadísticas:")
    println("Muestra: $numeros")
    println("Media: %.2f".format(media))
    println("Desviación típica: %.2f".format(desviacionTipica))
}