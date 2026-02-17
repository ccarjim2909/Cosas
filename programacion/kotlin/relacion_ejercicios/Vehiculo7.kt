package org.example

open class Vehiculo7(
    val marca: String,
    val modelo: String,
    val capacidadCombustible: Int
) {

    open fun calcularAutonomia(): Int {
        return capacidadCombustible * 10
    }

    open fun mostrarInformacion() {
        println("Marca: $marca")
        println("Modelo: $modelo")
        println("Capacidad de combustible: $capacidadCombustible L")
        println("Autonomía: ${calcularAutonomia()} km")
    }
}
