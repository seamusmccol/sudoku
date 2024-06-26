# Final version
import random
from Cell import *
from Board import *
from sudoku_generator import SudokuGenerator
import pygame, sys
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")
screen.fill(BG_COLOR)

num_font = pygame.font.Font(None, NUM_SIZE)

difficulty = 'easy'



def game_start_screen(screen):
    # Initialize screens and fonts for the start screen
    screen.fill(BG_COLOR)
    start_title_font = pygame.font.Font(None, 75)
    start_subtitle_font = pygame.font.Font(None, 55)
    button_font = pygame.font.Font(None, 50)

    # Initialize background image
    BG_surface = pygame.image.load("Graphics/BG.png")
    screen.blit(BG_surface, (0, 0))

    # Initialize the start screen itself and draw it
    title = start_title_font.render("Welcome to Sudoku", 0, LINE_COLOR)
    title_rect = title.get_rect( center=(WIDTH//2, HEIGHT//2 - 150))
    screen.fill(BG_COLOR, title_rect)
    screen.blit(title, title_rect)

    subtitle = start_subtitle_font.render("Select Game Mode:", 0, LINE_COLOR)
    subtitle_rect = subtitle.get_rect( center=(WIDTH//2, HEIGHT//2 - 50))
    screen.fill(BG_COLOR, subtitle_rect)
    screen.blit(subtitle, subtitle_rect)

    # Initialize button and text
    easy_text = button_font.render("Easy", 0, (255, 255, 255))
    medium_text = button_font.render("Medium", 0, (255, 255, 255))
    hard_text = button_font.render("Hard", 0, (255, 255, 255))

    # Initialize background and text color of the buttons
    easy = pygame.Surface((easy_text.get_size()[0] + 20, easy_text.get_size()[1] + 20))
    easy.fill(BG_COLOR)
    easy.blit(easy_text, (10, 10))
    medium = pygame.Surface((medium_text.get_size()[0] + 20, medium_text.get_size()[1] + 20))
    medium.fill(BG_COLOR)
    medium.blit(medium_text, (10, 10))
    hard = pygame.Surface((hard_text.get_size()[0] + 20, hard_text.get_size()[1] + 20))
    hard.fill(BG_COLOR)
    hard.blit(hard_text, (10, 10))

    # Global button rectangle areas for mouse click checking in main()
    global easy_rectangle, medium_rectangle, hard_rectangle

    # Activates button
    easy_rectangle = easy.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    medium_rectangle = medium.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 120))
    hard_rectangle = hard.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 190))

    # Draw Buttons
    screen.blit(easy, easy_rectangle)
    screen.blit(medium, medium_rectangle)
    screen.blit(hard, hard_rectangle)


def game_buttons(screen):
    button_font = pygame.font.Font(None, 50)

    # Initialize button and text
    reset_text = button_font.render("Reset", 0, (255, 255, 255))
    restart_text = button_font.render("Restart", 0, (255, 255, 255))
    exit_text = button_font.render("Exit", 0, (255, 255, 255))

    # Initialize background and text color of the buttons
    reset = pygame.Surface((reset_text.get_size()[0] + 20, reset_text.get_size()[1] + 20))
    reset.fill(BG_COLOR)
    reset.blit(reset_text, (10, 10))
    restart = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
    restart.fill(BG_COLOR)
    restart.blit(restart_text, (10, 10))
    exit = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
    exit.fill(BG_COLOR)
    exit.blit(exit_text, (10, 10))

    # Global button rectangle areas for mouse click checking in main()
    global reset_rectangle, restart_rectangle, exit_rectangle

    # Activates button
    reset_rectangle = reset.get_rect(center=(WIDTH // 2 - 150, HEIGHT // 2 + 350))
    restart_rectangle = restart.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 350))
    exit_rectangle = exit.get_rect(center=(WIDTH // 2 + 150, HEIGHT // 2 + 350))


    # Draw Buttons

    screen.blit(reset, reset_rectangle)
    screen.blit(restart, restart_rectangle)
    screen.blit(exit, exit_rectangle)

def game_won_screen(screen):
    # Initialize screens and fonts for the start screen
    screen.fill(BG_COLOR)
    title_font = pygame.font.Font(None, 75)
    button_font = pygame.font.Font(None, 50)

    # Initialize background image
    BG_surface = pygame.image.load("Graphics/BG.png")
    screen.blit(BG_surface, (0, 0))

    # Initialize the start screen itself and draw it
    title = title_font.render("Game Won!", 0, LINE_COLOR)
    title_rect = title.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100))
    screen.fill(BG_COLOR, title_rect)
    screen.blit(title, title_rect)

    # Initialize button and text
    exit_text = button_font.render("EXIT", 0, (255, 255, 255))

    # Initialize background and text color of the buttons
    exit = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
    exit.fill(BG_COLOR)
    exit.blit(exit_text, (10, 10))

    # Global button rectangle areas for mouse click checking in main()
    global exit_rectangle
    # Activates button
    exit_rectangle = exit.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))

    # Draw Buttons
    screen.blit(exit, exit_rectangle)

