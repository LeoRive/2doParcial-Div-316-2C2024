import pygame
import pygame.mixer as mixer_sonidos
from pygame.locals import *
from funciones_generales import *
import random
import time

mixer_sonidos.init()

TITULO_JUEGO = "El nuevo Fornite (con Patos)"

# COLORES!!!
NEGRO = (0, 0, 0)
VERDE = (0, 255, 0)
AMARILLO = (255, 255, 0)
BLANCO = (255, 255, 255)
AZUL = (0, 0, 255)
ROJO = (255, 0, 0)

#Imagenes

imagen_fondo_menu = pygame.image.load('Imagenes\\FondoJuegoCaceria.jpg')
imagen_mira_tipo_1_negra = pygame.image.load('Imagenes\\Black\\512\\15.png')
imagen_mira_tipo_2_negra = pygame.image.load('Imagenes\\Black\\512\\48.png')
imagen_mira_tipo_3_negra = pygame.image.load('Imagenes\\Black\\512\\8.png')
imagen_mira_tipo_1_blanca = pygame.image.load('Imagenes\\White\\512\\15.png')
imagen_mira_tipo_2_blanca = pygame.image.load('Imagenes\\White\\512\\48.png')
imagen_mira_tipo_3_blanca = pygame.image.load('Imagenes\\White\\512\\8.png')
imagen_pato = pygame.transform.scale(pygame.image.load('Imagenes\\pato_1.png'), (75,75))
fondo_menu = pygame.transform.scale(imagen_fondo_menu, (500, 500))
mira = pygame.transform.scale(imagen_mira_tipo_1_negra, (50, 50))

imagen_sonido_prendido = pygame.transform.scale(pygame.image.load('Imagenes\\unmute.png'), (35,35))
imagen_sonido_apagado = pygame.transform.scale(pygame.image.load('Imagenes\\mute.png'), (35,35))
imagen_sonido_actual = imagen_sonido_prendido

sonido_disparo = mixer_sonidos.Sound('Sonidos\\9-mm-gunshot.mp3')

#Rectangulos para eventos de click
rectanguloSonido = Rect(465, 0, 35, 35)


### Menú Principal
rectanguloSalirMenuPrincipal = Rect(400, 465, 100, 35)
rectConfMenuPrincipal = Rect(160, 250, 175, 35)
rectPuntuacionesMenuPrincipal = Rect(160, 350, 175, 35)
recJugarMenuPrincipal = Rect(175, 150, 145, 55)

###Puntuaciones
recSalirPuntuaciones = Rect(400, 465, 100, 35)

###Configuración
recSalirConfiguracion = Rect(400, 465, 100, 35)

rectTipo1Configuracion = Rect(130, 150, 100, 35)
rectTipo2Configuracion = Rect(240, 150, 100, 35)
rectTipo3Configuracion = Rect(350, 150, 100, 35)

rectTamañoChicoConfiguracion = Rect(130, 200, 100, 35)
rectTamañoMedianoConfiguracion = Rect(240, 200, 100, 35)
rectTamañoGrandeConfiguracion = Rect(350, 200, 100, 35)

rectColorBlancoConfiguracion = Rect(200, 250, 100, 35)
rectColorNegroConfiguracion = Rect(320, 250, 100, 35)

# configuracion = {
#     "tipo_mira": "tipo_1",
#     "tamaño_mira": "chico",
#     "color_mira": "negro",
# }

configuracion_mira = {"mira" : imagen_mira_tipo_1_negra}

###Juego
recSalirJuego = Rect(400, 465, 100, 35)

estadisticas = {
    "puntaje": 0,
    "cant_diparos": 0,
    "cant_exito": 0,
    "cant_perdidos": 0
}

lista_patos = []
tiempo_ultimo = time.time() #Se lo iba ausar para controlar la producción de patos (era la idea...)
velocidad = 5 

def punto_colicion_rectangulo(coordenada, rect):
    x, y = coordenada
    return x >= rect.left and x <= rect.right and y >= rect.top and y <= rect.bottom

