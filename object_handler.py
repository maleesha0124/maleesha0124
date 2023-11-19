import pygame as pg
from sprite_object import AnimatedSprite
from npc import SoldierNPC, CacoDemonNPC, CyberDemonNPC
from random import choices
from object_renderer import *
from settings import *
from levels2 import mini_map_1, mini_map_2, mini_map_3, mini_map_final

RES = (WIDTH, HEIGHT)

# Define the ObjectHandler class
class ObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.npc_list = []
        self.npc_positions = {}

        # Level system
        self.current_level = 1
        self.levels = [
            {"map": mini_map_1, "sprites": [{"pos": (1.5, 1.5)}, {"pos": (1.5, 7.5)}, {"pos": (5.5, 3.25)}], "npcs": [{"class": SoldierNPC, "pos": (1.5, 15.5)}, {"class": SoldierNPC, "pos": (11.5, 30.5)}]},
            {"map": mini_map_2, "sprites": [{"pos": (0, 0)}, {"pos": (0, 0)}, {"pos": (0, 0)}], "npcs": [{"class": CacoDemonNPC, "pos": (1.5, 30.5)}, {"class": SoldierNPC, "pos": (7.5, 30.5)}]},
            {"map": mini_map_3, "sprites": [{"pos": (14.5, 24.5)}, {"pos": (14.5, 30.5)}, {"pos": (1.5, 30.5)}], "npcs": [{"class": CyberDemonNPC, "pos": (7.5, 15.5)}, {"class": SoldierNPC, "pos": (1.5, 30.5)}]},
            {"map": mini_map_final, "sprites": [{"pos": (10.5, 10.5)}, {"pos": (15.5, 15.5)}, {"pos": (5.5, 5.5)}], "npcs": [{"class": SoldierNPC, "pos": (1.5, 24.5)}, {"class": CacoDemonNPC, "pos": (7.5, 15.5)}, {"class": CyberDemonNPC, "pos": (14.5, 30.5)}]},
        ]
  
        self.load_level()

    def load_level(self):
        level_data = self.levels[self.current_level - 1]

        # Clear existing sprites and NPCs
        self.sprite_list = []
        self.npc_list = []
        self.player = []

        # Clear the old map
        self.game.map.clear_map()

        # Set the game map
        self.game.map.get_map(level_data.get("map", []))

        # Spawn sprites
        for sprite_data in level_data["sprites"]:
            self.add_sprite(AnimatedSprite(self.game, **sprite_data))

        # Spawn NPCs
        for npc_data in level_data["npcs"]:
            npc_class = npc_data.pop("class")
            npc = npc_class(self.game, **npc_data)
            self.add_npc(npc)
    
    def display_win_image(self):
        self.win_image = self.game.get_texture('resources/textures/win.png', RES)
        # display the win image here
    
    def display_level_image(self):
        self.level_image = self.game.get_texture('resources/textures/nextlevel.png', RES)
    
    def check_win(self):
        if not len(self.npc_positions):
            # Check if there are more levels
            if self.current_level < len(self.levels):
                self.current_level += 1
                self.load_level()
            else:
                # Display win image based on the current level
                if self.current_level <= 3:
                    self.game.object_renderer.nextlevel()
                    self.display_level_image()
             
                    pg.time.delay(1500)
                else:
                    # Add a default image or handle the case where there are more levels
                    self.game.object_renderer.win()
                
                self.display_win_image()
                pg.display.flip()
                pg.time.delay(1500)
                self.game.new_game()

    def update(self):
        self.npc_positions = {npc.map_pos for npc in self.npc_list if npc.alive}
    
        for sprite in self.sprite_list:
            sprite.update()
    
        for npc in self.npc_list:
            npc.update()

        self.check_win()

    def add_npc(self, npc):
        self.npc_list.append(npc)

    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)
