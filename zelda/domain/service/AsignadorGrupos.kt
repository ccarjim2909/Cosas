package org.iesra.procesaalumnos.domain.service
import org.iesra.procesaalumnos.domain.model.Student
import org.iesra.procesaalumnos.domain.port.GroupAssigner


class AsignadorGrupos : GroupAssigner {

    private val contadoresGrupos = mutableMapOf<String, Int>()
    private val incidencias = mutableListOf<String>()

    override fun asignar(alumno: Student): String {
        val grupoSolicitado = alumno.grupoSolicitado.trim()


        val grupoTienePlazas = (contadoresGrupos[grupoSolicitado] ?: 0) < 5

        if (grupoSolicitado.isNotEmpty() && grupoTienePlazas) {
            val contadorActual = contadoresGrupos[grupoSolicitado] ?: 0
            contadoresGrupos[grupoSolicitado] = contadorActual + 1
            return grupoSolicitado
        }


        val grupoEstaLleno = (contadoresGrupos[grupoSolicitado] ?: 0) >= 5

        if (grupoSolicitado.isNotEmpty() && grupoEstaLleno) {
            val mensaje = "${alumno.nombre} ${alumno.apellido}: grupo $grupoSolicitado solicitado pero lleno, asignado a otro"
            incidencias.add(mensaje)
        }


        if (grupoSolicitado.isEmpty()) {
            val mensaje = "${alumno.nombre} ${alumno.apellido}: grupo en blanco, asignado uno cualquiera"
            incidencias.add(mensaje)
        }


        val abecedario = listOf('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')

        for (letra in abecedario) {
            val nombreGrupo = letra.toString()
            val numeroAlumnos = contadoresGrupos[nombreGrupo] ?: 0

            if (numeroAlumnos < 5) {
                contadoresGrupos[nombreGrupo] = numeroAlumnos + 1
                return nombreGrupo
            }
        }


        for (letra in abecedario) {
            val nombreGrupo = letra.toString()
            if (!contadoresGrupos.containsKey(nombreGrupo)) {
                contadoresGrupos[nombreGrupo] = 1
                return nombreGrupo
            }
        }
        throw IllegalStateException("No hay mas grupos disponibles")
    }

    override fun obtenerResumenGrupos(): Map<String, Int> {
        val resultado = mutableMapOf<String, Int>()
        for (entrada in contadoresGrupos) {
            resultado[entrada.key] = entrada.value
        }
        return resultado
    }

    override fun obtenerIncidencias(): List<String> {
        val resultado = mutableListOf<String>()
        for (incidencia in incidencias) {
            resultado.add(incidencia)
        }
        return resultado
    }
}
