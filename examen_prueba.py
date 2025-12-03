ejecucion = input("dime que quieres hacer:\n"
                "MOVE (número) TO (varialble).\n"
                "ADD (variable) TO (varialble).\n"
                "DISPLAY (variable).\n"
                "STOP.\n"
                ">>> ")

comando = ejecucion.split()

reserva = ["MOVE","ADD","DISPLAY","STOP", "move", "add", "display", "stop"]
memoria = {}


while len(comando) > 0 and comando[0] != "STOP.":
    if comando[0] == "MOVE":
        if len(comando) == 4 and comando[1].isdigit() and comando[2] == "TO":
            if comando[3].endswith("."):
                comando[3] = comando[3][:-1]

                if comando[3] in reserva:
                    print(comando[3] ,"es una palabra reservada del sistema y estas solo se pueden usar para ejecutar los comandos.\n")

                elif not comando[3].isidentifier():
                    print(comando[3] ,"contiene caracteres inválidos o empieza por número y no puede guardarse como nombre de una variable.\n")

                else:
                    memoria[comando[3]] =  int(comando[1])
                    print (memoria,"\n")
            else:
                print ("El comando no ha terminado con un punto\n")
        else:
            if len(comando) != 4:
                print ("El comando MOVE no tiene 4 parametros, intenta escribirlo de la siguiente manera: MOVE (valor) TO (varialble).\n")
            elif not comando[1].isdigit():
                print ("El comando MOVE requiere como valor un numero, intenta escribirlo de la siguiente manera: MOVE (valor) TO (varialble).\n")
            else:
                print ("El comando MOVE necesita que le escribas TO para declararle a quien le quieres asignar el valor de tu variable\n")

    elif comando[0] == "ADD":



    elif comando[0] == "DISPLAY":






    ejecucion = input("dime que quieres hacer.:\n"
                      "MOVE (valor) TO (varialble).:\n"
                      "ADD (valor) TO (varialble).:\n"
                      "DISPLAY (variable).:\n"
                      "STOP.:\n"
                      ">>> ")

    comando = ejecucion.split()

print ("----- Programa terminado ------\n")