package org.iesra.procesaalumnos.domain.service
import org.iesra.procesaalumnos.domain.model.Student
import org.iesra.procesaalumnos.domain.port.InstitutionalEmailGenerator


class GeneradorCorreoInstitucional : InstitutionalEmailGenerator {

    override fun generar(alumno: Student): String {
        val nombre = alumno.nombre
        val primeraLetra = nombre.firstOrNull()
        val primeraLetraMinuscula = primeraLetra?.lowercase() ?: ""

        val apellidos = alumno.apellido
        val apellidosSeparados = apellidos.split(" ")

        val apellidosValidos = mutableListOf<String>()
        for (apellido in apellidosSeparados) {
            if (apellido.isNotBlank()) {
                apellidosValidos.add(apellido)
            }
        }

        val segundoApellido: String
        if (apellidosValidos.size > 1) {
            segundoApellido = apellidosValidos[1]
        } else if (apellidosValidos.size == 1) {
            segundoApellido = apellidosValidos[0]
        } else {
            segundoApellido = ""
        }

        val segundoApellidoMinuscula = segundoApellido.lowercase()

        val segundaLetra: String
        if (segundoApellido.length > 1) {
            val letraChar = segundoApellido[1]
            segundaLetra = letraChar.lowercase()
        } else if (segundoApellido.length == 1) {
            val letraChar = segundoApellido[0]
            segundaLetra = letraChar.lowercase()
        } else {
            segundaLetra = ""
        }

        val email = "$primeraLetraMinuscula$segundoApellidoMinuscula$segundaLetra@iesrafaelalberti.es"

        return email
    }
}
