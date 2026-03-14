import pygame
import random

# Initialize Pygame
pygame.init()

# Define Screen and Colors
WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Custom Event Color Change")

# 1. Define a Custom Event
# Custom events in Pygame start at pygame.USEREVENT
CHANGE_COLOR_EVENT = pygame.USEREVENT + 1

# Define Sprite Class
class MySprite(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.image = pygame.Surface((60, 60))
        self.color = color
        self.image.fill(self.color)
        self.rect = self.image.get_rect(center=(x, y))

    def update_color(self):
        # Generate a random color
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.image.fill(self.color)

# 2. Add 2 Sprites
sprite1 = MySprite((255, 0, 0), 150, 150) # Red sprite
sprite2 = MySprite((0, 0, 255), 250, 150) # Blue sprite

# Create a group to manage them
all_sprites = pygame.sprite.Group(sprite1, sprite2)

# 3. Create a timer for the Custom Event (triggers every 1000ms / 1 second)
pygame.time.set_timer(CHANGE_COLOR_EVENT, 1000)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # 4. Handle the Custom Event
        if event.type == CHANGE_COLOR_EVENT:
            for sprite in all_sprites:
                sprite.update_color()

    # Draw everything
    screen.fill((30, 30, 30)) # Dark grey background
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
