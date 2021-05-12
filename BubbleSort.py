tamlista = int(input("Tamanho da Lista: "))
lista = [int(input("Número: ")) for i in range(tamlista)]
print("\n\nA lista é:", (lista))

def bubble_sort(lista):
    n=len(lista)
    for j in range(n-1):
        for i in range(n-1):
             if lista[i] > lista[i+1]:
                 lista[i], lista[i+1] = lista[i+1], lista[i]

bubble_sort(lista)
print("\nA lista ordenada é: ", lista)
