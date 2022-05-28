from random import random
from config import *
import pygame as pg
from cell import Cell


class Grid:
    def __init__(self):
        self.screen = pg.display.set_mode([COLS * SIZE_CELL, ROWS * SIZE_CELL])
        self.cells = self.make_grid()
        
        
    def make_grid(self):
        """Генерируем сетку с живыми (1) и мертвыми (0) клетками"""
        self.cells = [[1 if random() < N else 0 for col in range(COLS)] for row in range(ROWS)]
        return self.cells
    
    
    def living_neighbors(self, position):
        """Определяем количество живых соседей"""
        count = 0
        system=[[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        x, y = position[0], position[1]
        for i in system:
            if self.cells[(x + i[0]) % len(self.cells)][(y + i[1]) % len(self.cells[0])]:
                count += 1
        return count
    
    
    def grid_dead_cells(self):
        """Генерируем сетку с мертвыми клетками"""
        return [[0 for j in range(len(self.cells[0]))] for i in range(len(self.cells))]
    
    
    def life_or_death(self):
        """Оживляем или умертвляем клетки в зависимости от
           количества соседей"""
        cells_2 = self.grid_dead_cells()
        
        for x, _ in enumerate(self.cells):
            for y, _ in enumerate(self.cells[0]):
                if self.cells[x][y]:
                    if self.living_neighbors((x, y)) not in (2, 3):
                        cells_2[x][y] = 0
                    else: 
                        cells_2[x][y] = 1
                    continue
                if self.living_neighbors((x, y)) == 3:
                    cells_2[x][y] = 1
                else:
                    cells_2[x][y] = 0
        self.cells = cells_2            
        return self.cells
    
    
    def filling_cells(self):
        """Отрисовываем все клетки"""
        for i, _ in enumerate(self.cells):
            for j, _ in enumerate(self.cells[i]):
                pg.draw.rect(self.screen, (0, 255 * self.cells[i][j] % 256, 0), Cell(i, j).rect)
        
        
    def revival(self):
        """Оживление клетки щелчком мыши"""
        position = pg.mouse.get_pos()
        # Вычисляем координаты ближайшей клетки
        x = position[0] // SIZE_CELL
        y = position[1] // SIZE_CELL
        # Оживляем клетку
        self.cells[x][y] = 1