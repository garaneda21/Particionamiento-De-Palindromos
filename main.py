# modulo time para medir tiempos de ejecucion basado en la hora del sistema
import time

# importar ambos Algoritmos para ejecutarlos en este codigo y medir su tiempo
from Algotirmo_A import palPart
from Algoritmo_B import minCutDP

# Funcion que obtiene todas las palabras contenidas en el archivo especificado
def leer_palabras(archivo):
    with open(archivo, 'r', encoding='utf-8') as file:
        # Leer el contenido del archivo
        contenido = file.read()
        # Reemplazar las comas por espacios y dividir por espacios y saltos de línea
        palabras = contenido.replace(',', ' ').split()
    return palabras

# obtener todas las palabras
palabras = leer_palabras('palabras.txt')

# Generar un archivo "tiempos.cvs" donde guardar el resultado de los tiempos de los argoritmos
file_path = "tiempos.csv"
with open(file_path, 'w') as file:
    file.writelines("Palabra;Largo de la Palabra;Tiempo A[s];Tiempo B[s]\n")

    i = 1
    # Iterar sobre cada palabra, pasandosela como parametro a los Algoritmos
    # y cromonetrando el tiempo en que retornan con el modulo de time
    for palabra in palabras:
        n = len(palabra)

        # Algoritmo A
        start = time.time()
        palPart(palabra)
        end = time.time()

        tiempo_A = end - start

        # Algoritmo A
        start = time.time()
        minCutDP(palabra)
        end = time.time()

        tiempo_B = end - start


        print(i, ": Tiempo A: ", tiempo_A, "seg\t Tiempo B:", tiempo_B)

        file.writelines(palabra + ';' + str(n) + ';' + str(tiempo_A) + ';' + str(tiempo_B) + '\n')

        i += 1


print("Archivo " + file_path + " Creado con Exito.")
