package org.example

class Ordenador(
    nombre: String,
    precio: Double,
    val tipo: TipoOrdenador = TipoOrdenador.BASICO
) : Articulo(nombre, precio) {

    override fun promocionNavidad(porcentaje: Double) {
        if (precio > 500) {
            super.promocionNavidad(porcentaje)
        }
    }

    override fun toString(): String {
        return "${super.toString()} [$tipo]"
    }
}
