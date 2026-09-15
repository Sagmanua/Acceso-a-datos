import struct

NOMBRE_FICHERO_TEXTO = "temperaturas.txt"
NOMBRE_FICHERO_TEXTO_NO_EX ="configuracion.txt "

NOMBRE_FICHERO_BINARIO = "contador.bin"



def escribir_temperaturas():

    flujo = open(NOMBRE_FICHERO_TEXTO, "w")
    flujo.write("18.5\n")
    flujo.write("21.0\n")
    flujo.write("19.2\n")
    flujo.close()


def leer_temperaturas():
    flujo = open(NOMBRE_FICHERO_TEXTO, "r")
    contenido = flujo.read()
    flujo.close
    print(contenido)


def saltar_primera_temperatura():
    flujo = open(NOMBRE_FICHERO_TEXTO, "r")
    flujo.readline()
    position = flujo.tell()
    flujo.seek(position)
    resto = flujo.read()        
    flujo.close()
    print(resto)





def comprobar_fichero_configuracion():
    try:
        flujo = open(NOMBRE_FICHERO_TEXTO_NO_EX, "r")
        flujo.close
    except FileNotFoundError:
        print(f"el fichero no existe")

def guardar_numero_registros():

    flujo = open(NOMBRE_FICHERO_TEXTO, "r")
    lineas = flujo.readlines()
    temperatura_deseada = float(lineas[2].strip())


    datos = struct.pack("f", temperatura_deseada)
    
    flujo_salida = open(NOMBRE_FICHERO_BINARIO, "wb")  # wb = write binary
    flujo_salida.write(datos)
    flujo_salida.close()

    flujo_entrada = open(NOMBRE_FICHERO_BINARIO, "rb")  # rb = read binary
    leido = flujo_entrada.read()
    flujo_entrada.close()

    temperatura_recuperada = struct.unpack("f", leido)[0]

    print(f"Bytes escritos:  {list(datos)}")
    print(f"Bytes leídos:    {list(leido)}")
    print(f"Como número: {temperatura_recuperada}")

 
def main():
    escribir_temperaturas()
    leer_temperaturas()
    saltar_primera_temperatura()
    comprobar_fichero_configuracion()
    guardar_numero_registros()


if __name__ == "__main__":
    main()