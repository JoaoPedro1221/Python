import time
import timeit

import random
lista = random.sample(range(1, 100000), 10000)

def quick_sort(lista, start=0, end=None):
    if end is None:
        end = len(lista)-1
    if start < end:
        p = partition(lista, start, end)
        quick_sort(lista, start, p-1)
        quick_sort(lista, p+1, end)

def partition(lista, start, end):
    pivo = lista[end]
    high = start

    for low in range(start, end):
        if lista[low] <= pivo:
            lista[low], lista[high] = lista[high], lista[low]
            high = high + 1

    lista[high], lista[end] = lista[end], lista[high]

    return high

inicio = timeit.default_timer()
quick_sort(lista)
fim = timeit.default_timer()
print ('Duração da Função Quick_Sort: %f' % (fim - inicio))


def bubble_sort(lista):
    n=len(lista)
    for j in range(n-1):
        for i in range(n-1):
             if lista[i] > lista[i+1]:
                 lista[i], lista[i+1] = lista[i+1], lista[i]

inicio = timeit.default_timer()
bubble_sort(lista)
fim = timeit.default_timer()
print ('Duração da Função Bubble_Sort: %f' % (fim - inicio))

