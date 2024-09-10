import time  # Importar el módulo time para medir tiempo de ejecución

#Lectura de dataset
with open("semiordenados.txt", "r") as f:
    lista = f.read().split()
    lista = [int(x) for x in lista]  # str a int   

#función quicksort
def QuickSort(lista, izq, der):

    #elección de pivote
    pivote = lista[izq]
    i = izq
    j = der
    aux = 0

    while i < j:
        while lista[i] <= pivote and i < j:
            i += 1
        while lista[j] > pivote:
            j -= 1
        if i < j:
            aux = lista[i]
            lista[i] = lista[j]
            lista[j] = aux

    lista[izq] = lista[j]
    lista[j] = pivote

    if izq < j-1:
        QuickSort(lista,izq,j-1)

    if j+1 < der:
        QuickSort(lista,j+1,der)


# Medir el tiempo de ejecución inicial
inicio = time.time() 
QuickSort(lista,0,len(lista) - 1)
# Medir tiempo final
fin = time.time()  

# Imprimir el resultado
#print(lista)
# Imprimir el tiempo de ejecución
tiempo_ejecucion = fin - inicio
print(f"Tiempo de ejecución: {tiempo_ejecucion:.6f} segundos")
