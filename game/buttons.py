import pygame
from game.constants import BLACK, GREY, LIGHT_GREY, WINDOW_HEIGHT, STABLE_STRUCTURES


class Buttons:
    def __init__(self):
        button_width = 120
        button_height = 40
        total_button_height = 5 * button_height + 4 * 20
        self.button_margin_y = (WINDOW_HEIGHT - total_button_height) // 2
        self.structure_button_rect = pygame.Rect(
            20, self.button_margin_y, button_width, button_height
        )
        self.run_button_rect = pygame.Rect(
            20, self.button_margin_y + button_height + 20, button_width, button_height
        )
        self.stop_button_rect = pygame.Rect(
            20,
            self.button_margin_y + 2 * (button_height + 20),
            button_width,
            button_height,
        )
        self.reset_button_rect = pygame.Rect(
            20,
            self.button_margin_y + 3 * (button_height + 20),
            button_width,
            button_height,
        )
        self.quit_button_rect = pygame.Rect(
            20,
            self.button_margin_y + 4 * (button_height + 20),
            button_width,
            button_height,
        )
        self.structure_menu_visible = False
        self.structure_menu_rects = [
            pygame.Rect(
                160,
                self.button_margin_y + i * (button_height + 10),
                button_width,
                button_height,
            )
            for i in range(len(STABLE_STRUCTURES))
        ]

    def draw(self, screen, mouse_pos):
        self._draw_button(screen, self.structure_button_rect, "Structure", mouse_pos)
        self._draw_button(screen, self.run_button_rect, "Run", mouse_pos)
        self._draw_button(screen, self.stop_button_rect, "Stop", mouse_pos)
        self._draw_button(screen, self.reset_button_rect, "Reset", mouse_pos)
        self._draw_button(screen, self.quit_button_rect, "Quit", mouse_pos)
        if self.structure_menu_visible:
            for idx, rect in enumerate(self.structure_menu_rects):
                structure_name = list(STABLE_STRUCTURES.keys())[idx]
                self._draw_button(screen, rect, structure_name, mouse_pos)

    def _draw_button(self, screen, rect, text, mouse_pos):
        color = LIGHT_GREY if rect.collidepoint(mouse_pos) else GREY
        pygame.draw.rect(screen, color, rect)
        font = pygame.font.SysFont(None, 24)
        text_surf = font.render(text, True, BLACK)
        text_rect = text_surf.get_rect(center=rect.center)
        screen.blit(text_surf, text_rect)