def game_lost_screen(screen):
    # Initialize screens and fonts for the start screen
    screen.fill(BG_COLOR)
    title_font = pygame.font.Font(None, 75)
    button_font = pygame.font.Font(None, 50)

    # Initialize background image
    BG_surface = pygame.image.load("Graphics/BG.png")
    screen.blit(BG_surface, (0, 0))

    # Initialize the start screen itself and draw it
    title = title_font.render("Game Over :(", 0, LINE_COLOR)
    title_rect = title.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100))
    screen.fill(BG_COLOR, title_rect)
    screen.blit(title, title_rect)

    # Initialize button and text
    restart_text = button_font.render("RESTART", 0, (255, 255, 255))

    # Initialize background and text color of the buttons
    restart = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
    restart.fill(BG_COLOR)
    restart.blit(restart_text, (10, 10))

    # Global button rectangle areas for mouse click checking in main()
    global restart_rectangle
    # Activates button
    restart_rectangle = restart.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))

    # Draw Buttons
    screen.blit(restart, restart_rectangle)


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
def check_fill():
    for i in range(9):
        for j in range(9):
            if sudoku.get_board()[i][j] == " ":
                return False
    return True

# win_list = []
# in_list = []

# [[], [], [], [], [], [], [], [], []]
in_list_i = [[] for i in range(9)]
in_list_j = [[] for j in range(9)]
box = [[] for j in range(9)]

def check_board():
    # check_board function ONLY return True when row, col, 33 grid all three are satisfied
    # check row
    for i in range(9): # row
        for j in range(9): # col
            # if sudoku.get_board()[i][j] == " ":
            #     return False
            if sudoku.get_board()[i][j] not in in_list_i[i]:
                in_list_i[i].append(sudoku.get_board()[i][j])
                in_list_i[i].append(int(sudoku.get_board()[i][j]))
                continue
            elif sudoku.get_board()[i][j] in in_list_i[i]:
                # print(f"row {i} is: {in_list_i[i]}")
                return False
    # check col
    for j in range(9): # row
        for i in range(9): # col
            # if sudoku.get_board()[i][j] == " ":
            #     return False
            if sudoku.get_board()[i][j] not in in_list_j[j]:
                in_list_j[j].append(sudoku.get_board()[i][j])
                in_list_j[j].append(int(sudoku.get_board()[i][j]))
                continue
            elif sudoku.get_board()[i][j] in in_list_j[j]:
                return False

    # for i in in_list:
    #     print(i)
    # check 3x3 box

    for i in range(9): # row
        for j in range(9): # col
            box_index = j//3 + (i//3) * 3
            # if sudoku.get_board()[i][j] == " ":
            #     return False
            if sudoku.get_board()[i][j] not in box[box_index]:
                box[box_index].append(int(sudoku.get_board()[i][j]))
            elif sudoku.get_board()[i][j] in box[box_index]:
                return False
    # If all three check pass
    return True
def draw_select(col_num,row_num):
    pygame.draw.rect(screen, ('Red'), (SQUARE_SIZE2*col_num+5, SQUARE_SIZE2*row_num+5, SQUARE_SIZE2-7.5, SQUARE_SIZE2-7.5), 5)
    pygame.display.update()

def remove_select(col_num,row_num):
    pygame.draw.rect(screen, ('Black'), (SQUARE_SIZE2*col_num+5, SQUARE_SIZE2*row_num+5, SQUARE_SIZE2-7.5, SQUARE_SIZE2-7.5), 5)
    pygame.display.update()

