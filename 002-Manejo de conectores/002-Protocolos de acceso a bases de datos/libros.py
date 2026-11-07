import mysql.connector

libros = [
    {
        "titulo": "Don Quijote",
        "paginas": 863,
        "generos": ["novela", "aventuras", "humor"],
    },
    {"titulo": "Platero y yo", "paginas": 144, "generos": ["poesía", "infantil"]},
    {"titulo": "Marianela", "paginas": 256, "generos": ["novela"]},
]

conn = mysql.connector.connect(
    host="localhost", user="desfase", password="desfase", database="desfase"
)
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS libros_generos")
cursor.execute("DROP TABLE IF EXISTS libros")

cursor.execute("""
    CREATE TABLE libros (
        Identificador INT AUTO_INCREMENT PRIMARY KEY,
        titulo VARCHAR(255),
        paginas INT
    )
""")

cursor.execute("""
    CREATE TABLE libros_generos (
        Identificador INT AUTO_INCREMENT PRIMARY KEY,
        libros_id INT,
        valor VARCHAR(255),
        FOREIGN KEY (libros_id) REFERENCES libros(Identificador)
    )
""")

for libro in libros:
  cursor.execute(
      "INSERT INTO libros (titulo, paginas) VALUES (%s, %s)",
      (libro["titulo"], libro["paginas"]),
  )
  id_libro = cursor.lastrowid

  for genero in libro["generos"]:
    cursor.execute(
        "INSERT INTO libros_generos (libros_id, valor) VALUES (%s, %s)",
        (id_libro, genero),
    )

conn.commit()

recuperados = []

cursor.execute("SELECT Identificador, titulo, paginas FROM libros")
filas_libros = cursor.fetchall()

for fila_libro in filas_libros:
  id_libro = fila_libro[0]
  titulo = fila_libro[1]
  paginas = fila_libro[2]

  cursor.execute(
      "SELECT valor FROM libros_generos WHERE libros_id = %s", (id_libro,)
  )
  filas_generos = cursor.fetchall()

  lista_generos = []
  for g in filas_generos:
    lista_generos.append(g[0])

  fichas_libro = {
      "titulo": titulo,
      "paginas": paginas,
      "generos": lista_generos,
  }
  recuperados.append(fichas_libro)

print("Lista de libros recuperados:")
print(recuperados)
print("¿Son idénticas las listas?:", recuperados == libros)

print("\n--- Libros que son novelas ---")
cursor.execute(
    """
    SELECT libros.titulo 
    FROM libros 
    JOIN libros_generos ON libros.Identificador = libros_generos.libros_id 
    WHERE libros_generos.valor = %s
""",
    ("novela",),
)

novelas = cursor.fetchall()
for n in novelas:
  print(n[0])

cursor.close()
conn.close()