package org.example

class EmpleadoPorHora
    (nombre: String, id: Int, val horasTrabajadas: Int, val tarifaPorHora: Double
            ) : Empleado(nombre, id) {

    override fun calculaSalario(): Double {
        val salarioMensual = horasTrabajadas * tarifaPorHora
        return salarioMensual
    }
}