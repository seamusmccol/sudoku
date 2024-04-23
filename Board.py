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







class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty

    def draw(self):
        pass

    def select(self, row, col):
        pass

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

