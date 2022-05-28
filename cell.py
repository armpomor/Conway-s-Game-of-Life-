import pygame as pg
from config import *


class Cell:
    def __init__(self, x, y):
        self.image = pg.Surface((SIZE_CELL - 1, SIZE_CELL - 1))
        self.rect = pg.Rect(x * SIZE_CELL, y * SIZE_CELL, SIZE_CELL - 1, SIZE_CELL - 1)
        
        
    