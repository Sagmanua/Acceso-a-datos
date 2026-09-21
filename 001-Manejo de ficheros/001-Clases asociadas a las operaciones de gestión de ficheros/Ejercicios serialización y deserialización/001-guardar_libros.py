import json

NOMBRE_FICHERO = "biblioteca.dat"

def crear_lista_libros():
    libors = [
    {
        "titulo": "Harry Potter y la piedra filosofal",
        "autor": "J.K. Rowling",
        "anio": "1997",
        "paginas": "223"
    },
    {
            "titulo": "Cien años de soledad",
            "autor": "Gabriel García Márquez",
            "anio": "1967",
            "paginas": "471"
    },
    {
        "titulo": "1984",
        "autor": "George Orwell",
        "anio": "1949",
        "paginas": "328"
    }
    ]
    return libors


def serializar_libros(libors):
    print(libors)
    print(type(libors))
    cadena = json.dumps(libors)
    print(cadena)
    print(type(cadena))

    return cadena

def guardar_en_fichero(cadena):
    archivo = open("basededatos.dat", 'w')
    archivo.write(cadena)
    archivo.close()

    pass

def main():
    libros = crear_lista_libros()
    
    cadena_json = serializar_libros(libros)
    
    guardar_en_fichero(cadena_json)

    

if __name__ == "__main__":
    main()


