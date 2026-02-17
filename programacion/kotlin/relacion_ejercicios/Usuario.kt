package org.example

sealed class Usuario {
    abstract val id: String
    abstract val nombre: String

    data class Estudiante(
        override val id: String,
        override val nombre: String,
        val carrera: String
    ) : Usuario()

    data class Profesor(
        override val id: String,
        override val nombre: String,
        val departamento: String
    ) : Usuario()

    data class Visitante(
        override val id: String,
        override val nombre: String
    ) : Usuario()

}

fun puedePrestarLibro(usuario: Usuario, libro: Libro): String {
    return when(usuario) {
        is Usuario.Estudiante -> "${usuario.nombre} (Estudiante) puede tomar prestado '${libro.titulo}'."
        is Usuario.Profesor -> "${usuario.nombre} (Profesor) puede tomar prestado '${libro.titulo}' por mas tiempo."
        is Usuario.Visitante -> "${usuario.nombre} (Visitante) NO puede tomar prestado '${libro.titulo}'."

    }
}