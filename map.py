import pygame as pg
#from levels import mini_ma
from levels import *
from object_handler import *


MINI_MAP_SCALE = (10,10)

class Map:
    def __init__(self, game, map):
        self.game = game
        self.mini_map = map
        self.world_map = {}
        self.rows = len(self.mini_map)
        self.cols = len(self.mini_map[0])
        self.get_map()

    def get_map(self, map_data=None):
        if map_data is None:
            map_data = self.mini_map

        for j, row in enumerate(map_data):
            for i, value in enumerate(row):
                if value:
                    self.world_map[(i, j)] = value
                    
    
    # Inside the Map class in map.py
    def clear_map(self):
        self.world_map = {}

    
    #def draw(self):
        # Draw the map elements
        #[pg.draw.rect(self.game.screen, 'darkgray', (pos[0] * 10, pos[1] * 10, 10, 10), 2)
       #  for pos in self.world_map]
        

    def draw(self):
        mini_map_scale = 10  # Adjust the scale as needed
        mini_map_offset = (self.game.screen.get_width() - self.cols * mini_map_scale, 0)
        mini_map_size = (self.cols * mini_map_scale, self.rows * mini_map_scale)

        # Draw the background rectangle
        pg.draw.rect(self.game.screen, (50, 50, 50), (mini_map_offset[0], mini_map_offset[1], mini_map_size[0], mini_map_size[1]))


        for pos, value in self.world_map.items():
            mini_map_x = pos[0] * mini_map_scale + mini_map_offset[0]
            mini_map_y = pos[1] * mini_map_scale + mini_map_offset[1]
            pg.draw.rect(self.game.screen, 'darkgray', (mini_map_x, mini_map_y, mini_map_scale, mini_map_scale), 2)

        # Draw the player marker on the mini-map
        player = self.game.player
        player_mini_map_x = int(player.x * mini_map_scale) + mini_map_offset[0]
        player_mini_map_y = int(player.y * mini_map_scale) + mini_map_offset[1]
        pg.draw.circle(self.game.screen, (255, 0, 0), (player_mini_map_x, player_mini_map_y), 5)
