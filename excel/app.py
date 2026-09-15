"""
Gestor de contactos
-------------------
Lee datos.csv, los convierte en una lista de diccionarios,
los guarda en contactos.json, escribe un log.txt con una línea
por contacto procesado, y al final cuenta cuántas líneas tiene
ese log.txt.
"""

import csv
import json


def leer_csv(ruta_csv):
    """Paso 1 y 2: lee el CSV y devuelve una lista de diccionarios."""
    contactos = []

    with open(ruta_csv, mode="r", encoding="utf-8-sig", newline="") as archivo_csv:
        lector = csv.DictReader(archivo_csv, delimiter=";")  # ya usa la primera fila como claves

        for fila in lector:
            contacto = {
                "Column1": fila["Column1"],
                "Column2": fila["Column2"],
                "Column3": fila["Column3"],
                "Column4": fila["Column4"],
                "Column5": fila["Column5"],
                "Column6": fila["Column6"],
                "Column7": fila["Column7"],
                "Column8": fila["Column8"],
                "Column9": fila["Column9"],
                "Column10": fila["Column10"],
                "Column11": fila["Column11"],
            }
            contactos.append(contacto)

    return contactos



def guardar_json(contactos, ruta_json):
    """Paso 3: guarda la lista de diccionarios en un archivo JSON legible."""
    with open(ruta_json, mode="w", encoding="utf-8") as archivo_json:
        json.dump(contactos, archivo_json, indent=4, ensure_ascii=False)


def escribir_log(contactos, ruta_log):
    """Paso 4: escribe una línea de log por cada contacto procesado."""
    with open(ruta_log, mode="w", encoding="utf-8") as archivo_log:
        for contacto in contactos:
            linea = f"{contacto['Column1']} {contacto['Column2']} {contacto['Column3']} {contacto['Column4']}{contacto['Column5']}{contacto['Column6']} {contacto['Column7']} {contacto['Column8']} {contacto['Column9']} {contacto['Column10']} {contacto['Column11']}\n"
            archivo_log.write(linea)


def contar_lineas_log(ruta_log):
    """Paso 5: abre el log.txt y cuenta cuántas líneas (contactos) tiene."""
    with open(ruta_log, mode="r", encoding="utf-8") as archivo_log:
        lineas = archivo_log.readlines()
    return len(lineas)


def main():
    ruta_csv = "Nasa_page.csv"
    ruta_json = "contactos.json"
    ruta_log = "log.txt"

    # 1 y 2. Leer el CSV y convertir cada fila en un diccionario
    contactos = leer_csv(ruta_csv)
    print(f"Se han leído {len(contactos)} contactos desde '{ruta_csv}'.")

    # 3. Guardar todos los contactos en contactos.json
    guardar_json(contactos, ruta_json)
    print(f"Contactos guardados en '{ruta_json}'.")

    # 4. Escribir log.txt con una línea por contacto
    escribir_log(contactos, ruta_log)
    print(f"Registro de actividad escrito en '{ruta_log}'.")

    # 5. Leer log.txt y mostrar cuántas líneas (contactos) se han procesado
    total = contar_lineas_log(ruta_log)
    print(f"\nTotal de contactos procesados según el log: {total}")


if __name__ == "__main__":
    main()