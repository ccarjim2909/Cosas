fun main() {
    var opcion: Int

    do {
        println("\n--- MENÚ DE OPCIONES ---")
        println("1- Comenzar programa")
        println("2- Imprimir texto")
        println("3- Finalizar programa")
        print("Selecciona una opción (1-3): ")


        val entrada = readln().toIntOrNull()

        if (entrada == null) {
            println("Error: Por favor, introduce un número válido.")
            opcion = 0
        } else {
            opcion = entrada

            when (opcion) {
                1 -> println("Iniciando el programa.")
                2 -> println("Imprimiendo texto.")
                3 -> println("Saliendo del sistema.")
                else -> println("Error: Opción incorrecta. Por favor, elige 1, 2 o 3.")
            }
        }

    } while (opcion != 3) 
}