def check_empty():
    if str(sudoku.get_board()[int(row_num)][int(col_num)]) == " ":
        return True

difficulty_button_clicked = False
# Initialize game start screen
while True:
    screen.fill(BG_COLOR)
    game_start_screen(screen)

    pygame.display.update()
    break

# Uncomment either one to see how it looks
# game_won_screen(screen)
# game_lost_screen(screen)

# This variable is to ensure the program will ONLY proceed when a button in welcome screen is clicked

current_screen = 0
start_screen = 1
game_screen = 2
easy_button = True
medium_button = True
hard_button = True
reset_button = True
restart_button = True
exit_button = True

click_time = -2
last_col_num = 0
last_row_num = 0

current_screen = start_screen

sketch_board = [[0] * 9 for i in range(9)]

while True:
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            row = y // SQUARE_SIZE2
            col = x // SQUARE_SIZE2

        # Mouse click coordinate are x,y.
            board = Board(row, col, screen, difficulty)
            board.select(x, y)
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

            # The following if functions detect which button user clicked
            if (easy_rectangle.collidepoint(x, y)) and (easy_button == True):
                # User click on "easy", should set blank space generated quantity accordingly
                difficulty_button_clicked = True
                difficulty = "easy"
                easy_button = False
            elif (medium_rectangle.collidepoint(x, y)) and (medium_button == True):
                # User click on "medium", should set blank space generated quantity accordingly
                difficulty_button_clicked = True
                difficulty = "medium"
                medium_button = False
            elif (hard_rectangle.collidepoint(x, y)) and (hard_button == True):
                # User click on "hard", should set blank space generated quantity accordingly
                difficulty_button_clicked = True
                difficulty = "hard"
                hard_button = False

        if difficulty_button_clicked == True:
            if current_screen == start_screen:
                current_screen = game_screen
                # Set up the grid
                if difficulty == "easy":
                    sudoku = SudokuGenerator(9, 1)
                    sudoku.fill_values()
                    sudoku.remove_cells()
                if difficulty == "medium":
                    sudoku = SudokuGenerator(9, 40)
                    sudoku.fill_values()
                    sudoku.remove_cells()
                if difficulty == "hard":
                    sudoku = SudokuGenerator(9, 50)
                    sudoku.fill_values()
                    sudoku.remove_cells()

                difficulty_button_clicked = False

                game_buttons(screen)
                num_font = pygame.font.Font(None, NUM_SIZE)
                screen = pygame.display.set_mode((WIDTH, EHEIGHT))
                game_buttons(screen)

                # print(sudoku.get_board()[0][0])

                for row in range(BOARD_ROWS):
                    for col in range(BOARD_COLS):
                        # print([[row],[col]],  sudoku.get_board()[row][col])
                        num = sudoku.get_board()[row][col]
                        num_surf = num_font.render(str(num), 0, NUM_COLOR)
                        num_rect = num_surf.get_rect(center=(col * SQUARE_SIZE2 + SQUARE_SIZE2 / 2, row * SQUARE_SIZE2 + SQUARE_SIZE2 / 2))
                        screen.blit(num_surf, num_rect)
                # print the diagonal again
                board.draw()

                pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

            # The following if functions detect which button user clicked
            if (reset_rectangle.collidepoint(x, y)) and (reset_button == True):
                # resets the board according to their chosen difficulty
                if difficulty == "easy":
                    sudoku = SudokuGenerator(9, 30)
                    sudoku.fill_values()
                    sudoku.remove_cells()
                if difficulty == "medium":
                    sudoku = SudokuGenerator(9, 40)
                    sudoku.fill_values()
                    sudoku.remove_cells()
                if difficulty == "hard":
                    sudoku = SudokuGenerator(9, 50)
                    sudoku.fill_values()
                    sudoku.remove_cells()
                    break

                num_font = pygame.font.Font(None, NUM_SIZE)
                screen = pygame.display.set_mode((WIDTH, EHEIGHT))
                game_buttons(screen)
                #
                for row in range(BOARD_ROWS):
                    for col in range(BOARD_COLS):
                        # print([[row],[col]],  sudoku.get_board()[row][col])
                        num = sudoku.get_board()[row][col]
                        num_surf = num_font.render(str(num), 0, NUM_COLOR)
                        num_rect = num_surf.get_rect(center=(col * SQUARE_SIZE2 + SQUARE_SIZE2 / 2, row * SQUARE_SIZE2 + SQUARE_SIZE2 / 2))
                        screen.blit(num_surf, num_rect)
                # print the diagnal again
                board.draw()
                pygame.display.update()
                break

            elif (restart_rectangle.collidepoint(x, y)) and (restart_button == True):
                # Restarts to the start screen
                current_screen = 0
                start_screen = 1
                game_screen = 2
                easy_button = True
                medium_button = True
                hard_button = True
                reset_button = True
                restart_button = True
                exit_button = True
                screen.fill(BG_COLOR)
                game_start_screen(screen)

                pygame.display.update()
                current_screen = start_screen

            elif (exit_rectangle.collidepoint(x, y)) and (exit_button == True):
                # Ends the game
                pygame.quit()
                sys.exit()


        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

            if (restart_rectangle.collidepoint(x, y)) and (restart_button == True):
                # Clear all game state lists
                in_list_i = [[] for _ in range(9)]
                in_list_j = [[] for _ in range(9)]
                box = [[] for _ in range(9)]

                # Reset game as before
                current_screen = start_screen
                easy_button = medium_button = hard_button = True
                screen.fill(BG_COLOR)
                game_start_screen(screen)
                pygame.display.update()

                # Restarts to the start screen
                # current_screen = 0
                start_screen = 1
                game_screen = 2
                # easy_button = True
                # medium_button = True
                # hard_button = True
                reset_button = True
                restart_button = True
                exit_button = True
                screen.fill(BG_COLOR)
                game_start_screen(screen)

                pygame.display.update()
                # current_screen = start_screen
                break

            elif (exit_rectangle.collidepoint(x, y)) and (exit_button == True):
                # Ends the game
                pygame.quit()
                sys.exit()


        # mouseclick
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            # print(x,y)
            col_num = x // SQUARE_SIZE2
            row_num = y // SQUARE_SIZE2

            if click_time <= 0:
                click_time += 1
            if click_time == 0:
                draw_select(col_num, row_num)
                last_col_num = col_num
                last_row_num = row_num
                empty = check_empty()
                click_time += 1
            elif click_time > 0:
                remove_select(last_col_num, last_row_num)
                draw_select(col_num, row_num)
                last_col_num = col_num
                last_row_num = row_num
                empty = check_empty()

        if event.type == pygame.KEYDOWN and click_time > 0:
            if event.key == pygame.K_LEFT:
                col_num -= 1
                # row_num = row_num
                remove_select(last_col_num, last_row_num)
                draw_select(col_num, row_num)
                last_col_num = col_num
                last_row_num = row_num
                empty = check_empty()

                # check_empty()
                # print(row_num,col_num)
                # print(sudoku.get_board()[int(row_num)][int(col_num)])

            elif event.key == pygame.K_RIGHT:
                col_num += 1
                remove_select(last_col_num, last_row_num)
                draw_select(col_num, row_num)
                last_col_num = col_num
                last_row_num = row_num
                empty = check_empty()

            elif event.key == pygame.K_UP:
                row_num -= 1
                remove_select(last_col_num, last_row_num)
                draw_select(col_num, row_num)
                last_col_num = col_num
                last_row_num = row_num
                empty = check_empty()

            elif event.key == pygame.K_DOWN:
                row_num += 1
                remove_select(last_col_num, last_row_num)
                draw_select(col_num, row_num)
                last_col_num = col_num
                last_row_num = row_num
                empty = check_empty()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                if empty == True:
                    num_surf = num_font.render(str(1), 0, GRAY)
                    num_rect = num_surf.get_rect(
                        center=(col_num * SQUARE_SIZE2 + SQUARE_SIZE2 / 2, row_num * SQUARE_SIZE2 + SQUARE_SIZE2 / 2))
                    screen.blit(num_surf, num_rect)

                    sketch_board[int(row_num)][int(col_num)] = 1

            elif event.key == pygame.K_2:
                if empty == True:
                    num_surf = num_font.render(str(2), 0, GRAY)
                    num_rect = num_surf.get_rect(
                        center=(col_num * SQUARE_SIZE2 + SQUARE_SIZE2 / 2, row_num * SQUARE_SIZE2 + SQUARE_SIZE2 / 2))
                    screen.blit(num_surf, num_rect)
                    sketch_board[int(row_num)][int(col_num)] = 2

            elif event.key == pygame.K_3:
                if empty == True:
                    num_surf = num_font.render(str(3), 0, GRAY)
                    num_rect = num_surf.get_rect(
                        center=(col_num * SQUARE_SIZE2 + SQUARE_SIZE2 / 2, row_num * SQUARE_SIZE2 + SQUARE_SIZE2 / 2))
                    screen.blit(num_surf, num_rect)
                    sketch_board[int(row_num)][int(col_num)] = 3

            elif event.key == pygame.K_4:
                if empty == True:
                    num_surf = num_font.render(str(4), 0, GRAY)
                    num_rect = num_surf.get_rect(
                        center=(col_num * SQUARE_SIZE2 + SQUARE_SIZE2 / 2, row_num * SQUARE_SIZE2 + SQUARE_SIZE2 / 2))
                    screen.blit(num_surf, num_rect)
                    sketch_board[int(row_num)][int(col_num)] = 4

            elif event.key == pygame.K_5:
                if empty == True:
                    num_surf = num_font.render(str(5), 0, GRAY)
                    num_rect = num_surf.get_rect(
                        center=(col_num * SQUARE_SIZE2 + SQUARE_SIZE2 / 2, row_num * SQUARE_SIZE2 + SQUARE_SIZE2 / 2))
                    screen.blit(num_surf, num_rect)
                    sketch_board[int(row_num)][int(col_num)] = 5

            elif event.key == pygame.K_6:
                if empty == True:
                    num_surf = num_font.render(str(6), 0, GRAY)
                    num_rect = num_surf.get_rect(
                        center=(col_num * SQUARE_SIZE2 + SQUARE_SIZE2 / 2, row_num * SQUARE_SIZE2 + SQUARE_SIZE2 / 2))
                    screen.blit(num_surf, num_rect)
                    sketch_board[int(row_num)][int(col_num)] = 6

            elif event.key == pygame.K_7:
                if empty == True:
                    num_surf = num_font.render(str(7), 0, GRAY)
                    num_rect = num_surf.get_rect(
                        center=(col_num * SQUARE_SIZE2 + SQUARE_SIZE2 / 2, row_num * SQUARE_SIZE2 + SQUARE_SIZE2 / 2))
                    screen.blit(num_surf, num_rect)
                    sketch_board[int(row_num)][int(col_num)] = 7

            elif event.key == pygame.K_8:
                if empty == True:
                    num_surf = num_font.render(str(8), 0, GRAY)
                    num_rect = num_surf.get_rect(
                        center=(col_num * SQUARE_SIZE2 + SQUARE_SIZE2 / 2, row_num * SQUARE_SIZE2 + SQUARE_SIZE2 / 2))
                    screen.blit(num_surf, num_rect)
                    sketch_board[int(row_num)][int(col_num)] = 8

            elif event.key == pygame.K_9:
                if empty == True:
                    num_surf = num_font.render(str(9), 0, GRAY)
                    num_rect = num_surf.get_rect(
                        center=(col_num * SQUARE_SIZE2 + SQUARE_SIZE2 / 2, row_num * SQUARE_SIZE2 + SQUARE_SIZE2 / 2))
                    screen.blit(num_surf, num_rect)
                    sketch_board[int(row_num)][int(col_num)] = 9

        if event.type == pygame.KEYDOWN:
            # etch-in when return is pressed
            if event.key == pygame.K_RETURN:
                value = sketch_board[int(row_num)][int(col_num)]

                sudoku.get_board()[int(row_num)][int(col_num)] = value

                # print(sudoku.get_board())

                num_surf = num_font.render(str(value), 0, NUM_COLOR)
                num_rect = num_surf.get_rect(
                    center=(col * SQUARE_SIZE2 + SQUARE_SIZE2 / 2, row * SQUARE_SIZE2 + SQUARE_SIZE2 / 2))
                screen.blit(num_surf, num_rect)


                # determine if board is fully filled
                if check_fill() == True:
                    # check if a win is achieved (Three checks: row, col, 3x3 grid)
                    if check_board() == True:
                        game_won_screen(screen)
                    elif check_board() ==  False:
                        game_lost_screen(screen)
                        sudoku.board = [[0] * sudoku.row_length for i in range(sudoku.row_length)]



        pygame.display.update()
























