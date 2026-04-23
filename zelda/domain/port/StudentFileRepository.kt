package org.iesra.procesaalumnos.domain.port
import org.iesra.procesaalumnos.domain.model.StudentFile
import java.nio.file.Path

/**
 * Ejemplo de interfaz para acceso a ficheros.
 *
 * Aquí se puede explicar el patrón repositorio de forma básica:
 * el resto del programa no necesita saber cómo se leen o mueven los ficheros.
 */
interface StudentFileRepository {
    fun localizarFicherosEntrada(directorio: Path): List<StudentFile>

    fun moverAProcesados(fichero: StudentFile)
}