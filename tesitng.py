import pygame
import sys
pygame.init()
class ColorPicker:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x  # X-coordinate for the color picker
        self.y = y  # Y-coordinate for the color picker

        # Initial RGB values
        self.r_value = 128
        self.g_value = 128
        self.b_value = 128

        # Slider dimensions and properties
        self.slider_width = 200
        self.slider_height = 20
        self.slider_y_offset = 50  # Space between sliders
        
        # Flags to track if the sliders are being dragged
        self.dragging_r = False
        self.dragging_g = False
        self.dragging_b = False
        
        # Font for displaying text
        self.font = pygame.font.Font(None, 24)

    def draw_slider(self, y, value, color,screen):
        pygame.draw.rect(screen, color, (self.x, y, self.slider_width, self.slider_height), 1)  # Draw the border
        fill_width = int(value / 255 * self.slider_width)
        pygame.draw.rect(screen, color, (self.x, y, fill_width, self.slider_height))  # Draw the slider fill

    def draw(self,screen):
        # Draw sliders for RGB values
        self.draw_slider(self.y, self.r_value, (self.r_value, 0, 0),screen)  # Red slider
        self.draw_slider(self.y + self.slider_y_offset, self.g_value, (0, self.g_value, 0),screen)  # Green slider
        self.draw_slider(self.y + 2 * self.slider_y_offset, self.b_value, (0, 0, self.b_value),screen)  # Blue slider
        
        # Display the selected color as a rectangle
        selected_color = (self.r_value, self.g_value, self.b_value)
        pygame.draw.rect(screen, selected_color, (self.x + 250, self.y, 100, 100))

        # Display RGB values as text
        rgb_text = self.font.render(f"RGB: {self.r_value}, {self.g_value}, {self.b_value}", True, (0, 0, 0))
        screen.blit(rgb_text, (self.x + 250, self.y + 110))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Check if the mouse clicked on any of the sliders
            if self.y <= mouse_y < self.y + self.slider_height:
                self.dragging_r = True
            elif self.y + self.slider_y_offset <= mouse_y < self.y + self.slider_y_offset + self.slider_height:
                self.dragging_g = True
            elif self.y + 2 * self.slider_y_offset <= mouse_y < self.y + 2 * self.slider_y_offset + self.slider_height:
                self.dragging_b = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragging_r, self.dragging_g, self.dragging_b = False, False, False  # Reset dragging flags

    def update(self):
        # Handle mouse dragging
        if pygame.mouse.get_pressed()[0]:  # Left mouse button is held down
            mouse_x, mouse_y = pygame.mouse.get_pos()
            
            # Adjust RGB values based on which slider is being dragged
            if self.dragging_r and self.x <= mouse_x <= self.x + self.slider_width:
                self.r_value = int((mouse_x - self.x) / self.slider_width * 255)
                self.r_value = max(0, min(self.r_value, 255))
            elif self.dragging_g and self.x <= mouse_x <= self.x + self.slider_width:
                self.g_value = int((mouse_x - self.x) / self.slider_width * 255)
                self.g_value = max(0, min(self.g_value, 255))
            elif self.dragging_b and self.x <= mouse_x <= self.x + self.slider_width:
                self.b_value = int((mouse_x - self.x) / self.slider_width * 255)
                self.b_value = max(0, min(self.b_value, 255))







screen_width = 800
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Multiple Color Pickers")


color_picker1 = ColorPicker(screen, x=50, y=50)
color_picker2 = ColorPicker(screen, x=50, y=200)

# Main loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
            running = False
        
        # Pass events to each color picker
        color_picker1.handle_event(event)
        color_picker2.handle_event(event)
        
    # Update each color picker
    color_picker1.update()
    color_picker2.update()

    # Fill the screen with white color
    screen.fill((255, 255, 255))

    # Draw each color picker
    color_picker1.draw(screen)
    color_picker2.draw(screen)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
