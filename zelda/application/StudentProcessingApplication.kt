package org.iesra.procesaalumnos.application
import org.iesra.procesaalumnos.cli.CliOptions
import org.iesra.procesaalumnos.domain.model.FileIssue
import org.iesra.procesaalumnos.domain.model.ProcessingSummary
import org.iesra.procesaalumnos.domain.model.Student
import org.iesra.procesaalumnos.domain.port.GroupAssigner
import org.iesra.procesaalumnos.domain.port.InstitutionalEmailGenerator
import org.iesra.procesaalumnos.domain.port.OutputWriter
import org.iesra.procesaalumnos.domain.port.StudentFileRepository
import org.iesra.procesaalumnos.domain.port.StudentParser
import org.iesra.procesaalumnos.domain.service.AsignadorGrupos
import org.iesra.procesaalumnos.domain.service.EscritorSalidas
import org.iesra.procesaalumnos.domain.service.GeneradorCorreoInstitucional
import org.iesra.procesaalumnos.domain.service.ParserAlumnos
import org.iesra.procesaalumnos.domain.service.RepositorioFicherosAlumnos
/**
 * Coordina el caso de uso principal del programa.
 *
 * En esta base didáctica se comporta como orquestador: recibe los datos de entrada
 * ya parseados y explica cómo se podría repartir el trabajo entre otros objetos.
 *
 * Importante: en la rama `main` todavía no depende de implementaciones reales ni de
 * interfaces con métodos, porque la intención aquí es enseñar la estructura antes
 * de construir la solución completa.
 */
class StudentProcessingApplication {

    /**
     * Ejecuta el flujo principal del programa.
     *
     * @param options opciones recibidas desde la línea de comandos.
     */
    fun run(options: CliOptions) {
        println("Grupo recibido: ${options.group}")
        println("Directorio de trabajo: ${options.path}")
        println()

        val repositorio: StudentFileRepository = RepositorioFicherosAlumnos()
        val parseador: StudentParser = ParserAlumnos()
        val generadorCorreo: InstitutionalEmailGenerator = GeneradorCorreoInstitucional()
        val asignadorGrupos: GroupAssigner = AsignadorGrupos()
        val escritorSalidas: OutputWriter = EscritorSalidas(options.group)


        println("Buscando ficheros de entrada...")

        val ficherosEntrada = repositorio.localizarFicherosEntrada(options.path)
        println("Ficheros encontrados: ${ficherosEntrada.size}")
        println()

        val alumnos = mutableListOf<Student>()
        val problemas = mutableListOf<FileIssue>()


        println("Procesando ficheros...")

        for (fichero in ficherosEntrada) {
            val resultadoParseo = parseador.parsear(fichero)
            val alumnoParseado = resultadoParseo.first  // Primer elemento del Pair
            val problemaDetectado = resultadoParseo.second  // Segundo elemento del Pair

            if (problemaDetectado != null) {
                problemas.add(problemaDetectado)
            } else if (alumnoParseado != null) {
                val correoInstitucional = generadorCorreo.generar(alumnoParseado)
                val grupoAsignado = asignadorGrupos.asignar(alumnoParseado)
                val alumnoCompleto = alumnoParseado.copy(
                    emailGenerado = correoInstitucional,
                    grupoAsignado = grupoAsignado
                )

                alumnos.add(alumnoCompleto)
            }

            repositorio.moverAProcesados(fichero)
        }

        println("Ficheros procesados: ${alumnos.size}")
        println()


        println("Generando ficheros de salida...")

        if (alumnos.isNotEmpty()) {
            escritorSalidas.escribirCorreos(alumnos, options.path)

            escritorSalidas.escribirGrupos(alumnos, options.path)
        }
        println()


        val resumen = ProcessingSummary(
            detectedFiles = ficherosEntrada.size,
            validStudents = alumnos.size,
            issues = problemas
        )

        mostrarResumen(resumen, asignadorGrupos, problemas)
    }



    private fun mostrarResumen(resumen: ProcessingSummary, asignador: GroupAssigner, problemas: List<FileIssue>) {
        println("RESUMEN DEL PROCESAMIENTO")
        println()

        println("Ficheros procesados: ${resumen.detectedFiles}")
        println("Ficheros con errores: ${problemas.size}")
        println("Correos creados correctamente: ${resumen.validStudents}")
        println()

        println("Resumen de grupos:")
        val resumenGrupos = asignador.obtenerResumenGrupos()
        val gruposOrdenados = resumenGrupos.toSortedMap()

        for ((nombreGrupo, numeroAlumnos) in gruposOrdenados) {
            println("- Grupo-$nombreGrupo: $numeroAlumnos alumnos")
        }
        println()

        if (problemas.isNotEmpty()) {
            println("Errores detectados:")
            for (problema in problemas) {
                println("- ${problema.fileName}: ${problema.message}")
            }
            println()
        }

        val incidencias = asignador.obtenerIncidencias()
        if (incidencias.isNotEmpty()) {
            println("Incidencias:")
            for (incidencia in incidencias) {
                println("- $incidencia")
            }
            println()
        }

    }
}
