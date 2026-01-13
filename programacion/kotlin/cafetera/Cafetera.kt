

class Cafetera (val ubicacion: String) {
    var capacidad = 1000
    var cantidad = 0

    init{

    }

    constructor(ubicacion: String, capacidad: Int) : this(ubicacion, capacidad,  capacidad)

    constructor(ubicacion: String, capacidad: Int, cantidad: Int) : this(ubicacion) {
        this.capacidad = capacidad
        this.cantidad = cantidad

    }

    override fun toString(): String {
        return "Cafetera: ubi:$ubicacion cant: $cantidad cap: $capacidad"
    }
}
