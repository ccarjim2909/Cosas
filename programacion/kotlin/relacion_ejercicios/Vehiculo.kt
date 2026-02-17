package org.example

interface Vehiculo {
    var motorEncendido: Boolean
    var kmHora: Int

    fun acelerar(cantidad: Int)
    fun frenar(cantidad: Int)
}
