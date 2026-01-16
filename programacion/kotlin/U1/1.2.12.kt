fun main() {
    println("Introduce tu peso (kg): ")
    val peso = readln().toDouble()

    println("Introduce tu estatura (metros): ")
    val estatura = readln().toDouble()

    val imc = peso / (estatura * estatura)

    val imcRedondeado = "%.2f".format(imc)
    
    println("Tu índice de masa corporal es $imcRedondeado")
}