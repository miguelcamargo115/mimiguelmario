
import pygame
from pygame.locals import *
import os
import sys

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
IMG_DIR = "images"


def load_image(nombre, dir_imagen, alpha=False):
    
    ruta = os.path.join(dir_imagen, nombre)
    try:
        image = pygame.image.load(ruta)
    except:
        print("Error, no se puede cargar la imagen: " + ruta)
        sys.exit(1)
   
    if alpha is True:
        image = image.convert_alpha()
    else:
        image = image.convert()
    return image


# ------------------------------
# Funcion principal del juego
# ------------------------------


def main():
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Ejemplo de un Pong Simple")

    # cargamos el fondo
    fondo = load_image("imagenbrawl.jpg", IMG_DIR, alpha=False)

    # el bucle principal del juego
    while True:
        # actualizamos la pantalla
        screen.blit(fondo, (0, 0))
        pygame.display.flip()

        # Posibles entradas del teclado y mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


if __name__ == "__main__":
    main()



    #Se ejecuta desde abajo con python3 main.py
    