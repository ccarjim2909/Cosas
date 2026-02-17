package org.example

class Motocicleta(
    marca: String,
    modelo: String,
    capacidadCombustible: Int,
    val cilindrada: Int
) : Vehiculo7(marca, modelo, capacidadCombustible) {

    override fun calcularAutonomia(): Int {
        return super.calcularAutonomia() - 40
    }

    override fun mostrarInformacion() {
        super.mostrarInformacion()
        println("Cilindrada: $cilindrada cc")
    }
}
