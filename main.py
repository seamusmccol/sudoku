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

# Initialize game start screen
screen.fill(BG_COLOR)
game_start_screen(screen)


# Uncomment either one to see how it looks
# game_won_screen(screen)
# game_lost_screen(screen)

# This variable is to ensure the program will ONLY proceed when a button in welcome screen is clicked
difficulty_button_clicked = False

while True:
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Display the mouse click coordinate just for testing purpose.
        # It should be removed/commented for the final presentation
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            print(x, y)
            row = y // SQUARE_SIZE
            col = x // SQUARE_SIZE

        # Mouse click coordinate are x,y.
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

            # The following if functions detect which button user clicked
            if easy_rectangle.collidepoint(x, y):
                # User click on "easy", should set blank space generated quantity accordingly
                print("easy")
                difficulty_button_clicked = True
            elif medium_rectangle.collidepoint(x, y):
                # User click on "medium", should set blank space generated quantity accordingly
                print("medium")
                difficulty_button_clicked = True
            elif hard_rectangle.collidepoint(x, y):
                # User click on "hard", should set blank space generated quantity accordingly
                print("hard")
                difficulty_button_clicked = True

        if difficulty_button_clicked == True:
            # Set up the grid
            screen.fill(BG_COLOR)
            draw_grid()
            draw_num()


    pygame.display.update()

