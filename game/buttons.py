import pygame
from game.constants import (
    VINTAGE_BUTTON_COLOR,
    VINTAGE_BUTTON_HOVER_COLOR,
    VINTAGE_FONT_COLOR,
    WINDOW_HEIGHT,
    STABLE_STRUCTURES,
    CELL_SIZE,
    COLS,
)


class Buttons:
    def __init__(self):
        button_width = 150
        button_height = 50
        total_button_height = 6 * button_height + 5 * 20
        self.button_margin_y = (WINDOW_HEIGHT - total_button_height) // 2
        board_width = COLS * CELL_SIZE
        total_width = board_width + button_width + 60
        margin_x = (1280 - total_width) // 2

        self.structure_button_rect = pygame.Rect(
            margin_x, self.button_margin_y, button_width, button_height
        )
        self.random_button_rect = pygame.Rect(
            margin_x,
            self.button_margin_y + button_height + 20,
            button_width,
            button_height,
        )
        self.run_button_rect = pygame.Rect(
            margin_x,
            self.button_margin_y + 2 * (button_height + 20),
            button_width,
            button_height,
        )
        self.stop_button_rect = pygame.Rect(
            margin_x,
            self.button_margin_y + 3 * (button_height + 20),
            button_width,
            button_height,
        )
        self.reset_button_rect = pygame.Rect(
            margin_x,
            self.button_margin_y + 4 * (button_height + 20),
            button_width,
            button_height,
        )
        self.quit_button_rect = pygame.Rect(
            margin_x,
            self.button_margin_y + 5 * (button_height + 20),
            button_width,
            button_height,
        )

        self.structure_menu_visible = False
        self.structure_menu_rects = [
            pygame.Rect(
                margin_x + button_width + 20,
                self.button_margin_y + i * (button_height + 10),
                button_width,
                button_height,
            )
            for i in range(len(STABLE_STRUCTURES))
        ]

    def draw(self, screen, mouse_pos):
        self._draw_button(screen, self.structure_button_rect, "Structure", mouse_pos)
        self._draw_button(screen, self.random_button_rect, "Random", mouse_pos)
        self._draw_button(screen, self.run_button_rect, "Run", mouse_pos)
        self._draw_button(screen, self.stop_button_rect, "Stop", mouse_pos)
        self._draw_button(screen, self.reset_button_rect, "Reset", mouse_pos)
        self._draw_button(screen, self.quit_button_rect, "Quit", mouse_pos)

        if self.structure_menu_visible:
            for idx, rect in enumerate(self.structure_menu_rects):
                structure_name = list(STABLE_STRUCTURES.keys())[idx]
                self._draw_button(screen, rect, structure_name, mouse_pos)

    def _draw_button(self, screen, rect, text, mouse_pos):
        color = (
            VINTAGE_BUTTON_HOVER_COLOR
            if rect.collidepoint(mouse_pos)
            else VINTAGE_BUTTON_COLOR
        )
        pygame.draw.rect(screen, color, rect, border_radius=10)
        font = pygame.font.SysFont("Arial", 20)
        text_surf = font.render(text, True, VINTAGE_FONT_COLOR)
        text_rect = text_surf.get_rect(center=rect.center)
        screen.blit(text_surf, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if self.structure_button_rect.collidepoint(x, y):
                self.structure_menu_visible = not self.structure_menu_visible
                return "structure"
            if self.structure_menu_visible:
                for idx, rect in enumerate(self.structure_menu_rects):
                    if rect.collidepoint(x, y):
                        structure_name = list(STABLE_STRUCTURES.keys())[idx]
                        self.structure_menu_visible = False
                        return structure_name
            if self.run_button_rect.collidepoint(x, y):
                return "Run"
            if self.stop_button_rect.collidepoint(x, y):
                return "Stop"
            if self.reset_button_rect.collidepoint(x, y):
                return "Reset"
            if self.random_button_rect.collidepoint(x, y):
                return "Random"
            if self.quit_button_rect.collidepoint(x, y):
                return "Quit"
        return None
