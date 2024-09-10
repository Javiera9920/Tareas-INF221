import numpy as np

# Función para generar matriz
def generar_matriz(n_filas, n_columnas, tipo='aleatorio'):
    if tipo == 'aleatorio':
        return np.random.randint(0, 100, size=(n_filas, n_columnas))  # Números enteros aleatorios
    elif tipo == 'ordenado':
        return np.array([np.arange(i, i + n_columnas) for i in range(n_filas)])

# Guardar matriz en formato txt (separado por espacios)
def guardar_matriz_txt(matriz, archivo):
    np.savetxt(archivo, matriz, fmt='%d', delimiter=' ')  # Guardar cada valor con espacios entre ellos

f1= 65
c1 = 75
f2 = 75
c2= 55
# Generar una matriz aleatoria  A
matrizA = generar_matriz(f1, c1, tipo='aleatorio')
# Guardar la matriz en formato txt
guardar_matriz_txt(matrizA, 'matrizA.txt')
print("Matriz de tamaño",f1,"x",c1, "generada y guardada en 'matrizA.txt'.")

#Generar una matriz aleatoria B
matrizB = generar_matriz(f2, c2, tipo='aleatorio')
guardar_matriz_txt(matrizB, 'matrizB.txt')
print("Matriz de tamaño", f2,"x",c2,"generada y guardada en 'matrizB.txt'.")