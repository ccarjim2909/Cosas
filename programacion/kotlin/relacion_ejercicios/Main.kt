package org.example


fun main() {


    println("\n----Ejercicio 1----\n")

    val circulo = Circulo("Rojo", 5.0)
    val rectangulo = Rectangulo("Verde", 4.0, 6.0)
    val triangulo = Triangulo("Azul", 3.0, 4.0, 5.0)

    println("Circulo")
    circulo.mostrarInformacion()

    println("\nRectangulo")
    rectangulo.mostrarInformacion()

    println("\nTriangulo")
    triangulo.mostrarInformacion()





    println("\n----Ejercicio 2----\n")


    val departamento = Departamento("Informática")

    val empleado1 = EmpleadoPorHora("Ana", 1, 160, 15.50)

    val empleado2 = EmpleadoFijo("Luis", 23, 24000.0, 12)

    val empleado3 = EmpleadoPorHora("Carlos", 7, 120, 18.0)

    departamento.agregarEmpleado(empleado1)
    departamento.agregarEmpleado(empleado2)
    departamento.agregarEmpleado(empleado3)

    departamento.mostrarEmpleados()

    println("Salario total: ${String.format("%.2f", departamento.calculaSalarioTotal())}")






    println("\n----Ejercicio 3----\n")


    val telefono = Telefono()
    telefono.encender()
    telefono.reiniciar()
    telefono.apagar()

    println("")

    val lavadora = Lavadora()
    lavadora.encender()
    lavadora.reiniciar()
    lavadora.apagar()

    println("")

    val coche = Coche()
    coche.acelerar(50)
    coche.encender()
    coche.acelerar(50)
    coche.frenar(20)
    coche.frenar(50)
    coche.apagar()



    println("\n----Ejercicio 4----\n")

    val notificaciones: List<Notificable> = listOf(
        CorreoElectronico("usuario@hotmail.com", "Bienvenido"),
        MensajeTexto("674874834"),
        NotificacionPush("Copia completada")
    )

    for (notificacion in notificaciones) {
        notificacion.enviarNotificacion()
    }



    println("\n----Ejercicio 5----\n")

    val libro1 = Libro("Mein kampf", "Adolf Hitler", 1949)
    val libro2 = Libro("Clean Code", "Robert C. Martin", 2008)

    val estudiante = Usuario.Estudiante("E001", "Ana", "Programador")
    val profesor = Usuario.Profesor("P001", "Luis", "Matematicas")
    val visitante = Usuario.Visitante("V001", "Carlos")

    val usuarios = listOf<Usuario>(estudiante, profesor, visitante)
    val libros = listOf(libro1, libro2)

    for (usuario in usuarios) {
        for (libro in libros) {
            println(puedePrestarLibro(usuario, libro))
        }

    }



    println("\n----Ejercicio 6----\n")


    val articulo1 = Articulo("Cuaderno", 25.0)
    val articulo2 = Articulo("Boligrafo", 45.0)

    val ordenador1 = Ordenador(
        nombre = "PC Gamer",
        precio = 1299.99,
        tipo = TipoOrdenador.GAMING
    )

    val ordenador2 = Ordenador(
        nombre = "PC Basico",
        precio = 399.99
    )


    val articulos = listOf(articulo1, articulo2, ordenador1, ordenador2)

    for (articulo in articulos) {
        articulo.promocionNavidad(10.0)
        println(articulo)
    }


    println("\n----Ejercicio 7----\n")

    val vehiculo = Vehiculo7("Generica", "Base", 50)
    val coche7 = Automovil("Toyota", "RAV4", 60, "SUV")
    val moto = Motocicleta("Yamaha", "MT-07", 14, 689)

    val listaVehiculos = listOf(vehiculo, coche7, moto)

    for (v in listaVehiculos) {
        println("-----------")
        v.mostrarInformacion()
    }


    println("\n----Ejercicio 8----\n")


    val persona = Persona("Lucía", 21)
    println(persona.nombre)
    println(persona.edad)


    persona.cumple()


    println("Accediendo a propiedades: ${persona.nombre}, ${persona.edad}")
    println("Usando toString(): $persona")

    println("-----------")


    val estudiante8 = Estudiante8("Carlos", 20, "Informática")
    persona.actividad()
    estudiante8.actividad()

    println("-----------")


    try {
        val estudianteError = Estudiante8("Ana", -5, "Matemáticas")
        println(estudianteError)
    } catch (e: IllegalArgumentException) {
        println("Error al crear estudiante: ${e.message}")
    }


    println("\n----Ejercicio 9----\n")

    val estudiante9 = Estudiante9(
        nombre = "Ana",
        edad = 20,
        id = "E001",
        curso = "2º DAM",
        calificacionPromedio = 8.5
    )

    val profesor9 = Profesor9(
        nombre = "Luis",
        edad = 45,
        id = "P001",
        departamento = "Informática",
        aniosExperiencia = 20
    )

    println("---- Estudiante ----")
    estudiante9.mostrarRol()
    estudiante9.mostrarCalificacion()

    println("---- Profesor ----")
    profesor9.mostrarRol()
    profesor9.mostrarExperiencia()




    println("\n----Ejercicio 10----\n")

    val persona10 = Persona10("Julia", 24)
    println(persona10)
    println(persona10.celebrarCumple())

    println("-----------")

    val empleado10 = Empleado10("Pablo", 30, 32000, 12)
    println(empleado10)
    println(empleado10.trabajar())
    println(empleado10.celebrarCumple())

    println("-----------")

    val gerente10 = Gerente10(
        nombre = "Ana",
        edad = 40,
        salarioBase = 50000.0,
        bonus = 10000.0,
        exentoImpuestos = false
    )

    println(gerente10)
    println(gerente10.trabajar())
    println(gerente10.administrar())
    println(gerente10.celebrarCumple())


}