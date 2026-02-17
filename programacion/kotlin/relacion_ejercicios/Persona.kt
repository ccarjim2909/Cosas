package org.example

open class Persona(
    nombre: String,
    edad: Int = 0
) {

    val nombre: String
    var edad: Int = edad
        private set

    init {
        require(nombre.isNotBlank()) { "El nombre no puede estar vacío" }
        require(edad >= 0) { "La edad no puede ser negativa" }
        this.nombre = nombre
    }

    fun cumple() {
        edad++
    }

    open fun actividad() {
        println("$nombre está realizando una actividad.")
    }

    override fun toString(): String {
        return "Persona (nombre = $nombre, edad = $edad)"
    }
}
