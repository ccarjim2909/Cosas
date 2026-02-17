package org.example

class Departamento(val nombre: String) {

    private val empleados = mutableListOf<Empleado>()

    fun agregarEmpleado(empleado: Empleado) {
        empleados.add(empleado)
    }

    fun calculaSalarioTotal(): Double {
        var total = 0.0
        for (empleado in empleados) {
            total += empleado.calculaSalario()
        }
        return total
    }

    fun mostrarEmpleados() {
        for (empleado in empleados) {
            val idFormateado = String.format("%04d", empleado.id)
            val salarioFormateado = String.format("%.2f", empleado.calculaSalario())

            println("${empleado.nombre} con ID-$idFormateado tiene un salario de $salarioFormateado al mes.")
        }
    }
}
