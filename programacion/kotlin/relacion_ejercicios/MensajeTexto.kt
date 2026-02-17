package org.example

class MensajeTexto(private val numeroTelefono: String) : Notificable {

    override fun enviarNotificacion() {
        println("Enviando SMS al numero $numeroTelefono")
    }
}
