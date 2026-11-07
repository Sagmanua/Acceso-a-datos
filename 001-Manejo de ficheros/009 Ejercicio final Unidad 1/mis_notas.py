# mis_notas.py
# Mi cuaderno de notas: repaso de todo lo visto con ficheros.

# Módulos que vamos a necesitar
import csv      # para leer ficheros CSV (paso 6)
import json     # para serializar y deserializar (pasos 7 y 8)
import os       # para ver los ficheros de la carpeta (paso 11)

# Nombres de los ficheros (en MAYÚSCULAS porque no cambian nunca)
NOMBRE_NOTAS = "notas.csv"
NOMBRE_JSON = "notas.json"
NOMBRE_BINARIO = "total.bin"

# AQUÍ IRÁS PEGANDO LAS FUNCIONES DE CADA PASO (una debajo de otra)

# Paso 1: Crear el fichero de notas
def crear_fichero_notas():
    # 1. Lista con las tres líneas (fíjate en el \n del final de cada una)
    lineas = ["Ana,8\n", "Luis,6\n", "Marta,9\n"]
    # 2. Abre NOMBRE_NOTAS en modo escritura
    fichero = open(NOMBRE_NOTAS, "w")
    # 3. Escribe la lista entera de golpe
    fichero.writelines(lineas)
    # 4. Cierra el fichero
    fichero.close()
    print("Fichero", NOMBRE_NOTAS, "creado con 3 alumnos.")

# Paso 2: La clase Cuaderno: añadir alumnos
class Cuaderno:
    # Constructor: se ejecuta al crear el objeto
    def __init__(self, archivo):
        # Guarda el nombre del archivo dentro del objeto
        self.archivo = archivo

    # Añade UN alumno al final del archivo, sin borrar lo que había
    def anadir(self, nombre, nota):
        # 1. Abre self.archivo en modo añadir
        fichero = open(self.archivo, "a")
        # 2. Escribe nombre, coma, nota (como texto) y salto de línea
        fichero.write(nombre + "," + str(nota) + "\n")
        # 3. Cierra el fichero
        fichero.close()
        print("Añadido:", nombre, "con un", nota)

# Paso 3: Leer todo el fichero de golpe
def leer_todo():
    # 1. Abre NOMBRE_NOTAS en modo lectura
    fichero = open(NOMBRE_NOTAS, "r")
    # 2. Lee TODO el contenido de una vez
    contenido = fichero.read()
    # 3. Cierra el fichero y muestra lo leído
    fichero.close()
    print(contenido)

# Paso 4: Leer línea a línea
def leer_linea_a