tamlista = int(input("Tamanho da Lista: "))
lista = [int(input("Número: ")) for i in range(tamlista)]
print("\n\nA lista é:", (lista))

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

quick_sort(lista)
print("\nA lista ordenada é: ", lista)
