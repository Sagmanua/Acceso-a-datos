import os 

class Agenda:

    def __init__(self, archivo):
        self.archivo = archivo

    def guardar(self, nombre, telefono):
        f = open(self.archivo, "a")
        f.write(f"{nombre},{telefono}\n")
        f.close()  

    def leer(self):
        f = open(self.archivo, "r")
        for linea in f:
            datos = linea.strip().split(",")
            print(f"Name: {datos[0]} - Phone: {datos[1]}")
        f.close()  
        
print("--- MY ADDRESS BOOK ---")

mi_agenda = Agenda("agenda.csv")

mi_agenda.guardar("Marta", "611222333")
mi_agenda.guardar("Pablo", "622333444")
mi_agenda.guardar("Lucia", "633444555")

mi_agenda.leer()