import pygame
from game.constants import (
    BLACK,
    WHITE,
    ROWS,
    COLS,
    CELL_SIZE,
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    STABLE_STRUCTURES,
)


class Board:
    def __init__(self):
        self.cell_size = CELL_SIZE
        self.rows = ROWS
        self.cols = COLS
        self.width = self.cols * self.cell_size
        self.height = self.rows * self.cell_size
        self.grid = [[WHITE for _ in range(self.cols)] for _ in range(self.rows)]
        self.margin_x = (WINDOW_WIDTH - self.width) // 2
        self.margin_y = (WINDOW_HEIGHT - self.height) // 2

    def draw(self, screen):
        for row in range(self.rows):
            for col in range(self.cols):
                color = self.grid[row][col]
                pygame.draw.rect(
                    screen,
                    color,
                    (
                        self.margin_x + col * self.cell_size,
                        self.margin_y + row * self.cell_size,
                        self.cell_size,
                        self.cell_size,
                    ),
                )
                pygame.draw.rect(
                    screen,
                    BLACK,
                    (
                        self.margin_x + col * self.cell_size,
                        self.margin_y + row * self.cell_size,
                        self.cell_size,
                        self.cell_size,
                    ),
                    1,
                )

    def toggle_cell(self, x, y):
        if (
            self.margin_x <= x < self.margin_x + self.width
            and self.margin_y <= y < self.margin_y + self.height
        ):
            col = (x - self.margin_x) // self.cell_size
            row = (y - self.margin_y) // self.cell_size
            if self.grid[row][col] == WHITE:
                self.grid[row][col] = BLACK
            else:
                self.grid[row][col] = WHITE

    def toggle_cell_drag(self, x, y, is_drawing):
        if (
            self.margin_x <= x < self.margin_x + self.width
            and self.margin_y <= y < self.margin_y + self.height
        ):
            col = (x - self.margin_x) // self.cell_size
            row = (y - self.margin_y) // self.cell_size
            if is_drawing:
                self.grid[row][col] = BLACK
            else:
                self.grid[row][col] = WHITE

    def count_alive_neighbors(self, row, col):
        directions = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]
        count = 0
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < self.rows and 0 <= c < self.cols:
                if self.grid[r][c] == BLACK:
                    count += 1
        return count

    def update_grid(self):
        new_grid = [[WHITE for _ in range(self.cols)] for _ in range(self.rows)]
        for row in range(self.rows):
            for col in range(self.cols):
                alive_neighbors = self.count_alive_neighbors(row, col)
                if self.grid[row][col] == BLACK:
                    if alive_neighbors == 2 or alive_neighbors == 3:
                        new_grid[row][col] = BLACK
                    else:
                        new_grid[row][col] = WHITE
                else:
                    if alive_neighbors == 3:
                        new_grid[row][col] = BLACK
        self.grid = new_grid

    def reset_grid(self):
        self.grid = [[WHITE for _ in range(self.cols)] for _ in range(self.rows)]

    def place_structure(self, structure_name, x, y):
        structure = STABLE_STRUCTURES[structure_name]
        for dx, dy in structure:
            row = (y + dy) // self.cell_size
            col = (x + dx) // self.cell_size
            if 0 <= row < self.rows and 0 <= col < self.cols:
                self.grid[row][col] = BLACK
