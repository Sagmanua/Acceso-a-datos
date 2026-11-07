import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="accesoadatos2526",
    password="Accesoadatos2526$",
    database="accesoadatos2526"
)

cursor = conexion.cursor()

sql = "INSERT INTO clientes (Identificador, nombre, apellidos, correo) VALUES (%s, %s, %s, %s)"
valores = (None, "Ana", "Martinez Ruiz", "ana@martinezruiz.com")

cursor.execute(sql, valores)
conexion.commit()

cursor.close()
conexion.close()