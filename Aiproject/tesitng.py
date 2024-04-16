
import pygame
import math

# Constants
WIDTH, HEIGHT = 800, 600
RADIUS = 30
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Define Circle class
class Circle:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed = 5
        self.direction = [1, 1]  # Initial direction

    def move(self):
        self.x += self.speed * self.direction[0]
        self.y += self.speed * self.direction[1]

    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

# Function to check collision between two circles
def check_collision(circle1, circle2):
    distance = math.sqrt((circle1.x - circle2.x)**2 + (circle1.y - circle2.y)**2)
    if distance < circle1.radius + circle2.radius:
        return True
    return False

# Create two circles
circle1 = Circle(200, 300, RADIUS, WHITE)
circle2 = Circle(200, 300, RADIUS, RED)

running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move circles
    circle1.move()
    circle2.move()

    # Check collision
    if check_collision(circle1, circle2):
        # Simple collision response - reverse direction
        circle1.direction[0] *= 1
        circle1.direction[1] *= 1
        circle2.direction[0] *= -1
        circle2.direction[1] *= -1

    # Draw circles
    circle1.draw()
    circle2.draw()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
