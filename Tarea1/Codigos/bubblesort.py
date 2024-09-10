import time  # Importar el módulo time para medir tiempo de ejecución

def bubble_sort(list):
    n = len(list)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
                swapped = True
        if not swapped: break


#Lectura de dataset
with open("semiordenados.txt", "r") as f:
    lista = f.read().split()
    lista = [int(x) for x in lista]  # str a int   


# Medir el tiempo de ejecución inicial
inicio = time.time() 
# Dada una lista desordenada, ordenarla utilizando bubble sort
bubble_sort(lista)
# Medir tiempo final
fin = time.time()  


# Imprimir la lista ordenada
#print(lista)
# Imprimir el tiempo de ejecución
tiempo_ejecucion = fin - inicio
print(f"Tiempo de ejecución: {tiempo_ejecucion:.6f} segundos")