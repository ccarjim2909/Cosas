fun main() {
    println("Introduce el importe final del artículo (con IVA): ")

    val precioTotal = readln().toDouble()

    val precioSinIva = precioTotal / 1.10

    val ivaPagado = precioTotal - precioSinIva


    println("Importe sin IVA: ${"%.2f".format(precioSinIva)}€")
    println("IVA pagado (10%): ${"%.2f".format(ivaPagado)}€")
}