def swichear_sonido():
    global imagen_sonido_actual
    if imagen_sonido_actual == imagen_sonido_prendido:
        imagen_sonido_actual = imagen_sonido_apagado
    else:
        imagen_sonido_actual = imagen_sonido_prendido

def control_menu(coordenadas):

    control_apretado = ""

    #Verificar si se sale
    if punto_colicion_rectangulo(coordenadas, rectanguloSalirMenuPrincipal):
        control_apretado = "Salir"
    elif punto_colicion_rectangulo(coordenadas, rectConfMenuPrincipal):
        control_apretado = "Configuracion"
    elif punto_colicion_rectangulo(coordenadas, rectPuntuacionesMenuPrincipal):
        control_apretado = "Puntuaciones"
    elif punto_colicion_rectangulo(coordenadas, recJugarMenuPrincipal):
        control_apretado = "Juego"
    elif punto_colicion_rectangulo(coordenadas, rectanguloSonido):
        swichear_sonido()
        control_apretado = "Sonido"

    return control_apretado

def limpiar_estadisticas():
    estadisticas["cant_diparos"] = 0
    estadisticas["cant_exito"] = 0
    estadisticas["cant_perdidos"] = 0
    estadisticas["puntaje"] = 0

def refrescar_configuracion(configuracion):

    configuracion_archivo = obtener_configuracion()

    if bool(configuracion_archivo):
        configuracion = configuracion_archivo
        configuracion["tipo_mira"] = configuracion_archivo["tipo_mira"]
        configuracion["tamaño_mira"] = configuracion_archivo["tamaño_mira"]
        configuracion["color_mira"] = configuracion_archivo["color_mira"]
    else: #Lo necesito repetir sino genera error de variable local
        configuracion = {
            "tipo_mira": "tipo_1",
            "tamaño_mira": "chico",
            "color_mira": "negro",
        }
    return configuracion

def mira_segun_configuracion(configuracion):

    # configuracion_archivo = obtener_configuracion()

    # if bool(configuracion_archivo):
    #     configuracion = configuracion_archivo
    # else: #Lo necesito repetir sino genera error de variable local
    #     configuracion = {
    #         "tipo_mira": "tipo_1",
    #         "tamaño_mira": "chico",
    #         "color_mira": "negro",
    #     }

    if configuracion["tipo_mira"] == "tipo_1":
        if configuracion["color_mira"] == "blanco":
            mira = imagen_mira_tipo_1_blanca
            
        else:
            mira = imagen_mira_tipo_1_negra
    elif configuracion["tipo_mira"] == "tipo_2":
        if configuracion["color_mira"] == "blanco":
            mira = imagen_mira_tipo_2_blanca
        else:
            mira = imagen_mira_tipo_2_negra
    elif configuracion["tipo_mira"] == "tipo_3":
        if configuracion["color_mira"] == "blanco":
            mira = imagen_mira_tipo_3_blanca
        else:
            mira = imagen_mira_tipo_3_negra
    else:
        mira = imagen_mira_tipo_1_negra
    
    if configuracion["tamaño_mira"] == "mediano":
        mira = pygame.transform.scale(mira, (75, 75))
    elif configuracion["tamaño_mira"] == "grande":
        mira = pygame.transform.scale(mira, (100, 100))
    else: 
        mira = pygame.transform.scale(mira, (50, 50))

    configuracion_mira["mira"] = mira

