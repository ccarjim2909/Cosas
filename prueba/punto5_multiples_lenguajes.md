# Punto 2.5: Generación de ejecutables a partir de código fuente en distintos lenguajes en un mismo IDE

## IDEs utilizados
- *IDE 1:* Visual Studio Code (versión más reciente)  
- *IDE 2:* IntelliJ IDEA (versión más reciente)

## Descripción de la tarea
Escribir un programa que cuente de 10 a 0 y luego imprima "¡Despegue!" en dos lenguajes diferentes (Python y Java) usando un mismo IDE y generar los ejecutables.

## Respuestas a preguntas evaluativas
### Pregunta 1: ¿Cuál fue el proceso para ejecutar el mismo programa en diferentes lenguajes dentro del mismo IDE?
- **Visual Studio Code:** instalar extensiones de cada lenguaje, abrir archivos y ejecutar. Detecta automáticamente el lenguaje y usa el intérprete o compilador adecuado.  
- **IntelliJ IDEA:** crear módulos por lenguaje dentro del proyecto, compilar o interpretar según configuración del módulo.

### Pregunta 2: ¿Qué diferencias encontraste en la generación del ejecutable entre los dos lenguajes?
- **Python:** se ejecuta directamente (interpretado).  
- **Java:** se compila primero a bytecode `.class` (compilado), requiere más pasos pero ofrece mejor rendimiento.

## Evidencias
![Captura 1](img/11.png)

## Observaciones
Los lenguajes interpretados permiten iterar más rápido, mientras que los compilados ofrecen mejor rendimiento pero requieren pasos adicionales.