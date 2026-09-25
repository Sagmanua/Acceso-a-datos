import os

def mostrar(carpeta, espacios):
    for nombre in sorted(os.listdir(carpeta)):
        print(f"{espacios},{nombre}")
        ruta = os.path.join(carpeta, nombre)
        if os.path.isdir(ruta):
            mostrar(ruta,espacios + "    ")



# Programa principal
print("--- MI MUSICA ---")

# 2. Create the folder structure
os.makedirs("mi_musica/rock/clasicos", exist_ok=True)
os.makedirs("mi_musica/pop", exist_ok=True)

# 3. Create three empty files
open("mi_musica/lista.txt", "w").close()
open("mi_musica/rock/clasicos/queen.mp3", "w").close()
open("mi_musica/pop/abba.mp3", "w").close()

# 4. Call mostrar() starting with the root folder and no initial spaces
mostrar("mi_musica", "")