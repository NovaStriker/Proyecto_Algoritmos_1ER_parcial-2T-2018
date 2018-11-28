from random import randint
import time

salir = False

while (salir==False):
    print("MENÚ PRINCIPAL")
    print("(1) Realizar análisis")
    print("(2) Generar archivo de números aleatorios")
    print("(3) Salir")

    opcion = input("Escriba una opcion: ")
    print("\n")

    if (opcion == "1"):
        print ("REALIZAR ANÁLISIS")
        print ("hola : " + opcion)

    elif (opcion == "2"):
        print ("GENERAR ARCHIVO ALEATORIO")

        listaAleatoria = [0]*1000
        for i in range(1000):
            listaAleatoria[i] = randint(1000000, 9999999)

        print(listaAleatoria)

    elif (opcion == "3"):
        print ("SALIR")
        print ("Gracias por usar el sistema de comparación")
        salir = True

    else:
        print("(" + opcion + ") no es una opción válida...")


