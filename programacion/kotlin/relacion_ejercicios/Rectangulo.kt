package org.example

class Rectangulo(color: String, val base: Double, val altura: Double) : Figura(color) {

    override fun area(): Double {
        return base * altura
    }

    override fun perimetro(): Double {
        return 2 * (base + altura)
    }
}
