fun main() {
    val baseDatos = mutableMapOf<String, MutableMap<String, Any>>()
    var terminar = false

    while (!terminar) {
        println("\n--- GESTIÓN DE CLIENTES ---")
        println("(1) Añadir cliente")
        println("(2) Eliminar cliente")
        println("(3) Mostrar cliente")
        println("(4) Listar todos los clientes")
        println("(5) Listar clientes preferentes")
        println("(6) Terminar")
        print("Elige una opción: ")

        val opcion = readln()

        when (opcion) {
            "1" -> {
                print("NIF: ")
                val nif = readln()
                print("Nombre: ")
                val nombre = readln()
                print("Dirección: ")
                val direccion = readln()
                print("Teléfono: ")
                val telefono = readln()
                print("Correo: ")
                val correo = readln()
                print("¿Es cliente preferente? (si/no): ")
                val preferente = readln().lowercase() == "si"

                val datosCliente = mutableMapOf<String, Any>(
                    "nombre" to nombre,
                    "direccion" to direccion,
                    "telefono" to telefono,
                    "correo" to correo,
                    "preferente" to preferente
                )
                baseDatos[nif] = datosCliente
                println("Cliente añadido correctamente.")
            }

            "2" -> {
                print("Introduce el NIF del cliente a eliminar: ")
                val nif = readln()
                if (baseDatos.containsKey(nif)) {
                    baseDatos.remove(nif)
                    println("Cliente eliminado.")
                } else {
                    println("No existe ningún cliente con ese NIF.")
                }
            }

            "3" -> {
                print("Introduce el NIF del cliente: ")
                val nif = readln()
                val cliente = baseDatos[nif]
                if (cliente != null) {
                    println("\nDatos del cliente $nif:")
                    for ((campo, valor) in cliente) {
                        println("${campo.replaceFirstChar { it.uppercase() }}: $valor")
                    }
                } else {
                    println("Cliente no encontrado.")
                }
            }

            "4" -> {
                println("\nLISTA DE TODOS LOS CLIENTES:")
                for ((nif, datos) in baseDatos) {
                    println("NIF: $nif - Nombre: ${datos["nombre"]}")
                }
            }

            "5" -> {
                println("\nLISTA DE CLIENTES PREFERENTES:")
                for ((nif, datos) in baseDatos) {
                    if (datos["preferente"] == true) {
                        println("NIF: $nif - Nombre: ${datos["nombre"]}")
                    }
                }
            }

            "6" -> {
                println("Cerrando el programa...")
                terminar = true
            }

            else -> println("Opción no válida, intenta de nuevo.")
        }
    }
}