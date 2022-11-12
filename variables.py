import numpy as np

# Ancho y alto de la ventana
width, height = 1000, 1000

# Colores
bg = 25, 25, 25

# Numero de celdas
nxC, nyC = 50, 50

# Dimensiones de la celda
dimCW = width / nxC
dimCH = height / nyC

# Estado de las celdas. Vivas = 1; Muertas = 0
gameState = np.zeros((nxC, nyC))