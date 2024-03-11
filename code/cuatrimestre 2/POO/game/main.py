# pygame demo 2 - una imagen, clic y movimiento
# 1 - Importar paquetes
import pygame
from pygame.locals import *
import sys
import random
# 2 - Definir constantes
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
BALL_WIDTH_HEIGHT = 200
MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT
TARGET_X = 400
TARGET_Y = 320 
TARGET_WIDTH_HEIGHT = 120 
N_PIXELS_TO_MOVE = 3
# 3 - Inicializar el mundo
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
# 4 - Cargar activos: imagen(es), sonido(s), etc.
ballImage = pygame.image.load('images/ball.png')
targetImage = pygame.image.load('images/target.png')
# 5 - Inicializar variables
ballX = random.randrange(MAX_WIDTH)
ballY = random.randrange(MAX_HEIGHT)
ballRect = pygame.Rect(ballX, ballY, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)
targetRect = pygame.Rect(TARGET_X, TARGET_Y,TARGET_WIDTH_HEIGHT, TARGET_WIDTH_HEIGHT)
# 6 - Bucle infinito
while True:
  # 7 - Comprobar y manejar eventos
  for event in pygame.event.get():
    # ¿Se hizo clic en el botón de cierre? Salir de pygame y terminar el programa
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

    # Verificar si el usuario presionó una tecla
    elif event.type == pygame.KEYDOWN: 
      if event.key == pygame.K_LEFT:
        ballX = ballX - N_PIXELS_TO_MOVE
      elif event.key == pygame.K_RIGHT:
        ballX = ballX + N_PIXELS_TO_MOVE
      elif event.key == pygame.K_UP:
        ballY = ballY - N_PIXELS_TO_MOVE
      elif event.key == pygame.K_DOWN:
        ballY = ballY + N_PIXELS_TO_MOVE

    # Verificar si el usuario hizo clic
    if event.type == pygame.MOUSEBUTTONUP:
    #mouseX, mouseY = event.pos  # Podría hacerse esto si lo necesitáramos
    # Verificar si el clic fue dentro del rectángulo de la bola
    # Si es así, elegir una nueva ubicación aleatoria
      if ballRect.collidepoint(event.pos):
        ballX = random.randrange(MAX_WIDTH)
        ballY = random.randrange(MAX_HEIGHT)
        ballRect = pygame.Rect(ballX, ballY, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)
  # 8 - Realizar acciones "por cuadro"
  ballRect = pygame.Rect(ballX, ballY, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)
  if ballRect.colliderect(targetRect): 
    print('La pelota esta tocando el objetivo')
  # 9 - Limpiar la ventana
  window.fill(BLACK)
  # 10 - Dibujar todos los elementos de la ventana
  window.blit(targetImage, (TARGET_X, TARGET_Y)) # Dibuja el objetivo
  # Dibujar la bola en la ubicación aleatoria
  window.blit(ballImage, (ballX, ballY))
  # 11 - Actualizar la ventana
  pygame.display.update()
  # 12 - Reducir la velocidad un poco
  clock.tick(FRAMES_PER_SECOND)