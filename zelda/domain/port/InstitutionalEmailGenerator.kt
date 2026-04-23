package org.iesra.procesaalumnos.domain.port
import org.iesra.procesaalumnos.domain.model.Student

/**
 * Ejemplo de interfaz para la generación del correo institucional.
 */
interface InstitutionalEmailGenerator {
    fun generar(alumno: Student): String
}
