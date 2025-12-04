import sys

archivo = sys.argv[1]

with open(archivo, "r") as f:
    lineas = [l.strip() for l in f.readlines() if l.strip()]



programas = int(lineas[0])

lineas_comandos = iter(lineas[1:])

reserva = ["MOVE","ADD","DISPLAY","STOP", "move", "add", "display", "stop"]

display = []



for programa_actual in range(1, programas + 1):
    memoria = {}
    ejecucion = next(lineas_comandos)
    comando = ejecucion.split()

    while len(comando) > 0 and comando[0] != "STOP.":
        if comando[0] == "MOVE":
            if len(comando) == 4 and comando[1].isdigit() and comando[2] == "TO":
                if comando[3].endswith("."):
                    comando[3] = comando[3][:-1]

                    if comando[3] in reserva:
                        print(comando[3] ,"es una palabra reservada del sistema y estas solo se pueden usar para ejecutar los comandos.\n")

                    elif len(comando[3]) > 5:
                        print(comando[3] ,"solo puede tener una longitud maxima de 5 caracteres.\n")

                    elif not comando[3].isalpha() or comando[3].isupper():
                        print(comando[3] ,"contiene caracteres inválidos, solo puede tener letras minusculas (a-z) y no puede guardarse como nombre de una variable.\n")

                    else:
                        if len(comando[1]) > 5:
                            comando[1] = int(comando[1]) % 100000

                        memoria[comando[3]] =  int(comando[1])
                        # print (memoria,"\n")

                else:
                    print ("El comando no ha terminado con un punto\n")
            else:
                if len(comando) != 4:
                    print ("El comando MOVE no tiene 4 parametros, intenta escribirlo de la siguiente manera: MOVE (valor) TO (varialble).\n")
                elif not comando[1].isdigit():
                    print ("El comando MOVE requiere como valor un numero, intenta escribirlo de la siguiente manera: MOVE (valor) TO (varialble).\n")
                else:
                    print ("El comando MOVE necesita que le escribas TO para declararle a quien le quieres asignar el valor de tu variable\n")

        elif comando[0] == "DISPLAY":
            if len(comando) > 1:
                if comando[len(comando)-1].endswith("."):
                    comando[len(comando)-1] = comando[len(comando)-1][:-1]
                for variable in comando[1:]:
                    if variable in memoria:
                        display.append(str(memoria[variable]))
                print (",".join(display))
                display = []

        elif comando[0] == "ADD":

            if "GIVING" in comando:
                total = 0
                variable = 1
                if comando[len(comando) - 1].endswith("."):
                    comando[len(comando) - 1] = comando[len(comando) - 1][:-1]

                while comando[variable] != "TO":
                    origen = comando[variable]

                    total = total + int(memoria[origen])

                    variable = variable + 1

                variable = variable + 1

                while comando[variable] != "GIVING":
                    origen = comando[variable]

                    total = total + int(memoria[origen])

                    variable = variable + 1


                variable = variable + 1
                destino = comando[variable]

                if total > 99999:
                    total = total % 100000
                memoria[destino] = total

            else:
                total = 0
                variable = 1
                if comando[len(comando) - 1].endswith("."):
                    comando[len(comando) - 1] = comando[len(comando) - 1][:-1]

                while comando[variable] != "TO":
                    origen = comando[variable]

                    variable = variable + 1

                    total = total + int(memoria[origen])

                variable = variable + 1
                destino = comando[variable]

                suma = memoria[destino] + total

                if suma > 99999:
                    suma = suma % 100000
                memoria[destino] = suma


        ejecucion = next(lineas_comandos)
        comando = ejecucion.split()




    print ("-----------\n")

