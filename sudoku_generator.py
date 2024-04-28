# Test push
import math, random, copy
from Board import *
import pygame





class SudokuGenerator:
    def __init__(self, row_length, removed_cells):
        self.row_length = 9
        self.removed_cells = int(removed_cells)
        self.box_length = int(math.sqrt(self.row_length))
        self.board = [[0] * self.row_length for i in range(self.row_length)]

    # our getter func
    def get_board(self):
        return self.board

    # this function displays the board to the console
    def print_board(self):
        for row in range(self.row_length):
            for col in range(self.row_length):
                print(f"{self.board[row][col]} ", end="")
            print()

    # this function checks if a number is contained in a given row
    def valid_in_row(self, row, num):
        for i in range(0, self.row_length):
            if self.board[row][i] == num:
                return False
        return True

    # this function checks if a number is contained in a given column
    def valid_in_col(self, col, num):
        for i in range(0, self.row_length):
            if self.board[int(i)][int(col)] == num:
                return False
        return True

    # this function checks if a number is contained in any given box
    def valid_in_box(self, row_start, col_start, num):
        for a in range(row_start, row_start + 3):
            for b in range(int(col_start), int(col_start + 3)):
                if 0 <= a < self.row_length and 0 <= b < self.row_length and self.board[a][b] == num:
                    return False
        return True

    # this function checks if a number can be inputted at a certain position on the board
    def is_valid(self, row, col, num):

        if self.valid_in_row(row, num) and self.valid_in_col(col, num) and self.valid_in_box(
                row - row % int(self.box_length), col - col % int(self.box_length), num):
            return True
        return False

    # this function fills a given 3x3 box with values
    def fill_box(self, row_start, col_start):
        numbers = random.sample(range(1, self.row_length + 1), self.row_length)
        index = 0
        for a in range(row_start, row_start + 3):
            for b in range(col_start, col_start + 3):
                self.board[a][b] = numbers[index]
                index += 1

    # this function fills the diagonals
    def fill_diagonal(self):
        num_font = pygame.font.Font(None, NUM_SIZE)
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        used_numbers = [[] for _ in range(BOARD_ROWS)]
        used_columns = [[] for _ in range(BOARD_ROWS)]
        used_grids = [[] for _ in range(BOARD_ROWS)]
        # creates a diagonal
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if row < 3:
                    if col < 3:
                        grid_index = (row // 3) * 3 + (col // 3)
                        valid_found = False
                        attempts = 0
                        while not valid_found and attempts < 100:
                            random_num = random.randint(1, 9)
                            if (random_num not in used_numbers[row] and random_num not in used_columns[col] and
                                    random_num not in used_grids[grid_index]):
                                num_surf = num_font.render(str(random_num), 0, NUM_COLOR)
                                num_rect = num_surf.get_rect(
                                    center=(
                                    col * SQUARE_SIZE2 + SQUARE_SIZE2 / 2, row * SQUARE_SIZE2 + SQUARE_SIZE2 / 2))
                                screen.blit(num_surf, num_rect)
                                # Append this number to self.board
                                self.board[row][col] = random_num

                                used_numbers[row].append(random_num)
                                used_columns[col].append(random_num)
                                used_grids[grid_index].append(random_num)
                                valid_found = True
                            attempts += 1
                elif row >= 3 and row < 6:
                    if col >= 3 and col < 6:
                        grid_index = (row // 3) * 3 + (col // 3)
                        valid_found = False
                        attempts = 0
                        while not valid_found and attempts < 100:
                            random_num = random.randint(1, 9)
                            if (random_num not in used_numbers[row] and
                                    random_num not in used_columns[col] and
                                    random_num not in used_grids[grid_index]):
                                num_surf = num_font.render(str(random_num), 0, NUM_COLOR)
                                num_rect = num_surf.get_rect(
                                    center=(
                                    col * SQUARE_SIZE2 + SQUARE_SIZE2 / 2, row * SQUARE_SIZE2 + SQUARE_SIZE2 / 2))
                                screen.blit(num_surf, num_rect)
                                # Append this number to self.board
                                self.board[row][col] = random_num

                                used_numbers[row].append(random_num)
                                used_columns[col].append(random_num)
                                used_grids[grid_index].append(random_num)
                                valid_found = True
                            attempts += 1

                elif row >= 6 and row < 9:
                    if col >= 6 and col < 9:
                        grid_index = (row // 3) * 3 + (col // 3)
                        valid_found = False
                        attempts = 0
                        while not valid_found and attempts < 100:
                            random_num = random.randint(1, 9)

                            if (random_num not in used_numbers[row] and
                                    random_num not in used_columns[col] and
                                    random_num not in used_grids[grid_index]):
                                num_surf = num_font.render(str(random_num), 0, NUM_COLOR)
                                num_rect = num_surf.get_rect(
                                    center=(col * SQUARE_SIZE2 + SQUARE_SIZE2 / 2, row * SQUARE_SIZE2 + SQUARE_SIZE2 / 2))
                                screen.blit(num_surf, num_rect)
                                # Append this number to self.board
                                self.board[row][col] = random_num

                                used_numbers[row].append(random_num)
                                used_columns[col].append(random_num)
                                used_grids[grid_index].append(random_num)
                                valid_found = True
                            attempts += 1

    # once fill_diagonal is called, this function proceeds to fill the rest of the board
    def fill_remaining(self, row, col):
        if col >= self.row_length and row < self.row_length - 1:
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < int(self.box_length):
            if col < int(self.box_length):
                col = int(self.box_length)
        elif row < self.row_length - int(self.box_length):
            if col == int(row // self.box_length * self.box_length):
                col += int(self.box_length)
        else:
            if col == self.row_length - int(self.box_length):
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[int(row)][int(
                    col)] = num
                if self.fill_remaining(int(row),
                                       int(col) +
                                       1):
                    return True
                self.board[int(row)][int(col)] = 0
        return False

    # this function fills the entire board with values
    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    # randomly generates coords on the board with value = 0 based on the users inputted level of difficulty
    def remove_cells(self):
        target = self.removed_cells
        changed = 0
        while changed < target:
            row = random.randint(0, self.row_length - 1)
            col = random.randint(0, self.row_length - 1)
            if self.board[row][col] != " ":
                self.board[row][col] = " "
                changed = changed + 1
            elif self.board[row][col] == 0:
                continue
        return


# this function generates the board players will interact with
def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    completed_board = copy.deepcopy(board)
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board, completed_board