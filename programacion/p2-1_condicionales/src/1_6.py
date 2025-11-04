def pregunta_nombre_genero():
    nombre = input("Ingrese nombre: ")
    genero = input("Ingrese genero (masculino, feminino): ")
    return nombre,genero

def clase(nombre:str,genero:str):
    if nombre.upper() < "M" and genero == "femenino":
        return "Perteneces al grupo A"
    elif nombre.upper() > "N" and genero == "masculino":
        return "Perteneces al grupo A"
    else:
        return "Perteneces al grupo B"



def main():
    nombre,genero = pregunta_nombre_genero()
    resultado = clase(nombre,genero)
    print(resultado)


if __name__ == '__main__':
    main()