# Final version
from main import *
from Board import *
class Cell:

    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.rectangle = ''
        self.selected = False
        self.selectable = False
        if self.value == 0:
            self.selectable = True
    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self,value):
        self.value = value

    def draw(self):
        pass