package org.example

class CorreoElectronico(private val emailDestino: String, private val asunto: String) : Notificable {

    override fun enviarNotificacion() {
        println("Enviando correo a $emailDestino con asunto '$asunto'")
    }
}
