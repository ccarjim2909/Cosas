package org.iesra.procesaalumnos.domain.service
import org.iesra.procesaalumnos.domain.model.Student
import org.iesra.procesaalumnos.domain.port.OutputWriter
import java.nio.file.Files
import java.nio.file.Path


class EscritorSalidas(private val grupo: String) : OutputWriter {

    override fun escribirCorreos(alumnos: List<Student>, directorioSalida: Path) {
        val nombreFichero = "$grupo-correos.csv"

        val fichero = directorioSalida.resolve(nombreFichero)

        val cabecera = "nombre|apellidos|email1|email2"

        val lineasDatos = mutableListOf<String>()
        for (alumno in alumnos) {
            val linea = "${alumno.nombre}|${alumno.apellido}|${alumno.emailOriginal}|${alumno.emailGenerado}"
            lineasDatos.add(linea)
        }

        val lineas = mutableListOf<String>()
        lineas.add(cabecera)
        lineas.addAll(lineasDatos)

        Files.write(fichero, lineas)

        println("Fichero de correos generado: ${fichero.fileName}")
    }

    override fun escribirGrupos(alumnos: List<Student>, directorioSalida: Path) {
        val nombreFichero = "$grupo-grupos.txt"

        val fichero = directorioSalida.resolve(nombreFichero)

        val alumnosPorGrupo = mutableMapOf<String, MutableList<Student>>()

        for (alumno in alumnos) {
            val grupoAsignado = alumno.grupoAsignado

            if (!alumnosPorGrupo.containsKey(grupoAsignado)) {
                alumnosPorGrupo[grupoAsignado] = mutableListOf()
            }

            alumnosPorGrupo[grupoAsignado]?.add(alumno)
        }

        val gruposOrdenados = alumnosPorGrupo.toSortedMap()

        val lineasContenido = mutableListOf<String>()

        var esPrimerGrupo = true
        for ((nombreGrupo, alumnosDelGrupo) in gruposOrdenados) {
            if (!esPrimerGrupo) {
                lineasContenido.add("")
                lineasContenido.add("")
            }
            esPrimerGrupo = false

            lineasContenido.add("[Grupo-$nombreGrupo]")

            for (alumno in alumnosDelGrupo) {
                lineasContenido.add("- ${alumno.nombre} ${alumno.apellido}")
            }
        }

        val contenidoFinal = lineasContenido.joinToString("\n")

        Files.writeString(fichero, contenidoFinal)
        
        println("Fichero de grupos generado: ${fichero.fileName}")
    }
}
