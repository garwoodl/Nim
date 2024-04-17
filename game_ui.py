"""
Handles a user interface for playing the game. Maybe I'll experiment more later
"""
from GameState import GameState
from bots import *
import pygame
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Set up the window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Define basic colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
STONE_COLOR = (100, 100, 100)


class Button:
    def __init__(self, rect, text):
        self.rect = pygame.Rect(rect)
        self.text = text
        self.font = pygame.font.Font(None, 24)
        self.color = (150, 0, 0)
        self.hover_color = (200, 0, 0)
        self.clicked = False

    def draw(self, surface):
        color = self.hover_color if self.rect.collidepoint(pygame.mouse.get_pos()) else self.color
        pygame.draw.rect(surface, color, self.rect)
        text_surface = self.font.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                if self.rect.collidepoint(event.pos):
                    self.clicked = True


def draw_game_board(piles: list[int], screen: pygame.Surface, buttons: list[Button]):
    screen.fill(WHITE)  # Clear the screen with white

    bottom_height = 20
    start_y = screen.get_height() - bottom_height  # Starting Y-coordinate for the bottom of the screen

    # Calculate the maximum number of stones in any pile (for scaling)
    max_pile_size = max(piles) if piles else 0

    # Define constants for stone rendering 
    stone_size = 20  # Size (width and height) of each stone
    space_between_stones = 5  # Spacing between each stone within a pile
    space_between_piles = 4 * space_between_stones

    alpha = max_pile_size * (stone_size + space_between_stones) / (start_y - 5)
    if alpha > 1:
        stone_size /= alpha
        space_between_stones /= alpha

    # Calculate the total width needed to display all piles
    total_width_needed = len(piles) * (stone_size + space_between_piles)

    # Calculate the starting position to center the stones on the screen
    start_x = (screen.get_width() - total_width_needed) // 2

    # Draw each pile of stones
    current_x = start_x

    for pile_size in piles:
        current_y = start_y - (pile_size * (stone_size + space_between_stones))

        for _ in range(pile_size):
            pygame.draw.rect(screen, STONE_COLOR, 
                             (current_x, current_y, stone_size, stone_size))
            current_y += stone_size + space_between_stones

        current_x += stone_size + space_between_piles

    current_x = start_x
    button_height = stone_size // 2
    for i, pile_size in enumerate(piles):
        button_rect = (current_x, SCREEN_HEIGHT - button_height - 5, stone_size, button_height)
        buttons[i].rect = pygame.Rect(button_rect)
        buttons[i].draw(screen)
        current_x += stone_size + space_between_piles

    pygame.display.flip()  # Update the display


def handle_mouse_click(piles: list[int], buttons: list[Button]):
    for button in buttons:
        button.handle_event(pygame.event.Event(pygame.MOUSEBUTTONDOWN))  # Simulate mouse click event

    for i, button in enumerate(buttons):
        if button.clicked:
            # Prompt the user to enter the number of s  tones to remove from the selected pile
            pile_index = i
            pile_size = piles[pile_index]
            num_stones = input(f"Enter number of stones to remove from Pile {pile_index + 1} (1-{pile_size}): ")
            num_stones = int(num_stones) if num_stones.isdigit() else 0

            if 1 <= num_stones <= pile_size:
                piles[pile_index] -= num_stones
                print(f"Removed {num_stones} stones from Pile {pile_index + 1}.")
            else:
                print("Invalid number of stones.")

            button.clicked = False  # Reset button click state


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Nim Game")

    piles = [3, 4, 5]  # Example piles
    buttons = [Button((0, 0, 0, 0), "") for _ in range(len(piles))]  # Create buttons for each pile

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                print("Backspace")
                running = False

        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                handle_mouse_click(piles, buttons)

        draw_game_board(piles, screen, buttons)
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
