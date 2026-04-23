package org.iesra.procesaalumnos.domain.port
import org.iesra.procesaalumnos.domain.model.Student
import java.nio.file.Path

/**
 * Ejemplo de interfaz para escribir los artefactos de salida.
 */
interface OutputWriter {
    fun escribirCorreos(alumnos: List<Student>, directorioSalida: Path)

    fun escribirGrupos(alumnos: List<Student>, directorioSalida: Path)
}
