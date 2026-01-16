fun main() {
    println("Introduce el precio del producto con dos decimales (ej. 15.95): ")
    val precioInput = readln()

    val precioNormalizado = precioInput.replace(",", ".")

    val partes = precioNormalizado.split(".")

    if (partes.size == 2) {
        val euros = partes[0]
        val centimos = partes[1]
        println("El precio tiene $euros euros y $centimos céntimos.")
    } else {
        println("El precio tiene ${partes[0]} euros y 00 céntimos.")
    }
}