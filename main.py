import pygame, sys
from Board import *
from sudoku_generator import SudokuGenerator

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")

screen.fill(BG_COLOR)

num_font = pygame.font.Font(None, NUM_SIZE)

difficulty = 'easy'

Board(board, WIDTH, HEIGHT, screen, difficulty)


def draw_grid():
    #draw horizontal line
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
    #draw vertical lines
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

def draw_num():
    #the number 5 is temporary, will take an input in the future
    num_surf = num_font.render("5", 0, NUM_COLOR)
    #make the board initialization in order for this to work
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] != 0:
                num_rect = num_surf.get_rect( center = (col*SQUARE_SIZE + SQUARE_SIZE/2, row * SQUARE_SIZE + SQUARE_SIZE/2))
                screen.blit(num_surf, num_rect)


    num_surf = num_font.render("5", 0, NUM_COLOR)
    num_rect = num_surf.get_rect(center = (WIDTH / 2, HEIGHT / 2))
    screen.blit(num_surf, num_rect)


screen.fill(BG_COLOR)
draw_grid()
draw_num()

while True:
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            #stuff below isn't final
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            print(x, y)
            row = y // SQUARE_SIZE
            col = x // SQUARE_SIZE
    pygame.display.update()

