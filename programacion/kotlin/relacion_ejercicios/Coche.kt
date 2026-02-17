package org.example

class Coche : EncendidoApagado, Vehiculo {

    override var motorEncendido: Boolean = false
    override var kmHora: Int = 0

    override fun encender() {
        motorEncendido = true
        println("Coche encendido")
    }

    override fun apagar() {
        motorEncendido = false
        kmHora = 0
        println("Coche apagado")
    }

    override fun acelerar(cantidad: Int) {
        if (motorEncendido) {
            kmHora += cantidad
            println("Acelerando. Velocidad actual: $kmHora km/h")
        } else {
            println("No se puede acelerar: el motor está apagado")
        }
    }

    override fun frenar(cantidad: Int) {
        if (motorEncendido) {
            kmHora -= cantidad
            if (kmHora < 0) kmHora = 0
            println("Frenando. Velocidad actual: $kmHora km/h")
        } else {
            println("No se puede frenar: el motor esta apagado")
        }
    }
}
