package org.example

class Lavadora : EncendidoApagado, DispositivoElectronico {

    private var encendida = false

    override fun encender() {
        encendida = true
        println("Lavadora encendida")
    }

    override fun apagar() {
        encendida = false
        println("Lavadora apagada")
    }

    override fun reiniciar() {
        if (encendida) {
            println("Reiniciando la lavadora")
        } else {
            println("No se puede reiniciar: la lavadora esta apagada")
        }
    }
}
