class Contraseña(private val contraseña: String, val contraseña_usuario: String) {
    fun comparar(): Boolean {

    }
}

fun main() {
    val contraseña = "1234"

    print("Introduce la contraseña: ")
    val contraseñaUsuario = readLine()

    if (contraseña == contraseñaUsuario) {
        println("La contraseña es correcta")
    }
    else {
        println("La contraseña es incorrecta")
    }
}