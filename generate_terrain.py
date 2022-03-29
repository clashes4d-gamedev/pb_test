import pygame
import SPRNVA as sprnva
from SPRNVA import Vector
#debug
import random
import time

class TileMap:
    def __init__(self, min_room_size: Vector, max_room_size: Vector):
        self.min_room_width = min_room_size.x
        self.min_room_height = min_room_size.y

        self.max_room_width = max_room_size.x
        self.max_room_height = max_room_size.y

    def generate_room(self, num_exit: int):
        level_room = []
        exit_walls = ['LEFT', 'RIGHT', 'TOP', 'BOTTOM']
        room_height = random.randint(int(self.min_room_height), int(self.max_room_height))
        room_width = random.randint(int(self.min_room_width), int(self.max_room_width))

        for y in range(room_height):
            level_room.append([])
            x = 0
            for x in range(room_width):
                if y == 0:
                    level_room[y].append('1')

                elif y+1 == room_height:
                    level_room[y].append('1')

                else:
                    if x == 0:
                        level_room[y].append('1')

                    elif x+1 == room_width:
                        level_room[y].append('1')

                    else:
                        level_room[y].append('0')

                x += 1
            y += 1

        for i in range(num_exit):
            exit_wall = random.choice(exit_walls)
            if exit_wall == 'LEFT':
                exit_walls.remove('LEFT')
                exit_height = random.randint(0, room_height - 3)
                level_room[exit_height][0] = '0'
                level_room[exit_height + 1][0] = '0'
                level_room[exit_height + 2][0] = '0'

            elif exit_wall == 'RIGHT':
                exit_walls.remove('RIGHT')
                exit_height = random.randint(0, room_height - 3)
                level_room[exit_height][room_width - 1] = '0'
                level_room[exit_height + 1][room_width - 1] = '0'
                level_room[exit_height + 1][room_width - 2] = '0'

            elif exit_wall == 'TOP':
                exit_walls.remove('TOP')
                exit_width = random.randint(0, room_width - 3)
                level_room[0][exit_width] = '0'
                level_room[0][exit_width + 1] = '0'
                level_room[0][exit_width + 3] = '0'

            elif exit_wall == 'BOTTOM':
                exit_walls.remove('BOTTOM')
                exit_width = random.randint(0, room_width - 3)
                level_room[room_height - 1][exit_width] = '0'
                level_room[room_height - 1][exit_width + 1] = '0'
                level_room[room_height - 1][exit_width + 2] = '0'

        return level_room


class Terrain:
    def __init__(self, win: pygame.Surface, tile_size: Vector, tile_map: list):
        self.win = win
        self.tile_width = tile_size.x
        self.tile_height = tile_size.y
        self.tile_map = tile_map

    def generate(self):
        x = 0
        y = 0
        rm_count = 0
        tiles = []
        for room in self.tile_map:
            for row in room:
                x = 0
                for col in row:
                    if col == '1':
                        tile = pygame.Rect(self.tile_width * x, self.tile_height * y, self.tile_width, self.tile_height)
                        pygame.display.update()
                        tiles.append(tile)
                    elif col == '0':
                        pass
                    x += 1
                y += 1

        return tiles