def control_configuraciones(coordenadas, configuracion):

    control_apretado = ""

    #Verificar si se sale
    if punto_colicion_rectangulo(coordenadas, recSalirConfiguracion):
        control_apretado = "Salir"
    elif punto_colicion_rectangulo(coordenadas, rectTipo1Configuracion):
        configuracion["tipo_mira"] = "tipo_1"
    elif punto_colicion_rectangulo(coordenadas, rectTipo2Configuracion):
        configuracion["tipo_mira"] = "tipo_2"
    elif punto_colicion_rectangulo(coordenadas, rectTipo3Configuracion):
        configuracion["tipo_mira"] = "tipo_3"
    elif punto_colicion_rectangulo(coordenadas, rectTamañoChicoConfiguracion):
        configuracion["tamaño_mira"] = "chico"
    elif punto_colicion_rectangulo(coordenadas, rectTamañoMedianoConfiguracion):
        configuracion["tamaño_mira"] = "mediano"
    elif punto_colicion_rectangulo(coordenadas, rectTamañoGrandeConfiguracion):
        configuracion["tamaño_mira"] = "grande"
    elif punto_colicion_rectangulo(coordenadas, rectColorNegroConfiguracion):
        configuracion["color_mira"] = "negro"
    elif punto_colicion_rectangulo(coordenadas, rectColorBlancoConfiguracion):
        configuracion["color_mira"] = "blanco"
    elif punto_colicion_rectangulo(coordenadas, rectanguloSonido):
        swichear_sonido()
        control_apretado = "Sonido"

    print(configuracion)
    guardar_configuracion(configuracion)

    return control_apretado

def control_puntuaciones(coordenadas):

    control_apretado = ""

    #Verificar si se sale
    if punto_colicion_rectangulo(coordenadas, recSalirPuntuaciones):
        control_apretado = "Salir"
    elif punto_colicion_rectangulo(coordenadas, rectanguloSonido):
        swichear_sonido()
        control_apretado = "Sonido"
    # elif punto_colicion_rectangulo(coordenadas, rectConfMenuPrincipal):
    #     control_apretado = "Configuracion"
    # elif punto_colicion_rectangulo(coordenadas, rectPuntuacionesMenuPrincipal):
    #     control_apretado = "Puntuaciones"

    return control_apretado

def control_juego(coordenadas):

    control_apretado = ""

    #Verificar si se sale
    if punto_colicion_rectangulo(coordenadas, recSalirJuego):
        control_apretado = "Salir"
        guardar_puntaje(estadisticas["puntaje"])
    elif punto_colicion_rectangulo(coordenadas, rectanguloSonido):
        swichear_sonido()
        control_apretado = "Sonido"      
    else:                
        ### PARTE DE LOS DISPAROS A PATOS!!!
        acerto_pato = False        
        for pato in lista_patos:
            if punto_colicion_rectangulo(coordenadas, pato):
                acerto_pato = True
                lista_patos.remove(pato)
        
        if acerto_pato:
            estadisticas["cant_exito"] = estadisticas["cant_exito"] + 1
            estadisticas["puntaje"] += 100
        else:
            estadisticas["cant_perdidos"] = estadisticas["cant_perdidos"] + 1
            if (estadisticas["puntaje"] - 50) < 0:
                estadisticas["puntaje"] = 0
            else:
                estadisticas["puntaje"] -= 50

        estadisticas["cant_diparos"] = estadisticas["cant_diparos"] + 1
        print(estadisticas["puntaje"])
        sonido_disparo.play()

    return control_apretado

