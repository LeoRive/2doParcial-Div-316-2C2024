import pygame
import pygame.mixer as mixer
from funciones_principales import *
from pygame.locals import *


ANCHO_VENTANA = 500
ALTO_VENTANA = 500
ESCENARIO = "Menu Principal"

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

pygame.init()
mixer.init()
pantalla = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.display.set_caption(TITULO_JUEGO)

mixer.music.load("Sonidos\\summer-mix-243341.mp3")
mixer.music.play(-1) #Se escucha todo el tiempo

#Creo un reloj que regule la tasa de imagenes por segundo (FPS)
clock = pygame.time.Clock()

#TUVE QUE LLEVAR ESTA CONFIGURACIÖN ACÁ PROQUE NUNCA SE REFRESCABA
configuracion = {
    "tipo_mira": "tipo_1",
    "tamaño_mira": "chico",
    "color_mira": "negro",
}

segundos = 0
flag_correr = True
while flag_correr:
    clock.tick(60)

    if ESCENARIO == 'Menu Principal':
        dibujar_menu(pantalla)
    elif ESCENARIO == 'Configuracion':
        dibujar_configuracion(pantalla, configuracion)
    elif ESCENARIO == 'Puntuaciones':
        dibujar_puntuaciones(pantalla)
    elif ESCENARIO == 'Juego':
        ingresar_juego(pantalla)

    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag_correr = False

        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            #print(evento.pos)
            coordenada_click = evento.pos

            if ESCENARIO == 'Menu Principal':
                control_apretado = control_menu(coordenada_click)

                if control_apretado == "Salir":
                     flag_correr = False
                elif control_apretado == "Configuracion":
                    configuracion = refrescar_configuracion(configuracion)
                    ESCENARIO = 'Configuracion'
                elif control_apretado == "Puntuaciones":
                    ESCENARIO = 'Puntuaciones'
                elif control_apretado == "Juego":
                    configuracion = refrescar_configuracion(configuracion)
                    limpiar_estadisticas() #Limpia las estadisticas para que se sumen
                    mira_segun_configuracion(configuracion) #Configura la mira para que esté acorde a lo configurado
                    ESCENARIO = 'Juego'
                elif control_apretado == "Sonido":
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.stop()
                    else:
                        pygame.mixer.music.play(-1)
            
            elif ESCENARIO == "Configuracion":
                 control_apretado = control_configuraciones(coordenada_click, configuracion)

                 if control_apretado == "Salir":
                    ESCENARIO = 'Menu Principal'
                 elif control_apretado == "Sonido":
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.stop()
                    else:
                        pygame.mixer.music.play(-1)

            elif ESCENARIO == "Puntuaciones":
                 control_apretado = control_puntuaciones(coordenada_click)

                 if control_apretado == "Salir":
                    ESCENARIO = 'Menu Principal'
                 elif control_apretado == "Sonido":
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.stop()
                    else:
                        pygame.mixer.music.play(-1)
            
            elif ESCENARIO == "Juego":
                 
                 control_apretado = control_juego(coordenada_click)

                 if control_apretado == "Salir":

                    ESCENARIO = 'Menu Principal'
                    pygame.mouse.set_visible(True)
                 elif control_apretado == "Sonido":
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.stop()
                    else:
                        pygame.mixer.music.play(-1)
                 



            # lista_posicion = list(evento.pos) #guardo la pos del click en una lista
            # #print(lista_posicion)
            # rect_rana[0] = lista_posicion[0] #modifico el left del rect
            # rect_rana[1] = lista_posicion[1] #modifico el top del rect
            #print(rect_rana)

#     pantalla.fill((0,0,128))
#     #RANA-dibujar el rectangulo para ver cuanto ocupa
#     pygame.draw.rect(pantalla, (255,0,0),rect_rana)
#     pantalla.blit(imagen_rana,rect_rana) #fundir la imagen en la ventana

#     if rect_rana.colliderect(rect_mosca):
#         flag_viva = False

#     if flag_viva:
#         #MOSCA-dibujar el rectangulo para ver cuanto ocupa
#         pygame.draw.rect(pantalla, (255,0,0),rect_mosca)
#         pantalla.blit(imagen_mosca,rect_mosca) #fundir la imagen en la ventana

#     #mostrar los cambios de la pantalla
#     pygame.display.flip()

pygame.quit()