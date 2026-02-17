package org.example

class Telefono : EncendidoApagado, DispositivoElectronico {

    private var encendido = false

    override fun encender() {
        encendido = true
        println("Telefono encendido")
    }

    override fun apagar() {
        encendido = false
        println("Telefono apagado")
    }

    override fun reiniciar() {
        if (encendido) {
            println("Reiniciando telefono")
        } else {
            println("No se puede reiniciar: el telefono esta apagado")
        }
    }
}
