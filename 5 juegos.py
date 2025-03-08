import pygame
import sys
import random

# Inicialización de Pygame
pygame.init()

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Configuración de pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("3 Juegos en 1")

# Fuente del texto
font = pygame.font.SysFont(None, 60)

# Juego de Ping Pong
def game_ping_pong():
    paddle_width, paddle_height = 10, 100
    ball_size = 20

    player1 = pygame.Rect(30, HEIGHT // 2 - paddle_height // 2, paddle_width, paddle_height)
    player2 = pygame.Rect(WIDTH - 40, HEIGHT // 2 - paddle_height // 2, paddle_width, paddle_height)
    ball = pygame.Rect(WIDTH // 2 - ball_size // 2, HEIGHT // 2 - ball_size // 2, ball_size, ball_size)

    ball_speed_x, ball_speed_y = 4, 4
    paddle_speed = 6

    running = True
    while running:
        screen.fill(BLACK)

        pygame.draw.rect(screen, WHITE, player1)
        pygame.draw.rect(screen, WHITE, player2)
        pygame.draw.ellipse(screen, WHITE, ball)

        ball.x += ball_speed_x
        ball.y += ball_speed_y

        if ball.top <= 0 or ball.bottom >= HEIGHT:
            ball_speed_y *= -1

        if ball.colliderect(player1) or ball.colliderect(player2):
            ball_speed_x *= -1

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and player1.top > 0:
            player1.y -= paddle_speed
        if keys[pygame.K_s] and player1.bottom < HEIGHT:
            player1.y += paddle_speed
        if keys[pygame.K_UP] and player2.top > 0:
            player2.y -= paddle_speed
        if keys[pygame.K_DOWN] and player2.bottom < HEIGHT:
            player2.y += paddle_speed
        if keys[pygame.K_ESCAPE]:
            running = False

        if ball.left <= 0 or ball.right >= WIDTH:
            running = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
        pygame.time.Clock().tick(60)

# Juego de Nave disparando
def game_nave():
    nave = pygame.Rect(WIDTH // 2, HEIGHT - 50, 50, 30)
    bullets = []
    enemies = []

    enemy_spawn_timer = 30
    bullet_speed = 7

    running = True
    while running:
        screen.fill(BLACK)

        pygame.draw.rect(screen, GREEN, nave)

        for bullet in bullets[:]:
            bullet.y -= bullet_speed
            pygame.draw.rect(screen, WHITE, bullet)
            if bullet.bottom < 0:
                bullets.remove(bullet)

        if enemy_spawn_timer <= 0:
            enemy = pygame.Rect(random.randint(0, WIDTH - 40), 0, 40, 40)
            enemy.durability = 3  # Durabilidad del enemigo
            enemies.append(enemy)
            enemy_spawn_timer = 30
        else:
            enemy_spawn_timer -= 1

        for enemy in enemies[:]:
            enemy.y += 3
            pygame.draw.rect(screen, RED, enemy)

            for bullet in bullets[:]:
                if enemy.colliderect(bullet):
                    enemy.durability -= 1
                    bullets.remove(bullet)
                    if enemy.durability <= 0:
                        enemies.remove(enemy)

            if enemy.top > HEIGHT:
                enemies.remove(enemy)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and nave.left > 0:
            nave.x -= 5
        if keys[pygame.K_RIGHT] and nave.right < WIDTH:
            nave.x += 5
        if keys[pygame.K_SPACE]:
            bullets.append(pygame.Rect(nave.x + nave.width // 2 - 5, nave.y, 10, 20))
        if keys[pygame.K_ESCAPE]:
            running = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
        pygame.time.Clock().tick(60)

# Juego de Esquivar objetos
def game_esquivar():
    player = pygame.Rect(WIDTH // 2, HEIGHT - 50, 40, 40)
    projectiles = []
    projectile_speed = 5

    running = True
    while running:
        screen.fill(BLACK)
        pygame.draw.rect(screen, BLUE, player)

        if random.randint(1, 20) == 1:
            projectile = pygame.Rect(random.randint(0, WIDTH - 20), 0, 20, 20)
            projectiles.append(projectile)

        for projectile in projectiles[:]:
            projectile.y += projectile_speed
            pygame.draw.rect(screen, RED, projectile)
            if projectile.colliderect(player):
                running = False
            if projectile.top > HEIGHT:
                projectiles.remove(projectile)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.left > 0:
            player.x -= 5
        if keys[pygame.K_RIGHT] and player.right < WIDTH:
            player.x += 5
        if keys[pygame.K_ESCAPE]:
            running = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
        pygame.time.Clock().tick(60)

def main_menu():
    running = True
    while running:
        screen.fill(BLACK)
        title = font.render("3 Juegos en 1", True, WHITE)
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 100))

        text_ping_pong = font.render("[1] Ping Pong", True, BLUE)
        text_nave = font.render("[2] Nave", True, GREEN)
        text_esquivar = font.render("[3] Esquivar", True, RED)

        screen.blit(text_ping_pong, (WIDTH // 2 - text_ping_pong.get_width() // 2, 200))
        screen.blit(text_nave, (WIDTH // 2 - text_nave.get_width() // 2, 300))
        screen.blit(text_esquivar, (WIDTH // 2 - text_esquivar.get_width() // 2, 400))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    game_ping_pong()
                if event.key == pygame.K_2:
                    game_nave()
                if event.key == pygame.K_3:
                    game_esquivar()

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main_menu()
  