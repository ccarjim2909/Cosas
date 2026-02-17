package org.example

class Automovil(
    marca: String,
    modelo: String,
    capacidadCombustible: Int,
    val tipo: String
) : Vehiculo7(marca, modelo, capacidadCombustible) {

    override fun calcularAutonomia(): Int {
        return super.calcularAutonomia() + 100
    }

    override fun mostrarInformacion() {
        super.mostrarInformacion()
        println("Tipo: $tipo")
    }
}
