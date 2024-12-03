import os 

NOMBRE_ARCHIVO_CONFIGURACION = "Configuracion.txt"

def escribir_archivo_config (configuracion: dict):
    
    dir_path = os.path.dirname(os.path.realpath(__file__))

    archivo = open(dir_path + "\\" + NOMBRE_ARCHIVO_CONFIGURACION, "w")

    for clave, valor in configuracion.items():

        archivo.write(clave + ": " + str(valor))
        archivo.write("\n")

    archivo.close()

def leer_archivoo_config():

    dir_path = os.path.dirname(os.path.realpath(__file__))

    configuracion = {}

    if os.path.exists(dir_path + "\\" + NOMBRE_ARCHIVO_CONFIGURACION):
        archivo = open(dir_path + "\\" + NOMBRE_ARCHIVO_CONFIGURACION, "r")

        for linea in archivo:
                
                linea = linea.strip()

                if ": " in linea:
                    clave, valor = linea.split(": ", 1)
                    configuracion[clave] = valor

        archivo.close()

    return configuracion

# config = {"tipo_mira": 1,
#           "tamaño_mira": "grande",
#           "color": "negro"}

# escribir_archivo(config)

# config = leer_archivo()
# print(config)

