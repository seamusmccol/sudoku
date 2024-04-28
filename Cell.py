# Test push
from Board import *
import pygame
class Cell:

    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketch = 0
        self.selected = False
    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self,value):
        self.sketch = value

    def draw(self):
        pass
        # font = pygame.font.Font(None, 40)
        # if self.value != 0:
        #     text_1 = font.render(str(self.value), True, (0, 0, 0))
        #     self.rectangle = text_1.get_rect(center = (SQUARE_SIZE2//2+SQUARE_SIZE2* self.row, SQUARE_SIZE2//2 + SQUARE_SIZE2*self.col,))
        #     self.screen.blit(text_1, self.rectangle)
        # if self.selected:
        #     pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(self.row*SQUARE_SIZE2, self.col*SQUARE_SIZE2, SQUARE_SIZE2), 3)
        # else:
        #     pygame.draw.rect(self.screen, (255, 255, 255),
        #                      pygame.Rect(self.row*SQUARE_SIZE2, self.col*SQUARE_SIZE2, SQUARE_SIZE2), 3)
        #     # draw_lines()
