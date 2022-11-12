import numpy as np
import pygame
import time
from variables import *

pygame.init()

# Ancho y alto de la ventana
screen = pygame.display.set_mode((width, height))

# Colores
screen.fill(bg)

# Automata palo
gameState[5, 3] = 1
gameState[5, 4] = 1
gameState[5, 5] = 1

# Automata movil
gameState[21, 21] = 1
gameState[22, 22] = 1
gameState[22, 23] = 1
gameState[21, 23] = 1
gameState[20, 23] = 1

# Control de la ejecucion
pauseExect = False

# Bucle de ejecución
while True:
    
    newGameState = np.copy(gameState)

    screen.fill(bg)
    time.sleep(0.1)

    # Registramos eventos de teclado y ratón
    ev = pygame.event.get()

    for event in ev:
        if event.type == pygame.KEYDOWN:
            pauseExect = not pauseExect

        mouseClick = pygame.mouse.get_pressed()
        
        if sum(mouseClick) > 0:
            posX, posY = pygame.mouse.get_pos()
            celX, celY = int(np.floor(posX / dimCW)), int(np.floor(posY / dimCH))
            newGameState[celX, celY] = not mouseClick[2]


    for y in range(0, nxC):
        for x in range(0, nyC):

            if not pauseExect:

                # Calculamos el numero de vecinos cercanos
                n_neigh = gameState[(x - 1) % nxC, (y - 1) % nyC] + \
                            gameState[(x)     % nxC, (y - 1) % nyC] + \
                            gameState[(x + 1) % nxC, (y - 1) % nyC] + \
                            gameState[(x - 1) % nxC, (y)     % nyC] + \
                            gameState[(x + 1) % nxC, (y)     % nyC] + \
                            gameState[(x - 1) % nxC, (y + 1) % nyC] + \
                            gameState[(x)     % nxC, (y + 1) % nyC] + \
                            gameState[(x + 1) % nxC, (y + 1) % nyC]

            # Regla 1: Una celula muerta con exactamente 3 vecinas vivas "revive"
            if gameState[x, y] == 0 and n_neigh == 3:
                newGameState[x, y] = 1

            # Regla 2: Una celula viva con menos de 2 o mas de 3 vecinas vivas "muere"
            elif gameState[x, y] == 1 and (n_neigh < 2 or n_neigh > 3):
                newGameState[x, y] = 0

            # Creamos el poligono de cada celda a dibujar
            poly = [((x) * dimCW, y * dimCH),
                    ((x+1) * dimCW, y * dimCH),
                    ((x+1) * dimCW, (y+1) * dimCH),
                    ((x) * dimCW, (y+1) * dimCH)]

            # Y dibujamos la celda para cada par x e y
            if newGameState[x, y] == 0:
                pygame.draw.polygon(screen, (128, 128, 128), poly, 1)
            else:
                pygame.draw.polygon(screen, (255, 255, 255), poly, 0)

    # Actualizamos el estado del juego
    gameState = np.copy(newGameState)

    # actualizamos la pantalla
    pygame.display.flip()