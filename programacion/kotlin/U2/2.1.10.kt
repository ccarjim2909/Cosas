fun main() {
    val base = "Tomate, Mozzarella"

    println("Bienvenido a la pizzería Bella Napoli")
    println("¿Deseas una pizza vegetariana? (S/N): ")
    val respuestaVeg = readln().uppercase()

    val tipoPizza: String
    val ingredienteElegido: String

    if (respuestaVeg == "S") {
        tipoPizza = "Vegetariana"
        println("\nIngredientes disponibles: (1) Pimiento, (2) Tofu")
        println("Elige uno (escribe el nombre): ")
        ingredienteElegido = readln()
    } else {
        tipoPizza = "No vegetariana"
        println("\nIngredientes disponibles: (1) Peperoni, (2) Jamón, (3) Salmón")
        println("Elige uno (escribe el nombre): ")
        ingredienteElegido = readln()
    }

    println("\n--- Resumen de tu pedido ---")
    println("Tipo de pizza: $tipoPizza")
    println("Ingredientes: $base, $ingredienteElegido")
}