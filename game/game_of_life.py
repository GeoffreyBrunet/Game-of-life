import pygame
from game.board import Board
from game.buttons import Buttons
from game.constants import WHITE, BLACK


class GameOfLife:
    def __init__(self):
        self.board = Board()
        self.buttons = Buttons()
        self.screen = pygame.display.set_mode((1280, 800))
        pygame.display.set_caption("Game of Life")
        self.running = False
        self.generation = 0
        self.mouse_down = False
        self.is_drawing = True

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
                    self.mouse_down = True
                    self.is_drawing = True if event.button == 1 else False
                    if self.buttons.run_button_rect.collidepoint(x, y):
                        self.running = True
                    elif self.buttons.stop_button_rect.collidepoint(x, y):
                        self.running = False
                    elif self.buttons.reset_button_rect.collidepoint(x, y):
                        self.board.reset_grid()
                        self.running = False
                        self.generation = 0
                    elif self.buttons.quit_button_rect.collidepoint(x, y):
                        running = False
                    else:
                        self.board.toggle_cell(x, y)
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.mouse_down = False
                elif event.type == pygame.MOUSEMOTION and self.mouse_down:
                    x, y = event.pos
                    self.board.toggle_cell_drag(x, y, self.is_drawing)
            if self.running:
                self.board.update_grid()
                self.generation += 1

            self.screen.fill(WHITE)
            self.board.draw(self.screen)
            self.buttons.draw(self.screen, mouse_pos)
            self._draw_info()
            pygame.display.flip()
            clock.tick(10)
        pygame.quit()

    def _draw_info(self):
        font = pygame.font.SysFont(None, 36)
        generation_text = font.render(f"Generation: {self.generation}", True, BLACK)
        self.screen.blit(
            generation_text, (20, self.buttons.quit_button_rect.bottom + 20)
        )
