import random
import pygame
import sys

import SPRNVA as sprnva
from SPRNVA import Vector
from generate_terrain import Terrain, TileMap
from debug import Grid

class Main:
    def __init__(self):
        self.win_size = (1280, 720)
        self.win = pygame.display.set_mode(self.win_size, pygame.RESIZABLE, vsync=1)
        self.fps = 60
        self.clock = pygame.time.Clock()
        self.debug = False
        self.tile_size = Vector(32, 32)


        self.player_vel = Vector(3, 3)
        self.friction = 1
        self.player = sprnva.Player(self.win, Vector(50, 50), Vector(self.tile_size.x, self.tile_size.y*2))

        self.max_room_count = 5
        self.min_room_size = Vector(5, 5)
        self.max_room_size = Vector(10, 10)
        self.room_exits = random.randint(1, 3)

        # TODO generate this procedual
        self.tile_map = []
        for i in range(self.max_room_count):
            room = TileMap(self.min_room_size, self.max_room_size).generate_room(self.room_exits)
            self.tile_map.append(room)

        self.tiles = Terrain(self.win, self.tile_size, self.tile_map).generate()

    def update(self):
        tgl_debug = 0

        while True:
            self.win.fill((0, 0, 0))
            keys = pygame.key.get_pressed()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.VIDEORESIZE:
                    self.win_size = (event.w, event.h)
                    self.win = pygame.display.set_mode(self.win_size, pygame.RESIZABLE, vsync=1)

            if keys[pygame.K_q]:
                if tgl_debug == 0:
                    self.debug = True
                    tgl_debug = 1
                elif tgl_debug == 1:
                    self.debug = False
                    tgl_debug = 0

            if keys[pygame.K_w]:
                self.player.move(self.tiles, self.player_vel, minus_y=True)

            elif keys[pygame.K_s]:
                self.player.move(self.tiles, self.player_vel, y=True)

            if keys[pygame.K_a]:
                self.player.move(self.tiles, self.player_vel, minus_x=True)

            elif keys[pygame.K_d]:
                self.player.move(self.tiles, self.player_vel, x=True)

            for tile in self.tiles:
                if self.debug:
                    pygame.draw.rect(self.win, (0, 255, 0), pygame.Rect(tile.x, tile.y, tile.width, tile.height))
                else:
                    pygame.draw.rect(self.win, (0, 255, 0), tile)

            if self.debug:
                Grid(self.win, self.tile_size).draw()

            self.player.draw()
            pygame.display.flip()
            self.clock.tick(self.fps)

if __name__ == '__main__':
    Main().update()
