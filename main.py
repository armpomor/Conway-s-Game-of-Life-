import pygame as pg
from config import *
from grid import Grid


pg.init()


class App:
    def __init__(self):
        self.screen = pg.display.set_mode([COLS * SIZE_CELL, ROWS * SIZE_CELL])
        pg.display.set_caption("Conway's Game of Life")
        self.clock = pg.time.Clock()
        self.grid = Grid()
        self.fps = FPS

    
    def draw(self):
        pg.display.update()
        self.clock.tick(self.fps)
        self.screen.fill(WHITE)
        
        
    def pause(self):
        """Генерируем паузу при нажатии любой клавиши
        и выход при нажатии Esc, а также оживляем клетку
        на паузе"""
        while True:
          for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    exit()
                return
            elif event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.grid.revival()
                    self.grid.filling_cells()
                    pg.display.update()  
        
        
    def run(self):
        while True:
            self.draw()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()
                elif event.type == pg.KEYDOWN:
                    # Изменяем скорость
                    if event.key == pg.K_UP:
                        self.fps += SPEED_FPS
                    elif event.key == pg.K_DOWN and self.fps > SPEED_FPS:
                        self.fps -= SPEED_FPS
                    else:
                        self.pause()
                elif event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.grid.revival()
            
            self.grid.filling_cells()
            self.grid.cells = self.grid.life_or_death()
            
            

if __name__ == '__main__':
    app = App()
    app.run()