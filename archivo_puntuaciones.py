import os 

NOMBRE_ARCHIVO_PUNTAJE = "Puntaje.csv"

def escribir_archivo_puntuaciones (puntaje):
    
    dir_path = os.path.dirname(os.path.realpath(__file__))

    archivo = open(dir_path + "\\" + NOMBRE_ARCHIVO_PUNTAJE, "a")

    archivo.write(str(puntaje))
    archivo.write("\n")

    archivo.close()

def leer_archivo_puntuaciones():

    puntajes = "0"
    
    dir_path = os.path.dirname(os.path.realpath(__file__))
    if os.path.exists(dir_path + "\\" + NOMBRE_ARCHIVO_PUNTAJE):    

        archivo = open(dir_path + "\\" + NOMBRE_ARCHIVO_PUNTAJE, "r")

        puntajes = archivo.read()

        archivo.close()

    return puntajes

# escribir_archivo(1223)
# escribir_archivo(987)
# escribir_archivo(123)

# lectura = leer_archivo()
# print(lectura)