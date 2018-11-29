import time
from random import randint
import xlsxwriter
import matplotlib.pyplot as plt
import numpy as np
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.plotly as py
import plotly.tools as tls




#---------------------------------------------------------------------insertionSort---------------------------------------------------------------------
def insertionSort(alist):
   for index in range(1,len(alist)):
     currentvalue = alist[index]
     position = index
     while position > 0 and alist[position-1] > currentvalue:
         alist[position] = alist[position-1]
         position = position-1
     alist[position] = currentvalue
#---------------------------------------------------------------------insertionSort---------------------------------------------------------------------


#---------------------------------------------------------------------mergeSort------------------------------------------------------------------------
def mergeSort(alist):

    if len(alist)>1:

        #Dividir la lista formando sublistas
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        #Ordena cada una de las sublistas
        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=0
        j=0
        k=0
        #Intercala de forma ordenada las sublistas
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
#---------------------------------------------------------------------mergeSort------------------------------------------------------------------------


#---------------------------------------------------------------------stoogesort------------------------------------------------------------------------
    def stoogesort(arr, l, h):
        if l >= h:
            return

        # Si el primer elemento es más pequeño que el anterior, cámbiamos
        if arr[l] > arr[h]:
            t = arr[l]
            arr[l] = arr[h]
            arr[h] = t

        # Si hay más de 2 elementos en la matriz.
        if h -l + 1 > 2:
            t = (int)((h - l + 1) / 3)
            # Ordenar recursivamente los primeros 2/3 elementos
            stoogesort(arr, l, (h - t))
            # Ordenar recursivamente los ultimos 2/3 elementos
            stoogesort(arr, l + t, (h))
            # Ordenar recursivamente los primeros 2/3 elementos de nuevo para confirmar
            stoogesort(arr, l, (h - t))
        # main
#---------------------------------------------------------------------stoogesort------------------------------------------------------------------------


#---------------------------------------------------------------------quickSort------------------------------------------------------------------------
def quickSort(alist):
    quickSortHelper(alist, 0, len(alist) - 1)

def quickSortHelper(alist, first, last):
    #se ingresa al encontrar que un valor a la izquierda del arreglo es mayor que uno a su derecha
    if first < last:
        #inicialización de punto de división
        splitpoint = partition(alist, first, last)
        #llamada recursiva para localizar y desplazar los valores que son menores que el comparativo
        quickSortHelper(alist, first, splitpoint - 1)
        #llamada recursiva para localizar y desplazar los valores que son mayores que el comparativo
        quickSortHelper(alist, splitpoint + 1, last)

def partition(alist, first, last):
    pivotvalue = alist[first]
    #inicialización de marcadores de posición: leftmark y rightmark
    leftmark = first + 1
    rightmark = last

    done = False
    while not done:
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            #si el valor de la izquierda es menor que el valor del pivote la marca izquierda se acerca un elemento hacia el pivote
            leftmark = leftmark + 1
        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            #si el valor de la derecha es menor que el valor del pivote la marca derecha se acerca un elemento hacia el pivote
            rightmark = rightmark - 1
        if rightmark < leftmark:
            #si la marca izquierda es mayor que la marca derecha se finaliza el bucle while
            done = True
        else:
            #intercambio de valor de la posición de los marcadores para ordenarlos
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp
    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp
    return rightmark
#---------------------------------------------------------------------quickSort------------------------------------------------------------------------



workbook = xlsxwriter.Workbook('Tiempos.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write(4, 0, "n")
worksheet.write(4, 1, "Merge Sort")
worksheet.write(4, 2, "Insertion Sort")
worksheet.write(4, 3, "Quick Sort")
worksheet.write(4, 4, "Stooge Sort")

#inciando sesion en plotly
plotly.tools.set_credentials_file(username='esperanza.96', api_key='dgaQmgksjeqSqPZ1kXRG')

j = 4
cont = 10
L = []
L2 = []
L3 = []
ArregloTiempoMS=[]##arreglo de los tiempos de MERGE SORT
ArregloTiempoIS=[]#arreglo de los tiempos de INSERTION SORT
ArregloTiempoQS=[]#arreglo de los tiempos de QUICK SORT
Ndatos=[]#arreglo de los n datos

while cont <= 200:
    for i in range (0, cont):
        L.append(randint(0,500))
    L2 = L.copy()
    start_time = time.time()
    mergeSort(L)
    endtime = time.time() - start_time
    print("Merge sort para " + str(len(L)) + ": --- %s seconds ---"%"{0:.22f}".format(endtime))

    j += 1
    worksheet.write(j, 0, str(len(L)))
    worksheet.write(j, 1, endtime)
    ArregloTiempoMS.append(endtime)#agregando tiempos  al arreglo de MergeSort


    start_time = time.time()
    insertionSort(L2)
    endtime = time.time() - start_time
    print("Insertion sort para " + str(len(L2)) + ": --- %s seconds ---"%"{0:.22f}".format(endtime))
    worksheet.write(j, 2, endtime)
    ArregloTiempoIS.append(endtime)#agregando tiempos al arreglo de InsertionSort

    L3 = L2.copy()
    start_time = time.time()
    quickSort(L3)
    endtime = time.time() - start_time
    print("Quick sort para " + str(len(L3)) + ": --- %s seconds ---" % "{0:.22f}".format(endtime))
    worksheet.write(j, 3, endtime)
    ArregloTiempoQS.append(endtime)#agregando tiempos al arreglo de Quickort


    L = []
    Ndatos.append(cont)
    cont+=10




plt.figure()
#son los 3 ordenamientos
plt.plot(Ndatos, ArregloTiempoMS, '-')
plt.plot(Ndatos, ArregloTiempoIS, '-')
plt.plot(Ndatos, ArregloTiempoQS, '-')


plt.title("Grafico de los metodos de ordenamiento: MergeSort, InsertionSort, QuickSort")

fig = plt.gcf()
#fig.set_size_inches(200,120,True)
plotly_fig = tls.mpl_to_plotly( fig )

plotly_fig["data"][0]["error_y"].update({
                                         "visible": True,
                                         "color":"rgb(255,127,14)",
                                         "value":0.04,
                                         "type":"constant"
                                       })
plotly_fig["data"][0]["error_x"].update({
                                         "visible": True,
                                         "color":"rgb(255,127,14)",
                                         "value":0.04,
                                         "type":"constant"
                                       })


py.plot(plotly_fig, filename='Graficos Tiempo vs datos')


workbook.close()
