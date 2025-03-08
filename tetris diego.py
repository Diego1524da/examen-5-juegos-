import pygame
import random

# Inicialización de Pygame
pygame.init()

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
LIGHT_BLUE = (0, 191, 255)
DARK_BLUE = (25, 25, 112)
PINK = (255, 105, 180)

# Tamaño de la pantalla
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
BLOCK_SIZE = 30

# Crear la ventana
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris")

# Definir las piezas
shapes = [
    [[1, 1, 1, 1]],  # Línea
    [[1, 1], [1, 1]],  # Cuadrado
    [[1, 1, 0], [0, 1, 1]],  # Z
    [[0, 1, 1], [1, 1, 0]],  # S
    [[1, 1, 1], [0, 1, 0]],  # T
    [[1, 0, 0], [1, 1, 1]],  # L
    [[0, 0, 1], [1, 1, 1]],  # J
]

colors = [CYAN, YELLOW, RED, GREEN, BLUE, ORANGE, MAGENTA]

# Definir el tablero
board = [[0] * 10 for _ in range(20)]

# Definir el puntaje
score = 0
font = pygame.font.SysFont('Arial', 25)
font_button = pygame.font.SysFont('Arial', 22)

# Función para dibujar el tablero con bordes
def draw_board():
    for y in range(20):
        for x in range(10):
            if board[y][x] != 0:
                pygame.draw.rect(screen, board[y][x], (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
                pygame.draw.rect(screen, WHITE, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 2)  # Borde de las piezas

# Función para crear una nueva pieza
def new_piece():
    shape = random.choice(shapes)
    color = random.choice(colors)
    return shape, color

# Función para rotar la pieza
def rotate(shape):
    return [list(row) for row in zip(*shape[::-1])]

# Función para verificar si la pieza se puede mover
def valid_move(shape, offset):
    off_x, off_y = offset
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                if x + off_x < 0 or x + off_x >= 10 or y + off_y >= 20:
                    return False
                if y + off_y >= 0 and board[y + off_y][x + off_x] != 0:
                    return False
    return True

# Función para colocar la pieza en el tablero
def place_piece(shape, color, offset):
    off_x, off_y = offset
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                board[y + off_y][x + off_x] = color

# Función para eliminar líneas completas
def clear_lines():
    global score
    new_board = [row for row in board if any(cell == 0 for cell in row)]
    lines_cleared = 20 - len(new_board)
    score += lines_cleared * 100
    new_board = [[0] * 10] * lines_cleared + new_board
    return new_board

# Función para manejar la caída de las piezas
def drop_piece(shape, color, offset):
    while valid_move(shape, [offset[0], offset[1] + 1]):
        offset[1] += 1
    place_piece(shape, color, offset)
    return [3, 0]  # Nuevo inicio para la siguiente pieza

# Función para dibujar el botón de reinicio con efectos
def draw_restart_button():
    restart_button = pygame.Rect(100, 250, 100, 50)
    pygame.draw.rect(screen, LIGHT_BLUE, restart_button, border_radius=10)
    pygame.draw.rect(screen, DARK_BLUE, restart_button, 5, border_radius=10)
    restart_text = font_button.render('Reiniciar', True, WHITE)
    screen.blit(restart_text, (restart_button.x + 20, restart_button.y + 10))
    return restart_button

# Función para dibujar fondo de pantalla con gradiente
def draw_background():
    for y in range(SCREEN_HEIGHT):
        color = (y * 255 // SCREEN_HEIGHT, 100, 255 - y * 255 // SCREEN_HEIGHT)
        pygame.draw.line(screen, color, (0, y), (SCREEN_WIDTH, y))

# Función principal del juego
def game():
    global score, board
    clock = pygame.time.Clock()
    running = True
    piece, color = new_piece()
    offset = [3, 0]
    drop_speed = 500  # Tiempo en milisegundos para la caída de la pieza
    last_drop = pygame.time.get_ticks()

    while running:
        draw_background()  # Dibujar fondo de pantalla con gradiente
        draw_board()  # Dibujar el tablero
        draw_restart_button()  # Dibujar el botón de reinicio

        # Mostrar puntaje con sombra para hacerlo más legible
        score_text = font.render(f"Puntaje: {score}", True, WHITE)
        shadow_text = font.render(f"Puntaje: {score}", True, BLACK)  # Sombra para resaltar el texto
        screen.blit(shadow_text, (12, 12))  # Sombra del puntaje
        screen.blit(score_text, (10, 10))  # Puntaje real

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if valid_move(piece, [offset[0] - 1, offset[1]]):
                        offset[0] -= 1
                if event.key == pygame.K_RIGHT:
                    if valid_move(piece, [offset[0] + 1, offset[1]]):
                        offset[0] += 1
                if event.key == pygame.K_DOWN:
                    if valid_move(piece, [offset[0], offset[1] + 1]):
                        offset[1] += 1
                if event.key == pygame.K_UP:
                    rotated = rotate(piece)
                    if valid_move(rotated, offset):
                        piece = rotated

            # Detectar clic en el botón de reinicio
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if restart_button.collidepoint(mouse_x, mouse_y):
                    board = [[0] * 10 for _ in range(20)]
                    score = 0

        # Controlar la caída automática de la pieza
        if pygame.time.get_ticks() - last_drop > drop_speed:
            last_drop = pygame.time.get_ticks()
            if valid_move(piece, [offset[0], offset[1] + 1]):
                offset[1] += 1
            else:
                place_piece(piece, color, offset)
                board = clear_lines()
                piece, color = new_piece()
                offset = [3, 0]
                if not valid_move(piece, offset):
                    running = False  # El juego termina

        # Dibujar la pieza que está cayendo con un borde para más detalle
        for y, row in enumerate(piece):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(screen, color, ((offset[0] + x) * BLOCK_SIZE, (offset[1] + y) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
                    pygame.draw.rect(screen, WHITE, ((offset[0] + x) * BLOCK_SIZE, (offset[1] + y) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 2)  # Borde de la pieza

        pygame.display.flip()
        clock.tick(60)  # Controlar la tasa de cuadros

# Ejecutar el juego
game()

pygame.quit()
