fun main() {
    println("Nombre del producto: ")
    val nombre = readln()

    println("Precio unitario: ")
    val precio = readln().toDouble()

    println("Número de unidades: ")
    val unidades = readln().toInt()


    val costeTotal = precio * unidades

    val salida = "%s: %09.2f€ x %03d unidades = %011.2f€".format(nombre, precio, unidades, costeTotal)

    println(salida)
}