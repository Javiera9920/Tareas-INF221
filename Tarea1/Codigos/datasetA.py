import random

#Crea un archivo .txt con Datos aleatorios y Grandes 
f = open("aleatorios.txt", "w")
lista_numeros = ""
x = 50000
# Generar una lista de n números enteros aleatorios entre 1 y x
for _ in range(x):
    lista_numeros += str(random.randint(1,150000))+" "
f.write(lista_numeros)
f.close()
print(x, "Datos aleatorios generados y guardados en 'aleatorios.txt'.")