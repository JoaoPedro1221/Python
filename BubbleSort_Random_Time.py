import time
import timeit

import random
lista = random.sample(range(1, 100000), 10000)

def bubble_sort(lista):
    n=len(lista)
    for j in range(n-1):
        for i in range(n-1):
             if lista[i] > lista[i+1]:
                 lista[i], lista[i+1] = lista[i+1], lista[i]

inicio = timeit.default_timer()
bubble_sort(lista)
fim = timeit.default_timer()
print ('Duração da Função: %f' % (fim - inicio))
