package org.example

class Gerente10(
    nombre: String,
    edad: Int,
    salarioBase: Double,
    val bonus: Double,
    val exentoImpuestos: Boolean = false
) : Empleado10(
    nombre,
    edad,
    salarioBase,
    porcentajeImpuestos = 33.99
) {

    override fun calcularSalario(): Double {
        return if (exentoImpuestos) {
            salarioBase + bonus
        } else {
            (salarioBase * (1 - porcentajeImpuestos / 100)) + bonus
        }
    }

    fun administrar(): String {
        return "$nombre esta administrando la empresa."
    }

    override fun toString(): String {
        return "${super.toString()}, Bonus: ${"%.2f".format(bonus)}€, Gerente"
    }
}
