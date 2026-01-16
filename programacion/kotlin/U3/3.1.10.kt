fun main() {
    val precios = listOf(50, 75, 46, 22, 80, 65, 8)

    val menor = precios.minOrNull()
    val mayor = precios.maxOrNull()

    println("El precio menor es: $menor")
    println("El precio mayor es: $mayor")
}