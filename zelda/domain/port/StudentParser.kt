package org.iesra.procesaalumnos.domain.port
import org.iesra.procesaalumnos.domain.model.FileIssue
import org.iesra.procesaalumnos.domain.model.Student
import org.iesra.procesaalumnos.domain.model.StudentFile

/**
 * Ejemplo de interfaz para transformar un fichero en un objeto del dominio.
 */
interface StudentParser {
    fun parsear(fichero: StudentFile): Pair<Student?, FileIssue?>
}
