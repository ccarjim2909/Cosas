package org.example

class Circulo(color: String, val radio: Double) : Figura(color) {

    override fun area(): Double {
        return Math.PI * radio * radio
    }

    override fun perimetro(): Double {
        return 2 * Math.PI * radio
    }
}