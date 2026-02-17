package org.example

abstract class Figura (val color: String){
    abstract fun area(): Double
    abstract fun perimetro(): Double

    fun mostrarInformacion() {
        println("Color: $color")
        println("Area: ${area()}")
        println("Perimetro: ${perimetro()}")
    }

}