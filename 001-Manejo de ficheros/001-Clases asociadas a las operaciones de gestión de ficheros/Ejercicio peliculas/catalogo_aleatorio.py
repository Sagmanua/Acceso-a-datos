TAMANO_REGISTRO = 20
NOMBRE_FICHERO = "peliculas_aleatorio.txt"

def escribir_registros_tamano_fijo():
    titulos = ["Matrix", "Titanic", "Avatar", "Gladiator"]
    fichero = open(NOMBRE_FICHERO, "w", encoding="utf-8")
    for i in titulos:
        registro = i.ljust(TAMANO_REGISTRO - 1) + "\n"
        fichero.write(registro)
    fichero.close()

def leer_registro_directo(numero_registro):
    fichero = open(NOMBRE_FICHERO, "r", encoding="utf-8")
    posicion = numero_registro * TAMANO_REGISTRO
    fichero.seek(posicion)
    linea = fichero.readline()
    fichero.close()
    print(f"Registro {numero_registro}: {linea.strip()}")
    
def modificar_registro_directo(numero_registro, titulo_nuevo):
    fichero = open(NOMBRE_FICHERO, "r+", encoding="utf-8")
    posicion = numero_registro * TAMANO_REGISTRO
    fichero.seek(posicion)
    linea_nueva = titulo_nuevo.ljust(TAMANO_REGISTRO - 1) + "\n"
    fichero.write(linea_nueva)
    fichero.close()

def main():
    escribir_registros_tamano_fijo()
    
    print("Lectura directa del registro 2:")
    leer_registro_directo(2)
    
    print("\nModificando el registro 0 a 'Interstellar'")
    modificar_registro_directo(0, "Interstellar")

    print("\nComprobando todos los registros:")
    for i in range(4):
        leer_registro_directo(i)

if __name__ == "__main__":
    main()