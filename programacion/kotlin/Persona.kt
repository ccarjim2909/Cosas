class Persona(val nombre: String) {
    fun saludar(): String {
        return "Hola, mi nombre es $nombre"
    }
}

fun main() {
    val cris = Persona("Cris")
    println(cris.saludar())


//  While:
    do {
        val y = cris.saludar()
    } while (y != "Hola")


    var x = 15
//  When es como un if/elif...else
    when (x) {
        parseInt(x) -> print("x is a nombre")
        parseFloat(x) -> print("x is a nombre")
        else -> print("x is neither a nombre nor a nombre")
    }

}