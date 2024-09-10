import time  # Importar el módulo time para medir tiempo de ejecución

#Lectura de dataset
with open("semiordenados.txt", "r") as f:
    lista = f.read().split()
    lista = [int(x) for x in lista]  # str a int   


# Medir el tiempo de ejecución inicial
inicio = time.time() 
#Uso de .sort() para ordenamiento de la lista    
lista.sort()
# Medir tiempo final
fin = time.time()  


# Imprimir el resultado
#print(lista)
# Imprimir el tiempo de ejecución
tiempo_ejecucion = fin - inicio
print(f"Tiempo de ejecución: {tiempo_ejecucion:.6f} segundos")