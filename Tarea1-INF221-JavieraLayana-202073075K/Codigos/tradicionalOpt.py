import numpy as np
import time  # Importar el módulo time para medir tiempo de ejecución

def multiplicar_matrices_optimizado(A, B):
    if len(A[0]) != len(B):
        print("Las matrices no se pueden multiplicar")
        return

    # Transponer la matriz B
    B_T = B.T
    
    # Matriz Resultado
    C = np.zeros([A.shape[0], B_T.shape[0]], dtype=int)

    # Algoritmo cúbico optimizado
    for i in range(len(A)):
        for j in range(len(B_T)):
            suma = 0
            for k in range(len(B_T[0])):
                suma += A[i][k] * B_T[j][k]
            C[i][j] = suma

    return C

# Función para cargar matrices desde archivos .txt
def cargar_matriz_txt(archivo):
    return np.loadtxt(archivo, dtype=int)

# Cargar matrices A y B desde archivos .txt
A = cargar_matriz_txt('matrizA.txt')
B = cargar_matriz_txt('matrizB.txt')


# Medir el tiempo de ejecución inicial
inicio = time.time() 
# Multiplicar matrices
C = multiplicar_matrices_optimizado(A, B)
# Medir tiempo final
fin = time.time()  

# Mostrar el resultado
#print("Resultado de la multiplicación de A y B:\n", C)
tiempo_ejecucion = fin - inicio
print(f"Tiempo de ejecución: {tiempo_ejecucion:.6f} segundos")