def dibujar_menu(pantalla):

    pantalla.blit(fondo_menu, (0, 0))

    ##### TITULO DE LA PÄRTE DE ARRIBA
    # Dibujar el fondo del cuadro
    # rectangulo = Rect(150, 50, 210, 35)
    # pygame.draw.rect(pantalla, NEGRO, rectangulo)
    # pygame.draw.rect(pantalla, ROJO, rectangulo, 1)

    # Dibujar el texto
    dibujar_texto(pantalla, TITULO_JUEGO, 50, 50, color=ROJO, fuente= "Times New Roman")

    ##### BOTON JUGAR
    # Dibujar el fondo del cuadro
    recJugarMenuPrincipal = Rect(175, 150, 145, 55)
    # pygame.draw.rect(pantalla, NEGRO, recJugarMenuPrincipal)
    # pygame.draw.rect(pantalla, ROJO, recJugarMenuPrincipal, 1)

    # Dibujar el texto
    dibujar_texto(pantalla, "Jugar", 175, 150, color=ROJO, tamaño=75)
    # texto_renderizado = pygame.font.SysFont('System', 35).render("Jugar", True, BLANCO)
    # rect_texto = texto_renderizado.get_rect(left=50, top=100)  # Ajustar posición del texto
    # pantalla.blit(texto_renderizado, rect_texto)

    ##### BOTON CONFIGURACION
    
    # pygame.draw.rect(pantalla, NEGRO, rectConfMenuPrincipal)
    # pygame.draw.rect(pantalla, ROJO, rectConfMenuPrincipal, 1)

    # Dibujar el texto
    dibujar_texto(pantalla, "Configuración", 160, 250, color=BLANCO)

    ##### BOTON PUNTUCAIONES
    rectPuntuacionesMenuPrincipal = Rect(160, 350, 175, 35)
    # pygame.draw.rect(pantalla, NEGRO, rectPuntuacionesMenuPrincipal)
    # pygame.draw.rect(pantalla, ROJO, rectPuntuacionesMenuPrincipal, 1)

    # Dibujar el texto
    dibujar_texto(pantalla, "Puntuaciones", 160, 350, color=BLANCO)

    ##### BOTON SALIR
    #pygame.draw.rect(pantalla, NEGRO, rectanguloSalirMenuPrincipal)
    #pygame.draw.rect(pantalla, ROJO, rectanguloSalirMenuPrincipal, 1)

    #Boton sonido
    # pygame.draw.rect(pantalla, NEGRO, rectanguloSonido)
    # pygame.draw.rect(pantalla, ROJO, rectanguloSonido, 1)
    pantalla.blit(imagen_sonido_actual, (465, 0))

    # Dibujar el texto
    dibujar_texto(pantalla, "Salir", 400, 465, color=BLANCO)

    pygame.display.flip() #Muestro la pantalla

def dibujar_puntuaciones(pantalla):

    pantalla.blit(fondo_menu, (0, 0))

    ##### TITULO DE LA PÄRTE DE ARRIBA
    # Dibujar el fondo del cuadro
    # rectangulo = Rect(150, 50, 210, 35)
    # pygame.draw.rect(pantalla, NEGRO, rectangulo)
    # pygame.draw.rect(pantalla, ROJO, rectangulo, 1)

    # Dibujar el texto
    dibujar_texto(pantalla, TITULO_JUEGO, 50, 50, color=ROJO, fuente= "Times New Roman")

    ##### Titulo Puntuaciones
    # # Dibujar el fondo del cuadro
    # rectangulo = Rect(150, 100, 210, 35)
    # pygame.draw.rect(pantalla, NEGRO, rectangulo)
    # pygame.draw.rect(pantalla, ROJO, rectangulo, 1)

    # # Dibujar el texto
    # dibujar_texto(pantalla, "Puntuaciones", 150, 100, color=BLANCO)

    ##### PUNTAJES
    ### Muestra los tres mejores puntajes

    listado_puntajes = obtener_puntuaiones_maximas()
    
    contador = 0
    altura = 170

    for puntaje in listado_puntajes:
        altura += 50
        contador = contador + 1
        if contador == 4:
            break
        elif contador == 1:

            dibujar_texto(pantalla, "MEJOR PUNTAJE:", 150, altura, color=BLANCO)
            altura += 50
            dibujar_texto(pantalla, str(puntaje), 220, altura, color=BLANCO)
            
        else:
            dibujar_texto(pantalla, "Puntaje: ", 150, altura, color=BLANCO)
            dibujar_texto(pantalla, str(puntaje), 300, altura, color=BLANCO)
        
        

    ##### BOTON SALIR
    #pygame.draw.rect(pantalla, NEGRO, recSalirPuntuaciones)
    #pygame.draw.rect(pantalla, ROJO, recSalirPuntuaciones, 1)
    
    #Boton sonido
    # pygame.draw.rect(pantalla, NEGRO, rectanguloSonido)
    # pygame.draw.rect(pantalla, ROJO, rectanguloSonido, 1)
    pantalla.blit(imagen_sonido_actual, (465, 0))

    # Dibujar el texto
    dibujar_texto(pantalla, "Salir", 400, 465, color=BLANCO)

    pygame.display.flip() #Muestro la pantalla

