fun main() {
    val datosEntrada = "nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"

    val lineas = datosEntrada.split("\n")

    val encabezados = lineas[0].split(";")

    val directorio = mutableMapOf<String, Map<String, Any>>()

    for (i in 1 until lineas.size) {
        val valores = lineas[i].split(";")

        val nif = valores[0]

        val datosCliente = mutableMapOf<String, Any>()

        for (j in 1 until encabezados.size) {
            val clave = encabezados[j]
            val valor = valores[j]

            if (clave == "descuento") {
                datosCliente[clave] = valor.toDouble()
            } else {
                datosCliente[clave] = valor
            }
        }

        directorio[nif] = datosCliente
    }


    println("Diccionario generado:")
    println(directorio)

}