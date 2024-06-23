import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame Timer Example")

# Set up font
font = pygame.font.Font(None, 74)  # None uses the default font, 74 is the font size
text_color = (255, 255, 255)  # White color

# Set up the timer
start_ticks = pygame.time.get_ticks()  # Get the number of milliseconds since Pygame was initialized
timer_duration = 60  # Timer duration in seconds

# Main game loop
clock = pygame.time.Clock()
FPS = 60  # Desired frames per second
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calculate the elapsed time
    elapsed_seconds = (pygame.time.get_ticks() - start_ticks) // 1000
    remaining_time = timer_duration - elapsed_seconds
    if remaining_time < 0:
        remaining_time = 0

    # Render the timer text
    timer_text = f"Time: {remaining_time}"
    text_surface = font.render(timer_text, True, text_color)
    text_rect = text_surface.get_rect(center=(width // 2, height // 2))

    # Fill the screen with a color (black)
    screen.fill((0, 0, 0))

    # Blit the text surface onto the screen
    screen.blit(text_surface, text_rect)

    # Update the display
    pygame.display.flip()

    # Maintain frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
