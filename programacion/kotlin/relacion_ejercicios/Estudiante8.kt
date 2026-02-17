package org.example

class Estudiante8(
    nombre: String,
    edad: Int = 0,
    val carrera: String
) : Persona(nombre, edad) {

    override fun actividad() {
        println("$nombre está estudiando la carrera de $carrera.")
    }

    override fun toString(): String {
        return "${super.toString()}, carrera = $carrera"
    }
}
