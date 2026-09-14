import csv
import json


#Road 

ruta_csv = "datos.csv"
ruta_json = "contactos.json"
ruta_log = "log.txt"


#Save information 
contactos = []

with open(ruta_csv, mode="r", encoding="utf-8", newline="") as archivo_csv:
    lector = csv.DictReader(archivo_csv) 

    for fila in lector:
        contacto = {
            "nombre": fila["nombre"],
            "apellidos": fila["apellidos"],
            "telefono": fila["telefono"],
        }
        contactos.append(contacto)




with open(ruta_json, mode="w", encoding="utf-8") as archivo_json:
    json.dump(contactos, archivo_json, indent=4, ensure_ascii=False)

with open(ruta_log, mode="w", encoding="utf-8") as archivo_log:
    for contacto in contactos:
        linea = f"Contacto añadido: {contacto['nombre']} {contacto['apellidos']}\n"
        archivo_log.write(linea)


print(f"Se han leído {len(contactos)} contactos desde '{ruta_csv}'.")