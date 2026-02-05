// ============================================================
// Ejemplo didáctico del patrón Abstract Factory en Kotlin
// Contexto: un juego de aventuras que puede ambientarse
// en un mundo medieval o en uno futurista.
//
// Objetivo: crear familias de objetos relacionados sin
// acoplar el cliente a clases concretas.
// ============================================================

// 1) Productos abstractos:
//    Definen "qué" puede hacer cada tipo de producto.
interface Arma {
    fun atacar(): String
}

interface Vehiculo {
    fun mover(): String
}

interface Armadura {
    fun proteger(): String
}

interface Rol {
    fun accion(): String
}

// 2) Fábrica abstracta (clase abstracta):
//    Declara los métodos para crear cada tipo de producto.
abstract class MundoFactory {
    abstract fun crearArma(): Arma
    abstract fun crearVehiculo(): Vehiculo
    abstract fun crearArmadura(): Armadura
}

abstract class ExploradorFactory {
    abstract fun crearRol(): Rol
}

// 3) Productos concretos para el MUNDO MEDIEVAL:
//    Implementan los contratos de los productos abstractos.
class Espada : Arma {
    override fun atacar(): String = "⚔️  La espada hace *clang* contra el enemigo."
}

class Caballo : Vehiculo {
    override fun mover(): String = "🐎  El caballo galopa entre los árboles."
}

class CotaDeMalla : Armadura {
    override fun proteger(): String = "🛡️  La cota de malla absorbe el impacto."
}

// 4) Productos concretos para el MUNDO FUTURISTA.
class Laser : Arma {
    override fun atacar(): String = "🔫  El láser dispara un rayo de luz azul."
}

class MotoJet : Vehiculo {
    override fun mover(): String = "🏍️  La moto-jet planea a ras del suelo."
}

class EscudoDeEnergia : Armadura {
    override fun proteger(): String = "🛡️  El escudo de energía desvía el daño."
}

// Productos concretos para el MUNDO SUBMARINO.
class LanzaArpones : Arma {
    override fun atacar(): String = " El lanzaarpones lanza un arpon a propulsion."
}

class Submarino : Vehiculo {
    override fun mover(): String = " El submarino se mueve agilmente bajo agua."
}

class EquipoDeBuzo : Armadura {
    override fun proteger(): String = " El traje te permite respirar bajo el agua"
}

// Roles
class Tank : Rol {
    override fun accion(): String = "Soy tank y atraigo el agro de los enemigos para que me peguen a mi."
}

class Healer : Rol {
    override fun accion(): String = "Soy healer y curo a mis compañeros."
}

class Dps : Rol {
    override fun accion(): String = "Soy dps y hago el daño del equipo"
}

// 5) Fábricas concretas:
//    Crean una familia coherente de productos.
class MundoMedievalFactory : MundoFactory() {
    override fun crearArma(): Arma = Espada()
    override fun crearVehiculo(): Vehiculo = Caballo()
    override fun crearArmadura(): Armadura = CotaDeMalla()
}

class MundoFuturistaFactory : MundoFactory() {
    override fun crearArma(): Arma = Laser()
    override fun crearVehiculo(): Vehiculo = MotoJet()
    override fun crearArmadura(): Armadura = EscudoDeEnergia()
}

class MundoSubmarinoFactory : MundoFactory(){
    override fun crearArma(): Arma = LanzaArpones()
    override fun crearVehiculo(): Vehiculo = Submarino()
    override fun crearArmadura(): Armadura = EquipoDeBuzo()
}

class ExploradorTankFactory : ExploradorFactory() {
    override fun crearRol(): Rol = Tank()
}

class ExploradorHealerFactory : ExploradorFactory() {
    override fun crearRol(): Rol = Healer()
}

class ExploradorDpsFactory : ExploradorFactory() {
    override fun crearRol(): Rol = Dps()
}


// 6) Clase abstracta de dominio:
//    Representa a un explorador, reutiliza comportamiento
//    común y trabaja con productos abstractos.
abstract class Explorador(
    protected val arma: Arma,
    protected val vehiculo: Vehiculo,
    protected val armadura: Armadura,
    protected val rol: Rol
) {
    // Comportamiento común que usa la familia de productos.
    fun explorar(): String = buildString {
        appendLine("🧭  El explorador se prepara para la misión...")
        appendLine(rol.accion())
        appendLine(armadura.proteger())
        appendLine(vehiculo.mover())
        appendLine(arma.atacar())
        appendLine("✅  Misión completada en este mundo.")
    }
}

// 7) Personaje concreto que hereda de la clase abstracta.
class ExploradorCurioso(
    arma: Arma,
    vehiculo: Vehiculo,
    armadura: Armadura,
    rol: Rol
) : Explorador(arma, vehiculo, armadura, rol)

// 8) Cliente:
//    Solo conoce la fábrica abstracta y los productos abstractos.
class Juego(private val factory: MundoFactory, private val factoryEx: ExploradorFactory) {

    // Crear al personaje con el equipamiento adecuado.
    private val explorador: Explorador = ExploradorCurioso(
        arma = factory.crearArma(),
        vehiculo = factory.crearVehiculo(),
        armadura = factory.crearArmadura()
        rol = factoryEx.crearRol()
    )

    fun iniciarMision(): String = explorador.explorar()
}

// 9) Etapa de configuración:
//    Aquí se decide qué fábrica concreta usar (fuera del cliente).
enum class TipoMundo { MEDIEVAL, FUTURISTA, SUBMARINO }

enum class TipoExplorador { TANK, HEALER, DPS}

data class ConfiguracionMundo(val tipo: TipoMundo, val tipoEx: TipoExplorador)


object ConfiguradorJuego {
    // Mapea la configuración a la fábrica concreta adecuada.
    fun crearJuego(config: ConfiguracionMundo): Juego {
        val factory = when (config.tipo) {
            TipoMundo.MEDIEVAL -> MundoMedievalFactory()
            TipoMundo.FUTURISTA -> MundoFuturistaFactory()
            TipoMundo.SUBMARINO -> MundoSubmarinoFactory()
        }
        val factoryEx = when (config.tipoEx) {
            TipoExplorador.TANK -> ExploradorTankFactory()
            TipoExplorador.HEALER -> ExploradorHealerFactory()
            TipoExplorador.DPS -> ExploradorDpsFactory()
        }
        return Juego(factory,factoryEx)
    }
}

// 10) Punto de entrada:
//     Crea configuraciones de ejemplo y ejecuta el juego.
fun main() {
    val configuraciones = listOf(
        ConfiguracionMundo(TipoMundo.MEDIEVAL, TipoExplorador.TANK),
        ConfiguracionMundo(TipoMundo.FUTURISTA, TipoExplorador.HEALER),
        ConfiguracionMundo(TipoMundo.SUBMARINO, TipoExplorador.DPS)
    )

    configuraciones.forEach { config ->
        // Mostrar el nombre del mundo en un formato legible.
        val nombre = config.tipo.name.lowercase().replaceFirstChar { it.uppercase() }
        println("=== Mundo $nombre ===")
        val juego = ConfiguradorJuego.crearJuego(config)
        println(juego.iniciarMision())
        println()
    }

    // Idea para los alumnos:
    // Intenten crear un tercer mundo (por ejemplo "Submarino")
    // y vean que el cliente (Juego) no necesita modificarse.

}
