def escribir_varias_peliculas():
    peliculas = ["Matrix,148\n", "Titanic,195\n", "Avatar,162\n"]
    fichero = open("peliculas_secuencial.txt", "w", encoding="utf-8")
    fichero.writelines(peliculas)
    fichero.close()


def anadir_una_pelicula():
    fichero = open("peliculas_secuencial.txt", "a", encoding="utf-8")
    fichero.writelines("Gladiator,155\n")

def leer_todo_de_golpe():
    fichero = open("peliculas_secuencial.txt", "r", encoding="utf-8")
    contenido = fichero.read()
    fichero.close()
    print(contenido)


def leer_linea_a_linea():
    fichero = open("peliculas_secuencial.txt", "r", encoding="utf-8")

    linea = fichero.readline()

    while linea !="":
        print(linea.strip())
        linea = fichero.readline()

    fichero.close()


def main():
    escribir_varias_peliculas()
    anadir_una_pelicula()
    leer_todo_de_golpe()
    leer_linea_a_linea()



if __name__ == "__main__":
    main()