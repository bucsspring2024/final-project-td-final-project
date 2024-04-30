import pygame
import sys
from controller import Controller

# Initialize pygame
pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 480
FPS = 60
PLAYER_SPEED = 5
OBSTACLE_SPEED = 3
OBSTACLE_FREQUENCY = 2000  

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Runner Game")
clock = pygame.time.Clock()

# Load images function
def load_image(img_path, width, height, colorkey=None):
    try:
        image = pygame.image.load(img_path).convert()
        if colorkey is not None:
            image.set_colorkey(colorkey)
        image = pygame.transform.scale(image, (width, height))
        return image
    except pygame.error as e:
        print(f'Unable to load image at path {img_path}. Error: {e}')
        return pygame.Surface((width, height))  # return empty surface if fail

# Load player and background images or set defaults
player_image = load_image('assets/player.png', 50, 50, WHITE)  # Updated path
background_image = load_image('assets/background.png', SCREEN_WIDTH, SCREEN_HEIGHT)  # Updated path


# Player setup
player_rect = player_image.get_rect(topleft=(50, SCREEN_HEIGHT - 100))

# Obstacles setup
obstacles = []
last_obstacle = pygame.time.get_ticks()

# Utility functions
def draw_text(text, size, color, x, y):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

# Game state functions
def start_menu():
    screen.fill(BLACK)
    draw_text('Simple Runner Game', 40, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 60)
    draw_text('Press Enter to start', 30, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    draw_text('Press ESC to quit', 30, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 60)
    pygame.display.update()

def game_active():
    global last_obstacle
    screen.blit(background_image, (0, 0))
    screen.blit(player_image, player_rect)

    # Handle obstacles
    current_time = pygame.time.get_ticks()
    if current_time - last_obstacle > OBSTACLE_FREQUENCY:
        obstacle_rect = pygame.Rect(SCREEN_WIDTH, SCREEN_HEIGHT - 100, 20, 50)
        obstacles.append(obstacle_rect)
        last_obstacle = current_time

    for obstacle in obstacles[:]:
        obstacle.x -= OBSTACLE_SPEED
        if obstacle.x < 0:
            obstacles.remove(obstacle)
        pygame.draw.rect(screen, RED, obstacle)

    # Check for collisions
    if any(player_rect.colliderect(obstacle) for obstacle in obstacles):
        return False  # Game over
    return True  # Continue game

def game_over():
    screen.fill(BLACK)
    draw_text('Game Over', 50, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 30)
    draw_text('Press Enter to restart', 30, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 30)
    pygame.display.update()

# Main game loop
def main():
    running = True
    active_game = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    active_game = True
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        if not active_game:
            start_menu()
        else:
            active_game = game_active()
            if not active_game:
                game_over()
                pygame.time.wait(2000)  
                active_game = True  

        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
