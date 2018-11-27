# Referencias:
# http://interactivepython.org/courselib/static/pythonds/SortSearch/TheQuickSort.html

import time

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


tiempo = time.time()

lista = [10, 12, 4, 1, 7, 50, 24, 14, 34, 2, 5, 26, 18, 20, 3, 47, 5, 23, 37, 9, 44, 32, 17, 31, 49, 13]

quickSort(lista)

print(time.time() - tiempo)
print("segundos")

