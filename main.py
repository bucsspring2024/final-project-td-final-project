import pygame
import sys

# Constants for screen dimensions and colors
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Full Game Implementation')
clock = pygame.time.Clock()

# Function to draw text for menus and buttons
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

# Player class handling movement and collision
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.speed = 5
        self.health = 100

    def update(self, keys_pressed, obstacles):
        original_rect = self.rect.copy()
        if keys_pressed[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys_pressed[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys_pressed[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys_pressed[pygame.K_DOWN]:
            self.rect.y += self.speed

        # Collision detection and health management
        if pygame.sprite.spritecollideany(self, obstacles):
            self.rect = original_rect
            self.health -= 10
            if self.health <= 0:
                return True  # Game Over condition
        return False

# Obstacle class
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super(Obstacle, self).__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(RED)
        self.rect = self.image.get_rect(topleft=(x, y))

# Main menu function with interactive buttons
def main_menu():
    menu_font = pygame.font.Font(None, 50)
    button_start = draw_text('Start Game', menu_font, WHITE, screen, SCREEN_WIDTH // 2, 250)
    button_options = draw_text('Options', menu_font, WHITE, screen, SCREEN_WIDTH // 2, 320)
    button_quit = draw_text('Quit', menu_font, WHITE, screen, SCREEN_WIDTH // 2, 390)

    while True:
        screen.fill(BLACK)
        draw_text('Main Menu', menu_font, WHITE, screen, SCREEN_WIDTH // 2, 150)
        draw_text('Start Game', menu_font, WHITE, screen, SCREEN_WIDTH // 2, 250)
        draw_text('Options', menu_font, WHITE, screen, SCREEN_WIDTH // 2, 320)
        draw_text('Quit', menu_font, WHITE, screen, SCREEN_WIDTH // 2, 390)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(60)

# Game over screen display function
def game_over_screen():
    screen.fill(BLACK)
    font = pygame.font.Font(None, 74)
    draw_text('Game Over', font, RED, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    pygame.display.flip()
    pygame.time.wait(2000)  # Show Game Over screen for 2 seconds

# Main game loop
def game_loop():
    player = Player()
    all_sprites = pygame.sprite.Group(player)
    obstacles = pygame.sprite.Group(Obstacle(300, 300, 200, 50), Obstacle(100, 200, 50, 200))
    all_sprites.add(obstacles)

    running = True
    while running:
        keys_pressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if player.update(keys_pressed, obstacles):
            game_over_screen()
            break

        screen.fill(BLACK)
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

# Uncomment the line below to run the full game
# main_menu()  # Start from the main menu