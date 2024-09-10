import time  # Importar el módulo time para medir tiempo de ejecución

# Función merge_sort
def merge_sort(lista):
 
   """
   Comprobamos si la longitud de la lista es menor que 2, en caso de serlo se devuelve
   la lista porque significa que ya esta ordenada. 
   """
   if len(lista) < 2:
      return lista
    
    # De lo contrario, dividimos en 2 la lista
   else:
        middle = len(lista) // 2 #mitad
        right = merge_sort(lista[:middle]) #valores a la derecha
        left = merge_sort(lista[middle:]) #valores a la izquiera
        return merge(right, left)
    
# Función merge
def merge(lista1, lista2):
    """
    Intercalamos los elementos de las dos divisiones.
    """
    i, j = 0, 0 # Variables de incremento
    result = [] # Lista de resultado
 
   # Intercalar ordenadamente
    while(i < len(lista1) and j < len(lista2)):
        if (lista1[i] < lista2[j]):
            result.append(lista1[i])
            i += 1
        else:
            result.append(lista2[j])
            j += 1
 
   # Agregamos los resultados a la lista
    result += lista1[i:]
    result += lista2[j:]
 
    # Retornamos el resultados
    return result


#Lectura de dataset
with open("semiordenados.txt", "r") as f:
    lista = f.read().split()
    lista = [int(x) for x in lista]  # str a int


# Medir el tiempo de ejecución inicial
inicio = time.time() 
# función merge_sort para ordenar la lista
merge_sort_result = merge_sort(lista)
# Medir tiempo final
fin = time.time()  


# Imprimir el resultado
#print(merge_sort_result)
# Imprimir el tiempo de ejecución
tiempo_ejecucion = fin - inicio
print(f"Tiempo de ejecución: {tiempo_ejecucion:.6f} segundos")