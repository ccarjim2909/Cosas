# Punto 2.6: Generación de ejecutables con diferentes IDEs a partir del mismo código fuente

## IDEs utilizados
- *IDE 1:* PyCharm Professional
- *IDE 2:* Thonny

## Descripción de la tarea
Escribir un programa en Python que cuente de 10 a 0 y luego imprima "¡Despegue!" y ejecutarlo en los IDEs seleccionados.

## Respuestas a preguntas evaluativas
### Pregunta 1: ¿Qué diferencias encontraste al ejecutar el mismo código fuente en diferentes IDEs?
- **PyCharm:** gestión avanzada de carpetas, consola profesional, mensajes de error detallados.  
- **Thonny:** interfaz limpia, intuitiva y excelente para principiantes.

### Pregunta 2: ¿Cuál de los IDEs te pareció más cómodo o eficiente para ejecutar el código Python o el lenguaje que hayas elegido? ¿Por qué?
- **PyCharm:** más cómodo por su accesibilidad y herramientas integradas.  
- **Thonny:** excelente para aprender y crear scripts simples.

## Evidencias
![Captura 1](../capturas/12.png)  

![Captura 2](../capturas/13.png)

## Observaciones
PyCharm es ideal para proyectos complejos y profesionales, mientras que Thonny es excelente para aprendizaje y tareas sencillas.




class Empleado(
    val numEmpleado: String,
    val nombre: String
)

class Medico(
    numEmpleado: String
    nombre: String
    val especialidad: String
) : Empleado(numEmpleado, nombre) {
    fun solicitaAnalisis()
}

class Enfermero(
    numEmpleado: String,
    nombre: String
) : Empleado(numEmpleado, nombre) {
    fun realizaAnalisis()
}

class Analisis(
    val numReferencia: String
    val tipoAnalisis: String
    val fechaRealizacion: Date
    val resultados: String
)

class Paciente(
    val nHistoriaClinica: String
    val nombre: String
    val direccion: String
)
