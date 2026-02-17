package org.example

open class Empleado10(
    nombre: String,
    edad: Int,
    salarioBase: Double,
    open val porcentajeImpuestos: Double = 10.0
) : Persona10(nombre, edad) {

    var salarioBase: Double = salarioBase
        protected set


    constructor(
        nombre: String,
        edad: Int,
        salarioBase: Int,
        porcentajeImpuestos: Int = 10
    ) : this(nombre, edad, salarioBase.toDouble(), porcentajeImpuestos.toDouble())

    open fun calcularSalario(): Double {
        return salarioBase * (1 - porcentajeImpuestos / 100)
    }

    open fun trabajar(): String {
        return "$nombre esta trabajando en la empresa."
    }

    override fun toString(): String {
        return "${super.toString()}, Salario: ${"%.2f".format(calcularSalario())}€"
    }
}
