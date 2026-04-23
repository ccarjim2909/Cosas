package org.iesra.procesaalumnos.domain.service
import org.iesra.procesaalumnos.domain.model.FileIssue
import org.iesra.procesaalumnos.domain.model.Student
import org.iesra.procesaalumnos.domain.model.StudentFile
import org.iesra.procesaalumnos.domain.port.StudentParser
import java.nio.file.Files


class ParserAlumnos : StudentParser {

    override fun parsear(fichero: StudentFile): Pair<Student?, FileIssue?> {
        try {
            val lineas = Files.readAllLines(fichero.path)

            val nombre = extraerValor(lineas, "Nombre:")
            val apellidos = extraerValor(lineas, "Apellidos:")
            val correo = extraerValor(lineas, "email:")
            val grupo = extraerValor(lineas, "Grupo =")
            val grupoFinal = grupo ?: ""

            if (nombre.isNullOrBlank()) {
                val problema = FileIssue(fichero.path.fileName.toString(), "Campo 'Nombre' vacío")
                return null to problema
            }

            if (apellidos.isNullOrBlank()) {
                val problema = FileIssue(fichero.path.fileName.toString(), "Campo 'Apellidos' vacío")
                return null to problema
            }

            if (correo.isNullOrBlank()) {
                val problema = FileIssue(fichero.path.fileName.toString(), "Campo 'email' vacío")
                return null to problema
            }

            if (!correo.contains("@")) {
                val problema = FileIssue(fichero.path.fileName.toString(), "Email mal formado: $correo")
                return null to problema
            }

            val alumno = Student(
                nombre = nombre,
                apellido = apellidos,
                emailOriginal = correo,
                emailGenerado = "",
                grupoSolicitado = grupoFinal,
                grupoAsignado = ""
            )

            return alumno to null
        } catch (e: Exception) {
            val problema = FileIssue(fichero.path.fileName.toString(), "Error al leer fichero: ${e.message}")
            return null to problema
        }
    }

    private fun extraerValor(lineas: List<String>, prefijo: String): String? {
        for (linea in lineas) {
            if (linea.startsWith(prefijo)) {
                val valor = linea.substringAfter(prefijo)

                val valorLimpio = valor.trim()

                return if (valorLimpio.isNotEmpty()) valorLimpio else null
            }
        }
        return null
    }
}
