package org.example

open class Persona9(
    val nombre: String,
    val edad: Int,
    val id: String
) {

    open fun mostrarRol() {
        println("Rol: Persona")
    }
}
