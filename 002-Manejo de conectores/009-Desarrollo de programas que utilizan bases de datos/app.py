import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234"
)

cursor = conexion.cursor()
print("Conexión correcta con MySQL")

cursor.execute("CREATE DATABASE IF NOT EXISTS tienda")

cursor.execute("SHOW DATABASES")
for base in cursor:
    print(base[0])

cursor.execute("USE tienda")

cursor.execute("DROP TABLE IF EXISTS productos")

cursor.execute("""
    CREATE TABLE productos (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(50),
        precio DECIMAL(6,2)
    )
""")

cursor.execute("SHOW TABLES")
for tabla in cursor:
    print(f"Tabla creada: {tabla[0]}")

sql_insert = "INSERT INTO productos (nombre, precio) VALUES (%s, %s)"
datos = [
    ("Teclado", 25),
    ("Raton", 12.5),
    ("Monitor", 140),
    ("Altavoces", 30)
]

cursor.executemany(sql_insert, datos)
conexion.commit()
print(f"{cursor.rowcount} filas insertadas")

print("--- Todos los productos ---")
cursor.execute("SELECT * FROM productos")
for fila in cursor.fetchall():
    print(f"{fila[0]} | {fila[1]} | {fila[2]:.2f}")

print("--- Productos de menos de 30 euros ---")
sql_where = "SELECT nombre, precio FROM productos WHERE precio < %s"
cursor.execute(sql_where, (30,))
for fila in cursor:
    print(f"{fila[0]} | {fila[1]:.2f}")

sql_update = "UPDATE productos SET precio = %s WHERE nombre = %s"
cursor.execute(sql_update, (120, "Monitor"))
print(f"Filas modificadas: {cursor.rowcount}")

sql_delete = "DELETE FROM productos WHERE nombre = %s"
cursor.execute(sql_delete, ("Raton",))
print(f"Filas borradas: {cursor.rowcount}")

conexion.commit()

print("--- Productos después de los cambios ---")
cursor.execute("SELECT * FROM productos")
for fila in cursor.fetchall():
    print(f"{fila[0]} | {fila[1]} | {fila[2]:.2f}")

cursor.close()
conexion.close()
print("Conexión cerrada")