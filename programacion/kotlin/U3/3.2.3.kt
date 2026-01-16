fun main() {
    val preciosFrutas = mapOf(
        "Plátano" to 1.35,
        "Manzana" to 0.80,
        "Pera" to 0.85,
        "Naranja" to 0.70
    )

    println("¿Qué fruta quieres comprar? ")
    val fruta = readln().trim().replaceFirstChar { it.uppercase() } // Normalizamos la primera letra

    println("¿Cuántos kilos necesitas? ")
    val kilos = readln().toDouble()


    val precioUnitario = preciosFrutas[fruta]

    if (precioUnitario != null) {
        val total = precioUnitario * kilos
        println("El precio de $kilos kg de $fruta es: $total€")
    } else {
        println("Lo siento, la fruta '$fruta' no está disponible en nuestra tienda.")
    }
}