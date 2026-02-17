package org.example

class Triangulo(
    color: String,
    val lado1: Double,
    val lado2: Double,
    val lado3: Double
) : Figura(color) {

    override fun area(): Double {
        val s = perimetro() / 2
        return Math.sqrt(s * (s - lado1) * (s - lado2) * (s - lado3))
    }

    override fun perimetro(): Double {
        return lado1 + lado2 + lado3
    }
}
