fun main() {
    val contrasenaGuardada = "contraseña"

    println("Introduce la contraseña: ")
    val intentoUsuario = readln()

    if (intentoUsuario == contrasenaGuardada) {
        println("La contraseña coincide.")
    } else {
        println("La contraseña no coincide.")
    }
}