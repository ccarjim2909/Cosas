package org.example

open class Persona10(
    val nombre: String,
    var edad: Int
) {

    fun celebrarCumple(): String {
        edad++
        return "Feliz cumpleaños $nombre! Ahora tienes $edad años."
    }

    override fun toString(): String {
        return "Nombre: $nombre, Edad: $edad"
    }
}
