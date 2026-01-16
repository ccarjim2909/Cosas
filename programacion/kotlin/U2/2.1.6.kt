fun main() {
    println("¿Cual es tu nombre? ")
    val nombre = readln().uppercase()

    println("¿Cual es tu sexo (M para mujer, H para hombre)? ")
    val sexo = readln().uppercase()

    val grupo: String

    if ((sexo == "M" && nombre < "M") || (sexo == "H" && nombre > "N")) {
        grupo = "A"
    } else {
        grupo = "B"
    }


    println("Tu grupo es el $grupo")
}