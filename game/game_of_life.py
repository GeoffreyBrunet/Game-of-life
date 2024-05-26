import pygame
from game.board import Board
from game.buttons import Buttons
from game.constants import BACKGROUND_COLOR


class GameOfLife:
    def __init__(self):
        self.board = Board()
        self.buttons = Buttons()
        self.screen = pygame.display.set_mode((1280, 800))
        pygame.display.set_caption("Game of Life")
        self.running = False
        self.mouse_down = False
        self.is_drawing = True
        self.selected_structure = None

    def run(self):
        clock = pygame.time.Clock()
        running = True
        while running:
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if event.button == 1:
                        self.mouse_down = True
                        if self.buttons.structure_menu_visible:
                            structure_name = self.buttons.handle_event(event)
                            if structure_name and structure_name != "structure":
                                self.selected_structure = structure_name
                                self.board.place_structure(self.selected_structure)
                                self.selected_structure = None
                        else:
                            button_action = self.buttons.handle_event(event)
                            if button_action:
                                self.handle_button_action(button_action)
                            else:
                                self.board.toggle_cell(x, y)
                    elif event.button == 3:
                        self.is_drawing = not self.is_drawing
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.mouse_down = False
                elif event.type == pygame.MOUSEMOTION and self.mouse_down:
                    x, y = event.pos
                    if event.buttons[0]:
                        self.board.toggle_cell_drag(x, y, self.is_drawing)
            self.screen.fill(BACKGROUND_COLOR)
            self.board.draw(self.screen)
            self.buttons.draw(self.screen, mouse_pos)
            pygame.display.flip()
            if self.running:
                self.board.update_grid()
            clock.tick(10)
        pygame.quit()

    def handle_button_action(self, action):
        if action == "Run":
            self.running = True
        elif action == "Stop":
            self.running = False
        elif action == "Reset":
            self.board.reset_grid()
        elif action == "Random":
            self.board.randomize_grid()
        elif action == "Quit":
            pygame.quit()
            exit()
