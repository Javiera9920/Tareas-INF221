import numpy as np
import time  # Importar el módulo time para medir tiempo de ejecución


def multiplicar_matrices(A, B):
    if len(A[0]) != len(B):
        print("Las matrices no se pueden multiplicar")
        return
    
    # Matriz Resultado
    C = np.zeros([A.shape[0], B.shape[1]], dtype=int)

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                C[i][j] += A[i][k] * B[k][j]

    return C

# Función para cargar matrices desde archivos .txt
def cargar_matriz_txt(archivo):
    return np.loadtxt(archivo, dtype=int)  # Cargar la matriz desde un archivo de texto

# Cargar matrices A y B desde archivos .txt
A = cargar_matriz_txt('matrizA.txt')
B = cargar_matriz_txt('matrizB.txt')


# Medir el tiempo de ejecución inicial
inicio = time.time() 
# Multiplicar matrices
C = multiplicar_matrices(A, B)
# Medir tiempo final
fin = time.time()  

# Mostrar el resultado
#print("Resultado de la multiplicación de A y B:\n", C)
tiempo_ejecucion = fin - inicio
print(f"Tiempo de ejecución: {tiempo_ejecucion:.6f} segundos")