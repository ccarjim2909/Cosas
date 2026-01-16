fun main() {
    println("Introduce los productos de la cesta (separados por comas): ")
    val entrada = readln()

    val productos = entrada.split(",")

    println("\n--- Tu Cesta de la Compra ---")

    for (objeto in productos) {
        println(objeto)
    }
}