def dibujar_configuracion(pantalla, configuracion):

    pantalla.blit(fondo_menu, (0, 0))

    ##### TITULO DE LA PÄRTE DE ARRIBA
    # Dibujar el fondo del cuadro
    # rectangulo = Rect(150, 50, 210, 35)
    # pygame.draw.rect(pantalla, NEGRO, rectangulo)
    # pygame.draw.rect(pantalla, ROJO, rectangulo, 1)

    # Dibujar el texto
    dibujar_texto(pantalla, TITULO_JUEGO, 50, 50, color=ROJO, fuente= "Times New Roman")

    ##### Titulo configuracion
    # Dibujar el fondo del cuadro
    # rectangulo = Rect(150, 100, 210, 35)
    # pygame.draw.rect(pantalla, NEGRO, rectangulo)
    # pygame.draw.rect(pantalla, ROJO, rectangulo, 1)

    # # Dibujar el texto
    # dibujar_texto(pantalla, "Configuracion", 150, 100, color=BLANCO)

    ### CONFIGURACIONES
    dibujar_texto(pantalla, "Tipo Mira", 5, 150, color=NEGRO)

    #Colores para marcar las configuraciones seleccionadas
    color_tipo1 = ROJO
    color_tipo2 = ROJO
    color_tipo3 = ROJO
    color_chico = ROJO
    color_mediano = ROJO
    color_grande = ROJO
    color_negro = ROJO
    color_blanco = ROJO

    if configuracion["tipo_mira"] == "tipo_1":
        color_tipo1 = VERDE
    if configuracion["tipo_mira"] == "tipo_2":
        color_tipo2 = VERDE
    if configuracion["tipo_mira"] == "tipo_3":
        color_tipo3 = VERDE

    if configuracion["tamaño_mira"] == "chico":
        color_chico = VERDE
    if configuracion["tamaño_mira"] == "mediano":
        color_mediano = VERDE
    if configuracion["tamaño_mira"] == "grande":
        color_grande = VERDE

    if configuracion["color_mira"] == "negro":
        color_negro = VERDE
    if configuracion["color_mira"] == "blanco":
        color_blanco = VERDE

    #pygame.draw.rect(pantalla, NEGRO, rectTipo1Configuracion)
    pygame.draw.rect(pantalla, color_tipo1, rectTipo1Configuracion, 1)
    dibujar_texto(pantalla, "Tipo 1", rectTipo1Configuracion.left, rectTipo1Configuracion.top, color=NEGRO)

    #pygame.draw.rect(pantalla, NEGRO, rectTipo2Configuracion)
    pygame.draw.rect(pantalla, color_tipo2, rectTipo2Configuracion, 1)
    dibujar_texto(pantalla, "Tipo 2", rectTipo2Configuracion.left, rectTipo2Configuracion.top, color=NEGRO)

    #pygame.draw.rect(pantalla, NEGRO, rectTipo3Configuracion)
    pygame.draw.rect(pantalla, color_tipo3, rectTipo3Configuracion, 1)
    dibujar_texto(pantalla, "Tipo 3", rectTipo3Configuracion.left, rectTipo3Configuracion.top, color=NEGRO)

    dibujar_texto(pantalla, "Tamaño", 5, 200, color=NEGRO)

    #pygame.draw.rect(pantalla, NEGRO, rectTamañoChicoConfiguracion)
    pygame.draw.rect(pantalla, color_chico, rectTamañoChicoConfiguracion, 1)
    dibujar_texto(pantalla, "Chico", rectTamañoChicoConfiguracion.left, rectTamañoChicoConfiguracion.top, color=NEGRO)

    #pygame.draw.rect(pantalla, NEGRO, rectTamañoMedianoConfiguracion)
    pygame.draw.rect(pantalla, color_mediano, rectTamañoMedianoConfiguracion, 1)
    dibujar_texto(pantalla, "Mediano", rectTamañoMedianoConfiguracion.left, rectTamañoMedianoConfiguracion.top, color=NEGRO)

    #pygame.draw.rect(pantalla, NEGRO, rectTamañoGrandeConfiguracion)
    pygame.draw.rect(pantalla, color_grande, rectTamañoGrandeConfiguracion, 1)
    dibujar_texto(pantalla, "Grande", rectTamañoGrandeConfiguracion.left, rectTamañoGrandeConfiguracion.top, color=NEGRO)

    dibujar_texto(pantalla, "Color", 5, 250, color=NEGRO)

    #pygame.draw.rect(pantalla, NEGRO, rectColorNegroConfiguracion)
    pygame.draw.rect(pantalla, color_negro, rectColorNegroConfiguracion, 1)
    dibujar_texto(pantalla, "Negro", rectColorNegroConfiguracion.left, rectColorNegroConfiguracion.top, color=NEGRO)

    #pygame.draw.rect(pantalla, NEGRO, rectColorBlancoConfiguracion)
    pygame.draw.rect(pantalla, color_blanco, rectColorBlancoConfiguracion, 1)
    dibujar_texto(pantalla, "Blanco", rectColorBlancoConfiguracion.left, rectColorBlancoConfiguracion.top, color=NEGRO)

    #Boton sonido
    # pygame.draw.rect(pantalla, NEGRO, rectanguloSonido)
    # pygame.draw.rect(pantalla, ROJO, rectanguloSonido, 1)
    pantalla.blit(imagen_sonido_actual, (465, 0))

    ##### BOTON SALIR 
    #pygame.draw.rect(pantalla, NEGRO, recSalirConfiguracion)
    #pygame.draw.rect(pantalla, ROJO, recSalirConfiguracion, 1)

    # Dibujar el texto
    dibujar_texto(pantalla, "Salir", 400, 465, color=BLANCO)

    pygame.display.flip() #Muestro la pantalla

