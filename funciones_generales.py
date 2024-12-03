import pygame
from archivo_puntuaciones import *
from archivo_configuraciones import *

def dibujar_texto(pantalla, texto, izq, arriba, fuente = "System", tamaño = 35, color = (0,0,0)):

    texto_renderizado = pygame.font.SysFont(fuente, tamaño).render(texto, True, color)
    rect_texto = texto_renderizado.get_rect(left=izq, top=arriba)  # Ajustar posición del texto
    pantalla.blit(texto_renderizado, rect_texto)

def guardar_configuracion(configuracion: dict):
    
    escribir_archivo_config(configuracion)

def obtener_configuracion():

    return leer_archivoo_config()

def guardar_puntaje(puntaje):

    escribir_archivo_puntuaciones(puntaje)

def obtener_puntuaiones_maximas():

    puntuaciones = leer_archivo_puntuaciones()

    lista_puntuaciones = puntuaciones.split("\n")

    for i in range(len(lista_puntuaciones)):

        if validar_numero(lista_puntuaciones[i]):
            lista_puntuaciones[i] = int(lista_puntuaciones[i])
        else:
            lista_puntuaciones[i] = 0

    lista_puntuaciones = bubble_sort_mayor_a_menor(lista_puntuaciones)

    return lista_puntuaciones


def validar_numero(cadena) -> bool:
    """
    Verifica una cadena es un numero
    cadena:  posible numero a validar
    Retorno: (bool) TRUE si es valido, FALSE si no lo es
    """
    retorno = True
    
    for caracter in cadena:
        if caracter < "0" or caracter > "9":
            retorno = False
            break
    
    if len(cadena) == 0:
        retorno = False

    return retorno

def bubble_sort_mayor_a_menor(lista):
    n = len(lista)
    for i in range(n):
        
        for j in range(0, n - i - 1):
            if lista[j] < lista[j + 1]:
                
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    
    return lista