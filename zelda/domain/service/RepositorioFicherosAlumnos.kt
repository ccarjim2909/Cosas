package org.iesra.procesaalumnos.domain.service
import org.iesra.procesaalumnos.domain.model.StudentFile
import org.iesra.procesaalumnos.domain.port.StudentFileRepository
import java.nio.file.Files
import java.nio.file.Path
import kotlin.io.path.extension
import kotlin.io.path.moveTo


class RepositorioFicherosAlumnos : StudentFileRepository {

    override fun localizarFicherosEntrada(directorio: Path): List<StudentFile> {
        return try {
            val ficherosList = Files.list(directorio)

            val ficherosTexto = ficherosList.filter { fichero ->
                fichero.extension == "txt"
            }

            val studentFiles = mutableListOf<StudentFile>()
            for (fichero in ficherosTexto) {
                studentFiles.add(StudentFile(fichero))
            }

            studentFiles
        } catch (e: Exception) {
            emptyList()
        }
    }

    override fun moverAProcesados(fichero: StudentFile) {
        try {
            val directorioPadre = fichero.path.parent

            val directorioProcesados = directorioPadre.resolve("procesados")

            Files.createDirectories(directorioProcesados)

            val nombreFichero = fichero.path.fileName

            val rutaDestino = directorioProcesados.resolve(nombreFichero)

            fichero.path.moveTo(rutaDestino, overwrite = true)
        } catch (e: Exception) {

        }
    }
}
