import pygame
from SPRNVA import Vector

class Grid:
    def __init__(self, win: pygame.Surface, tile_size: Vector):
        self.win = win
        self.winX = self.win.get_width()
        self.winY = self.win.get_height()
        self.tile_size = tile_size

    def draw(self):
        for y in range(int(self.winY / self.tile_size.y)):
            pygame.draw.line(self.win, (255, 255, 255), (0, self.tile_size.y * y),
                             (self.winX, self.tile_size.y * y))
            for x in range(int(self.winX / self.tile_size.x)):
                pygame.draw.line(self.win, (255, 255, 255), (self.tile_size.x * x, 0),
                                 (self.tile_size.x * x, self.winY))

