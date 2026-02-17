package org.example

class Profesor9(
    nombre: String,
    edad: Int,
    id: String,
    val departamento: String,
    val aniosExperiencia: Int
) : Persona9(nombre, edad, id) {

    override fun mostrarRol() {
        println("Rol: Profesor")
    }

    fun mostrarExperiencia() {
        println("Años de experiencia: $aniosExperiencia")
    }
}
