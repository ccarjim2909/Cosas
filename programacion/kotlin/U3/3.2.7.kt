fun main() {
    val cesta = mutableMapOf<String, Double>()
    var continuar = true

    while (continuar) {
        println("Introduce el nombre del artículo: ")
        val articulo = readln().trim()

        println("Introduce el precio de '$articulo': ")
        val precio = readln().toDouble()

        cesta[articulo] = precio

        println("¿Deseas añadir otro artículo? (si/no): ")
        val respuesta = readln().lowercase()

        if (respuesta != "si") {
            continuar = false
        }
    }

    println("\n--- LISTA DE LA COMPRA ---")
    var costeTotal = 0.0

    for ((item, precio) in cesta) {
        println("${item.padEnd(20)} $precio€")
        costeTotal += precio
    }


    println("-".repeat(30))
    println("${"Total".padEnd(20)} $costeTotal€")
}