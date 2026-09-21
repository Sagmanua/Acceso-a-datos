TAMANO_REGISTRO = 20

def escribir_registros_tamano_fijo():
    titulos = ["MAtrix","titanic","Avatar","Galdiator"]
    fichero = open("peliculas_aletorio.txt", "w", encoding="utf-8")
    for i in titulos:
        registro = i.ljust(TAMANO_REGISTRO - 1) + "\n"
        fichero.write(registro)
    fichero.close

    pass
def leer_registro_directo(numero_registro):
    fichero = open("peliculas_aletorio.txt", "w", encoding="utf-8")

    pass
def modificar_registro_directo(numero_registro, titulo_nuevo):
    pass

def main():
    pass

if __name__ == "__main__":
    main()