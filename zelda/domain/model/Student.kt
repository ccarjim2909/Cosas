package org.iesra.procesaalumnos.domain.model


data class Student(
    val nombre: String,
    val apellido: String,
    val emailGenerado: String,
    val emailOriginal: String,
    val grupoSolicitado: String,
    val grupoAsignado: String
)
