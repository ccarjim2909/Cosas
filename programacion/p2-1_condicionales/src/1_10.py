def pedir_tipo_pizza():
    tipo = input("¿Desea pizza vegetariana? (si/no): ")
    return tipo


def elegir_ingrediente(tipo: str) -> str:
    ingredientes = ["mozzarella", "tomate"]

    if tipo.lower() == "si":
        menu = ["pimiento", "tofu"]
        ingrediente_extra = input("Elija un ingrediente vegetariano (pimiento/tofu): ")
        if ingrediente_extra.lower() not in menu:
            return "Ingrediente no valido. Debe elegir pimiento o tofu."
        ingredientes.append(ingrediente_extra)
        tipo_pizza = "vegetariana"
    elif tipo.lower() == "no":
        menu = ["peperoni", "jamon", "salmon"]
        ingrediente_extra = input("Elija un ingrediente no vegetariano (peperoni/jamon/salmon): ")
        if ingrediente_extra.lower() not in menu:
            return "Ingrediente no valido. Debe elegir peperoni, jamon o salmon."
        ingredientes.append(ingrediente_extra)
        tipo_pizza = "no vegetariana"
    else:
        return "Respuesta no valida. Debe responder 'si' o 'no'."


    ingredientes_str = ingredientes[0]
    for i in range(1, len(ingredientes)):
        ingredientes_str = ingredientes_str + ", " + ingredientes[i]

    return "Su pizza es " + tipo_pizza + " y lleva: " + ingredientes_str


def main():
    tipo = pedir_tipo_pizza()
    resultado = elegir_ingrediente(tipo)
    print(resultado)


if __name__ == "__main__":
    main()
