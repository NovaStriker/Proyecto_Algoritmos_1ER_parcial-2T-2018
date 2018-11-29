from random import randint
import time
import os.path
from pathlib import Path


def insertionSort(alist):   #definir la funcion del algoritmo que reciba una lista
   for index in range(1,len(alist)): #recorrer la lista
     currentvalue = alist[index] #valor que va tomando index
     position = index
     while position > 0 and alist[position-1] > currentvalue: #comparacion y validacion de la posicion con el indice
         alist[position] = alist[position-1]
         position = position-1
     alist[position] = currentvalue




def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1
        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1


def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:
       splitpoint = partition(alist,first,last)
       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)

def partition(alist,first,last):
   pivotvalue = alist[first]
   leftmark = first+1
   rightmark = last

   done = False
   while not done:
       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1
       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1
       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp
   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp
   return rightmark


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
                    insertionSort(arregloA)
                    mergeSort(arregloB)

                elif (opcionComparacion == "2"):
                    print("Insertion Sort vs Quick Sort")
                    arregloA = arregloAnalisis
                    arregloB = arregloAnalisis
                    insertionSort(arregloA)
                    quickSort(arregloB)

                elif (opcionComparacion == "3"):
                    print("Merge Sort vs Quick Sort")
                    arregloA = arregloAnalisis
                    arregloB = arregloAnalisis
                    mergeSort(arregloA)
                    quickSort(arregloB)



                elif (opcionComparacion == "4"):
                    print("Comparar todos los algoritmos")
                    arregloA = arregloAnalisis
                    arregloB = arregloAnalisis
                    arregloC = arregloAnalisis
                    insertionSort(arregloA)
                    mergeSort(arregloB)
                    quickSort(arregloC)

                    ArregloTiempoMS.append(endtime)  # agregando tiempos  al arreglo de MergeSort

                    start_time = time.time()
                    insertionSort(L2)
                    endtime = time.time() - start_time
                    print("Insertion sort para " + str(len(L2)) + ": --- %s seconds ---" % "{0:.22f}".format(endtime))
                    worksheet.write(j, 2, endtime)
                    ArregloTiempoIS.append(endtime)  # agregando tiempos al arreglo de InsertionSort

                    L3 = L2.copy()
                    start_time = time.time()
                    quickSort(L3)
                    endtime = time.time() - start_time
                    print("Quick sort para " + str(len(L3)) + ": --- %s seconds ---" % "{0:.22f}".format(endtime))
                    worksheet.write(j, 3, endtime)
                    ArregloTiempoQS.append(endtime)  # agregando tiempos al arreglo de Quickort

                    L = []
                    Ndatos.append(cont)
                    cont += 10

            plt.figure()
            # son los 3 ordenamientos
            plt.plot(Ndatos, ArregloTiempoMS, '-')
            plt.plot(Ndatos, ArregloTiempoIS, '-')
            plt.plot(Ndatos, ArregloTiempoQS, '-')

            plt.title("Grafico de los metodos de ordenamiento: MergeSort, InsertionSort, QuickSort")

            fig = plt.gcf()
            # fig.set_size_inches(200,120,True)
            plotly_fig = tls.mpl_to_plotly(fig)

            plotly_fig["data"][0]["error_y"].update({
                "visible": True,
                "color": "rgb(255,127,14)",
                "value": 0.04,
                "type": "constant"
            })
            plotly_fig["data"][0]["error_x"].update({
                "visible": True,
                "color": "rgb(255,127,14)",
                "value": 0.04,
                "type": "constant"
            })

            py.plot(plotly_fig, filename='Graficos Tiempo vs datos')




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


