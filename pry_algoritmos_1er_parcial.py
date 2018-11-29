from random import randint
import time
import os.path
from pathlib import Path

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
        nombreArchivo = input("Escriba el nombre de su archivo ubicado en la carpeta: ")
        nombreArchivo = nombreArchivo + ".txt"

        if (os.path.isfile(".\\" + nombreArchivo)):
            print("El archivo " + nombreArchivo + " ha sido encontrado")
            print("\n")

            archivoAnalisis = open(".\\" + nombreArchivo,"r")
            salirDeAnalisis = False

            salirEscogerCantidad = False

            while (salirEscogerCantidad == False):
                cantidadNumeros = input("Ingrese la cantidad de números que desea tomar del archivo (Max 1000): ")
                if(str.isdigit(cantidadNumeros)):
                    cantidadNumeros = int(cantidadNumeros)
                else:
                    print("No ha ingresado un número válido")
                contador = 0
                if (cantidadNumeros <= 1000):
                    arregloAnalisis = [0]*cantidadNumeros
                    for j in archivoAnalisis:
                        #print(archivoAnalisis.readline())
                        arregloAnalisis[contador] = int(j)
                        contador = contador + 1
                        if(contador == cantidadNumeros):
                            break

                    archivoAnalisis.close()
                    salirEscogerCantidad = True
                    #print(arregloAnalisis)

            while (salirDeAnalisis == False):

                print("Escoja el tipo de analisis que desea")
                print("\n")

                print("(1) Comparación Insertion Sort vs Merge Sort")
                print("(2) Comparación Insertion Sort vs Quick Sort")
                print("(3) Comparación Merge Sort vs Quick Sort")
                print("(4) Comparar todos los algoritmos")
                print("(5) Volver al menú principal")

                opcionComparacion = input("Escriba una opcion: ")
                print("\n")
            
                if (opcionComparacion == "1"):
                    print("Insertion Sort vs Merge Sort")
                    arregloA = arregloAnalisis
                    arregloB = arregloAnalisis
                    #---------------- Insertar Arreglos ----------------
                    #---------------- Insertar Arreglos ----------------
                elif (opcionComparacion == "2"):
                    print("Insertion Sort vs Quick Sort")
                    arregloA = arregloAnalisis
                    arregloB = arregloAnalisis
                    #---------------- Insertar Arreglos ----------------
                    #---------------- Insertar Arreglos ----------------
                elif (opcionComparacion == "3"):
                    print("Merge Sort vs Quick Sort")
                    arregloA = arregloAnalisis
                    arregloB = arregloAnalisis
                    #---------------- Insertar Arreglos ----------------
                    #---------------- Insertar Arreglos ----------------
                elif (opcionComparacion == "4"):
                    print("Comparar todos los algoritmos")
                    arregloA = arregloAnalisis
                    arregloB = arregloAnalisis
                    arregloC = arregloAnalisis
                    #---------------- Insertar Arreglos ----------------
                    #---------------- Insertar Arreglos ----------------
                elif (opcionComparacion == "5"):
                    print("Volviendo al menú principal...")
                    salirDeAnalisis = True
                else:
                    print("La opción " + opcionComparacion + " no es válida")

        else:
            print("El archivo " + nombreArchivo + " no existe \n")
            print("Intente generar un archivo aleatorio.txt desde la opción del menú principal")
            print("\n")

    elif (opcion == "2"):
        print ("GENERAR ARCHIVO ALEATORIO")
        archivoAleatorio = open(".\\aleatorio.txt","w")
        elementos = 1000

        listaAleatoria = [0]*elementos
        for i in range(elementos):
            listaAleatoria[i] = randint(1000000, 9999999)
            archivoAleatorio.write(str(listaAleatoria[i]) + "\n")

        archivoAleatorio.close()
        #print(listaAleatoria)
        print ("Archivo generado!\n")

    elif (opcion == "3"):
        print ("SALIENDO...")
        print ("Gracias por usar el sistema de comparación \n")
        salir = True

    else:
        print("(" + opcion + ") no es una opción válida...")


