import numpy as np
import time  # Importar el módulo time para medir tiempo de ejecución

# Función para verificar si un número es una potencia de 2
def es_potencia_de_2(n):
    return (n & (n - 1)) == 0 and n > 0

def strassen(A, B):
    n = len(A)
    
    if n <= 2:  # caso base
        return np.dot(A, B)
    
    # DIVIDIR MATRICES EN SUBMATRICES
    mid = n // 2
    A11 = A[:mid, :mid]
    A12 = A[:mid, mid:]
    A21 = A[mid:, :mid]
    A22 = A[mid:, mid:]
    B11 = B[:mid, :mid]
    B12 = B[:mid, mid:]
    B21 = B[mid:, :mid]
    B22 = B[mid:, mid:]
    
    # MULTIPLICACIÓN RECURSIVA
    P1 = strassen(A11, B12 - B22)
    P2 = strassen(A11 + A12, B22)
    P3 = strassen(A21 + A22, B11)
    P4 = strassen(A22, B21 - B11)
    P5 = strassen(A11 + A22, B11 + B22)
    P6 = strassen(A12 - A22, B21 + B22)
    P7 = strassen(A11 - A21, B11 + B12)
    
    # COMBINAR RESULTADOS PARA FORMAR C
    C11 = P5 + P4 - P2 + P6
    C12 = P1 + P2
    C21 = P3 + P4
    C22 = P5 + P1 - P3 - P7
    
    # UNIR SUBMATRICES PARA FORMAR LA MATRIZ C
    C = np.vstack((np.hstack((C11, C12)), np.hstack((C21, C22))))
    return C

# Función para cargar matrices desde archivos .txt
def cargar_matriz_txt(archivo):
    return np.loadtxt(archivo, dtype=int)  # Cargar matriz de un archivo de texto

# Cargar matrices A y B desde archivos .txt
A = cargar_matriz_txt('matrizA.txt')
B = cargar_matriz_txt('matrizB.txt')

# Asegurarse de que las matrices sean cuadradas y compatibles para Strassen
if A.shape == B.shape and A.shape[0] == A.shape[1] and es_potencia_de_2(A.shape[0]):
    # Medir el tiempo de ejecución inicial
    inicio = time.time() 
    # Realizar la multiplicación de Strassen
    C = strassen(A, B)
    # Medir tiempo final
    fin = time.time()  

    #print("Matriz C (Resultado de A * B):\n", C)
    tiempo_ejecucion = fin - inicio
    print(f"Tiempo de ejecución: {tiempo_ejecucion:.6f} segundos")

else:
    print("Error: Las matrices no son cuadradas o no tienen las mismas dimensiones.")