def ingresar_juego(pantalla):

    pantalla.blit(fondo_menu, (0, 0))

    actualizar_diana(pantalla) #Se hace aca, para que el pato no "parpadee", y la mira este como fija

    dibujar_texto(pantalla, "Puntaje", 5, 5, color=BLANCO)
    dibujar_texto(pantalla, str(estadisticas["puntaje"]), 100, 5, color=BLANCO)
    
    pygame.mouse.set_visible(False)
    cursor_img_rect = configuracion_mira["mira"].get_rect() #cursor_img_rect = mira.get_rect()
    cursor_img_rect.center = pygame.mouse.get_pos()  
    pantalla.blit(configuracion_mira["mira"], cursor_img_rect)  #pantalla.blit(mira, cursor_img_rect) 
    
    #Boton sonido
    # pygame.draw.rect(pantalla, NEGRO, rectanguloSonido)
    # pygame.draw.rect(pantalla, ROJO, rectanguloSonido, 1)
    pantalla.blit(imagen_sonido_actual, (465, 0))

    ##### BOTON SALIR
    #pygame.draw.rect(pantalla, NEGRO, recSalirJuego)
    #pygame.draw.rect(pantalla, ROJO, recSalirJuego, 1)

    # Dibujar el texto
    dibujar_texto(pantalla, "Salir", 400, 465, color=BLANCO)

    pygame.display.flip() 

def actualizar_diana(pantalla):
    
    #if time.time() - tiempo_ultimo >= 5:
    if len(lista_patos) == 0:
        
        # Altura aleatoria netre el tamaño fijo de pantalla y la altura de pato
        nueva_imagen = Rect(0, random.randint(0, 500 - 70), 75, 75)
        
        lista_patos.append(nueva_imagen)
        #tiempo_ultimo = time.time()

    mover_patos()

    for un_pato in lista_patos:
        #pantalla.blit(imagen_pato, (un_pato['x'], un_pato['y']))
        pantalla.blit(imagen_pato, (un_pato.left, un_pato.top))

    pygame.display.flip()

def mover_patos():
    for un_pato in lista_patos[:]:
        un_pato.left += velocidad
        if un_pato.left > 500:  # <========= ACA SALE DE LA PANTALLA!!! ACAAAAAA!!!!
            lista_patos.remove(un_pato)

