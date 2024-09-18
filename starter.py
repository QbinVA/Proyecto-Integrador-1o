#Importo pygame y sistema
import pygame, sys
#Importo la pantalla
import pygame.display
from pygame.locals import *
from button import Button
import constantes
import menuplay
from personaje import Personaje

#Inicializo pygame
pygame.init()

pantalla = pygame.display.set_mode((500, 750))
pygame.display.set_caption("Hungry Jump")

#Declaro e inserto el icono
icono = pygame.image.load("assets/images/items/banana0.png")
pygame.display.set_icon(icono)

menuBg = pygame.image.load("assets/images/fondos/menuBg.png")


def get_font(size):
    return pygame.font.Font("assets/Font/font.ttf", size)

def jugar():
    menuplay.play()

    
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        pantalla.fill("white")

        OPTIONS_TEXT = get_font(25).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(200, 300))
        pantalla.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(400, 600), 
                            text_input="BACK", font=get_font(25), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(pantalla)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    # Variables para el desplazamiento del fondo
    x = 0  # Posición inicial del fondo
    velocidad_fondo = 1  # Velocidad de desplazamiento del fondo

    # Carga la imagen con el nombre del juego
    titulo = pygame.image.load("assets/images/menu/Título.png")
    tituloS = pygame.transform.scale(titulo, (int(titulo.get_width() * 0.4), int(titulo.get_height() * 0.4)))  #Escala al 50%
    tituloPos = (45, 200)  # Posición en la pantalla

    while True:
        # Desplazamiento horizontal del fondo
        x -= velocidad_fondo  # Mueve el fondo hacia la izquierda

        # Calcula la posición relativa del fondo para hacer un bucle infinito
        x_relativa = x % menuBg.get_rect().width
        pantalla.blit(menuBg, (x_relativa - menuBg.get_rect().width, 0))
        pantalla.blit(menuBg, (x_relativa, 0))

        # Dibujar el titulo en pantalla
        pantalla.blit(tituloS, tituloPos)

        # Después de dibujar el fondo, ahora se dibujan los botones y el texto
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(25).render("", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(200, 300))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/images/menu/StartButton.png"), pos=(250, 530), 
                            text_input="", font=get_font(25), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/images/menu/Config.png"), pos=(410, 90), 
                            text_input="OPTIONS", font=get_font(25), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/images/menu/btnPausa.png"), pos=(90, 90), 
                            text_input="QUIT", font=get_font(25), base_color="#d7fcd4", hovering_color="White")

        pantalla.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(pantalla)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    jugar()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()