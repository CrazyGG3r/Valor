
import pygame
import sys
import random as rrr

# Initialize Pygame
pygame.init()

# Function to convert RGB to hex
def rgb_to_hex(r, g, b):
    return '{:02x}{:02x}{:02x}'.format(r, g, b)

# Set up the screen
screen_width = 1300
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Gradient Squares")

# Colors 
WHITE = (0,0,0)
RED =(73, 36, 62)######<------ RED MEANS STARTINGGG COLOR. SHOULD BE DARK
GREEN =(219, 175, 160)### <<______------ GREEEN MEANS ENDING COLOR. SHOULD BE BRIGHT
 

# Square dimensions and positions
square_size = 30
margin = 50 # Margin between squares
square_y = 100

# Calculate gradient colors
num_squares = 12
colors = []
for i in range(num_squares + 2):  # Add 2 for red and green endpoints
    ratio = i / (num_squares + 1)
    # Interpolate between red and green
    r = int((1 - ratio) * RED[0] + ratio * GREEN[0])
    g = int((1 - ratio) * RED[1] + ratio * GREEN[1])
    b = int((1 - ratio) * RED[2] + ratio * GREEN[2])
    colors.append((r, g, b))

# Set up the font
font = pygame.font.Font(None, 24)

# Main loop
running = True
print(colors)
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with white color
    screen.fill(WHITE)

    # Draw squares and display RGB values
    for i in range(num_squares+2):
        square_x = (screen_width - (num_squares * (square_size + margin) - margin)) / 2 + i * (square_size + margin)
        
        # Draw the square with the interpolated color
        pygame.draw.rect(screen, colors[i ], (square_x, square_y, square_size, square_size))
        
        # Create a text surface for the RGB values
        rgb_text = font.render(f"{colors[i]}", True, (200,200,200))
        
        # Display the RGB values above each square
        if i%2 != 0:
            screen.blit(rgb_text, (square_x-30, square_y-30))
        else:
            screen.blit(rgb_text, (square_x-30, square_y+50))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
