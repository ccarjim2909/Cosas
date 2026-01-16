fun main() {
    println("Introduce un número de teléfono (+34-XXXXXXXXX-XX): ")
    val telefonoCompleto = readln()

    val partes = telefonoCompleto.split("-")

    if (partes.size == 3) {
        val numeroSolo = partes[1]
        println("El número de teléfono es: $numeroSolo")
    } else {
        println("El formato introducido no es correcto.")
    }
}