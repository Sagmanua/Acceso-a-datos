import json

def leer_fichero():
    archivo = open("basededatos.dat", 'r')
    linea = archivo.readlines()[0]
    archivo.close()

    return linea


def deserializar_libros(linea):
    devuelta = json.loads(linea)
    print(devuelta)
    print(type(devuelta))

def main():
    contenido_linea = leer_fichero()
    deserializar_libros(contenido_linea)

if __name__ == "__main__":
    main()

