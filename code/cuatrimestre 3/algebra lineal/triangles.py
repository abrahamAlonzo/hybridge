import pygame
import random
import math

# Inicializar Pygame
pygame.init()

# Definir colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Configurar pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego de Triángulos")

# Variables del juego
triangles = []  # Lista para guardar los triángulos creados
font = pygame.font.SysFont(None, 36)

def draw_triangle(surface, color, vertex1, vertex2, vertex3):
    """Función para dibujar un triángulo."""
    pygame.draw.polygon(surface, color, [vertex1, vertex2, vertex3])

def generate_triangle(hypotenuse, cateto):
    """Generar las coordenadas de un triángulo rectángulo a partir de la hipotenusa y el cateto."""
    other_cateto = math.sqrt(hypotenuse**2 - cateto**2)
    
    # Generar una posición aleatoria en pantalla
    x = random.randint(0, WIDTH - 1)
    y = random.randint(0, HEIGHT - 1)
    
    # Vertices del triángulo rectángulo
    vertex1 = (x, y)  # Punto inicial
    vertex2 = (x + cateto, y)  # Punto en el eje x
    vertex3 = (x, y + int(other_cateto))  # Punto en el eje y

    return (vertex1, vertex2, vertex3)

def check_overlap(new_triangle):
    """Verificar si un triángulo se solapa con otros triángulos ya dibujados."""
    for triangle in triangles:
        if pygame.Rect(new_triangle).colliderect(pygame.Rect(triangle)):
            return True
    return False

def game_loop():
    running = True
    clock = pygame.time.Clock()
    
    while running:
        screen.fill(WHITE)

        # Evento de salida
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Generar aleatoriamente la hipotenusa y solicitar el cateto
        hypotenuse = random.randint(50, 150)
        user_input = input(f"Ingresa el valor de un cateto (para hipotenusa {hypotenuse}): ")
        cateto = int(user_input)

        # Generar triángulo
        new_triangle = generate_triangle(hypotenuse, cateto)
        
        # Verificar si el triángulo se solapa con los existentes
        if check_overlap(new_triangle):
            print("¡Perdiste! No se puede dibujar más triángulos.")
            running = False
        else:
            # Dibujar el nuevo triángulo
            triangles.append(new_triangle)
            draw_triangle(screen, RED, *new_triangle)

        # Dibujar los triángulos ya existentes
        for triangle in triangles:
            draw_triangle(screen, BLACK, *triangle)
        
        pygame.display.flip()
        clock.tick(30)

# Iniciar el juego
game_loop()

# Salir
pygame.quit()
