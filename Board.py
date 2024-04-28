import pygame,sys

WIDTH = 600
HEIGHT = 600
RED = (255, 0, 0)
BG_COLOR = (0, 0, 0)
LINE_COLOR = (255, 255, 255)
NUM_COLOR = (255, 255, 255)
BOARD_ROWS = 9
BOARD_COLS = 9
LINE_WIDTH = 4
LINE_WIDTH2 = 1
WIN_LINE_WIDTH = 2
SQUARE_SIZE = 200
SQUARE_SIZE2 = 66.7
SPACE_SIZE = 20
NUM_SIZE = 40
GAME_OVER_FONT = 40
GRAY = (128, 128, 128)







screen = pygame.display.set_mode((WIDTH, HEIGHT))

class Board:
    def __init__(self, WIDTH, HEIGHT, screen, difficulty):
        self.selected = None
        self.width = WIDTH
        self.height = HEIGHT
        self.screen = screen
        self.difficulty = difficulty

    def draw(self):
        for i in range(1, BOARD_ROWS):
            pygame.draw.line(
                screen,
                LINE_COLOR,
                (0, i * SQUARE_SIZE),
                (WIDTH, i * SQUARE_SIZE),
                LINE_WIDTH
            )
            pygame.draw.line(
                screen,
                LINE_COLOR,
                (0, i * SQUARE_SIZE2),
                (WIDTH, i * SQUARE_SIZE2),
                LINE_WIDTH2
            )
        # draw vertical lines
        for i in range(1, BOARD_COLS):
            pygame.draw.line(
                screen,
                LINE_COLOR,
                (i * SQUARE_SIZE, 0),
                (i * SQUARE_SIZE, HEIGHT),
                LINE_WIDTH
            )
            pygame.draw.line(
                screen,
                LINE_COLOR,
                (i * SQUARE_SIZE2, 0),
                (i * SQUARE_SIZE2, HEIGHT),
                LINE_WIDTH2
            )

    def select(self, row, col):
        self.selected = (row, col)

    def click(self, x, y):
        pass

    def clear(self):
        pass

    def sketch(self, value):
        pass

    def place_number(self, value):
        pass

    def reset_to_original(self):
        pass

    def is_full(self):
        pass

    def update_board(self):
        pass

    def find_empty(self):
        pass

    def check_board(self):
        pass

