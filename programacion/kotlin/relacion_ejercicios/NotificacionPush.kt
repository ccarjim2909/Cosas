package org.example

class NotificacionPush(private val dispositivoId: String) : Notificable {

    override fun enviarNotificacion() {
        println("Enviando notificacion push al dispositivo $dispositivoId")
    }
}
