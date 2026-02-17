package org.example

class EmpleadoFijo
    (nombre: String, id: Int, val salarioFijo: Double, val numPagas: Int
        ) : Empleado(nombre, id) {

    override fun calculaSalario(): Double {
        val salarioMensual = (salarioFijo * numPagas) / 12
        return salarioMensual
    }
}