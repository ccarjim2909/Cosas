fun main() {
    println("Introduce la cantidad de dinero depositada: ")
    val depositoInicial = readln().toDouble()

    val interes = 1.04

    val balanceAño1 = depositoInicial * interes
    val balanceAño2 = balanceAño1 * interes
    val balanceAño3 = balanceAño2 * interes

    println("Balance tras el primer año: ${"%.2f".format(balanceAño1)}€")
    println("Balance tras el segundo año: ${"%.2f".format(balanceAño2)}€")
    println("Balance tras el tercer año: ${"%.2f".format(balanceAño3)}€")
}