import pygame
import sys

class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 50, 50)
        self.y_velocity = 0
        self.on_ground = True

    def jump(self):
        if self.on_ground:
            self.y_velocity = -15  # Control jump height
            self.on_ground = False

    def update(self, gravity, ground_height):
        self.y_velocity += gravity
        self.rect.y += self.y_velocity
        if self.rect.y >= ground_height - self.rect.height:
            self.rect.y = ground_height - self.rect.height
            self.on_ground = True
            self.y_velocity = 0

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.rect)

class Controller:
    def __init__(self, screen, Player):
        """
        Initializes the Controller with a reference to the pygame screen and clock.
        This will be used to handle drawing and time-related functionalities within the controller.
        """
        self.screen = screen
        self.player = Player
        self.obstacles = []
        self.running = True
        self.gravity = 1
        self.ground_height = screen.get_height() - 100
        self.last_obstacle_time = pygame.time.get_ticks()

    def handle_events(self):
        """
        Handles all input events from the user, including quitting and other keyboard events.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.jump()

    def detect_collisions_and_update_models(self):
        """
        Checks for collisions between game entities and updates the model's states.
        """
        self.player.update(self.gravity, self.ground_height)
        current_time = pygame.time.get_ticks()
        if current_time - self.last_obstacle_time > 2000:
            obstacle = pygame.Rect(self.screen.get_width(), self.ground_height - 50, 20, 50)
            self.obstacles.append(obstacle)
            self.last_obstacle_time = current_time
        self.obstacles = [obs for obs in self.obstacles if obs.x > -20]
        for obstacle in self.obstacles:
            obstacle.x -= 3
            if self.player.rect.colliderect(obstacle):
                self.running = False

    def redraw_next_frame(self):
        """
        Redraws all game entities and updates the display.
        """
        self.screen.fill((0, 0, 0))
        self.player.draw(self.screen)
        for obstacle in self.obstacles:
            pygame.draw.rect(self.screen, (0, 255, 0), obstacle)

    def mainloop(self):
        """
        The main loop of the game, which continues until the game is running.
        """
        while self.running:
            self.handle_events()
            self.detect_collisions_and_update_models()
            self.redraw_next_frame()
            pygame.display.flip()

