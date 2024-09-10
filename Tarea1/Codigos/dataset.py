import random


n = 10000  # Cantidad de elementos

# Función para generar un conjunto de datos parcialmente ordenados
def generar_datos_parciales(n, porcentaje_desorden):
    # Generar una lista ordenada de 1 a n
    lista = list(range(1, n+1))    
    # Calcular cuántos elementos desordenar
    elementos_a_desordenar = int(n * porcentaje_desorden / 100)
    # Elegir índices aleatorios para desordenar
    indices = random.sample(range(n), elementos_a_desordenar)
    # Desordenar esos elementos elegidos
    for i in indices:
        lista[i] = random.randint(1, n)
    
    return lista

# Guardar la lista en un archivo txt
def guardar_datos_en_txt(lista, nombre_archivo):
    with open(nombre_archivo, "w") as f:
        for num in lista:
            f.write(f"{num} ")
            
# Parámetros
porcentaje_desorden = 50  # Porcentaje de desorden (por ejemplo, 10%)

# Generar conjunto de datos semiordenado
datos_parciales = generar_datos_parciales(n, porcentaje_desorden)
# Guardar en archivo de texto
guardar_datos_en_txt(datos_parciales, "parciales.txt")

print(n, "Datos parcialmente ordenados generados y guardados en 'parciales.txt'.")