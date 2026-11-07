import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="accesoadatos2526",
    password="Accesoadatos2526$",
    database="accesoadatos2526"
)

cursor = conexion.cursor()

sql = "DELETE FROM clientes WHERE Identificador = %s"
valores = (4,)

cursor.execute(sql, valores)
conexion.commit()

cursor.close()
conexion.close()