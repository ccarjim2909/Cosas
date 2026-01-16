fun main() {
    val primaria = mutableSetOf<String>()
    println("Introduce los nombres de primaria (escribe 'x' para terminar):")
    print("> ")
    var nombre = readln().trim().lowercase()

    while (nombre != "x") {
        primaria.add(nombre)
        print("> ")
        nombre = readln().trim().lowercase()
    }

    val secundaria = mutableSetOf<String>()
    println("\nIntroduce los nombres de secundaria (escribe 'x' para terminar):")
    print("> ")
    nombre = readln().trim().lowercase()

    while (nombre != "x") {
        secundaria.add(nombre)
        print("> ")
        nombre = readln().trim().lowercase()
    }


    val todosLosAlumnos = primaria.union(secundaria)
    println("\n1. Todos los nombres (primaria + secundaria): $todosLosAlumnos")

    val nombresRepetidos = primaria.intersect(secundaria)
    println("2. Nombres que se repiten en ambos niveles: $nombresRepetidos")

    val soloPrimaria = primaria.subtract(secundaria)
    println("3. Nombres de primaria que no están en secundaria: $soloPrimaria")

    val primariaIncluida = secundaria.containsAll(primaria)
    if (primariaIncluida) {
        println("4. Sí, todos los nombres de primaria están incluidos en secundaria.")
    } else {
        println("4. No todos los nombres de primaria están incluidos en secundaria.")
    }
}