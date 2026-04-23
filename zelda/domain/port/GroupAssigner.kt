package org.iesra.procesaalumnos.domain.port
import org.iesra.procesaalumnos.domain.model.Student

/**
 * Ejemplo de interfaz para asignar grupos.
 *
 * Didácticamente interesa porque permite explicar polimorfismo:
 * podría haber distintas estrategias de asignación y todas implementar
 * la misma interfaz.
 */
interface GroupAssigner {
    fun asignar(alumno: Student): String

    fun obtenerResumenGrupos(): Map<String, Int>

    fun obtenerIncidencias(): List<String>
}
