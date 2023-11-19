from settings import *
from Newmenu import *
import pygame as pg
import sys
import math
from map import *
from player import *
from raycasting import *
from object_renderer import *
from sprite_object import *
from object_handler import *
from weapon import *
from sound import *
from pathfinding import *



class Game:
    def __init__(self):
        pg.init()
        pg.mouse.set_visible(False)
        self.screen = pg.display.set_mode(RES)
        self.width, self.height = RES # difine for normel weapons aims
        pg.event.set_grab(True)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.global_trigger = False
        self.global_event = pg.USEREVENT + 0
        pg.time.set_timer(self.global_event, 40)
        self.player_x = 0
        self.player_y = 0
        self.new_game()

        #self.mini_map = MiniMap(self)  # Create an instance of the MiniMap class
        #level images


    def draw_crosshair(self):
    # Set default color for other weapons
        color = (255, 255, 255, 200)  # Set RGBA values with some transparency

    # Check the current weapon and draw the different Aim for specific weapon
        if self.weapon.current_weapon_type == 'shotgun':
        # Draw a pulsating circle in the middle
            circle_radius = 20 + int(5 * math.sin(pg.time.get_ticks() * 0.005))  # Pulsating effect
            circle_thickness = 2
            pg.draw.circle(self.screen, (255, 255, 255), (HALF_WIDTH, HALF_HEIGHT), circle_radius, circle_thickness)
            
            
        
        elif self.weapon.current_weapon_type == 'machine gun':
            circle_radius = 30 + int(5 * math.sin(pg.time.get_ticks() * 0.010))  # Pulsating effect
            circle_thickness = 2
            pg.draw.circle(self.screen, (0, 255, 0), (HALF_WIDTH, HALF_HEIGHT), circle_radius, circle_thickness)
            
             # Draw a transparent center
            pg.draw.circle(self.screen, (255, 0, 0, 0), (HALF_WIDTH , HALF_HEIGHT ), 2)  # Adjust the radius as needed
              
        
        else:
        # Draw vertical lines with space in the middle
          pg.draw.line(self.screen, (255, 255, 255), (self.width // 2 - 20, self.height // 2), (self.width // 2 - 5, self.height // 2), 2)
          pg.draw.line(self.screen, (255, 255, 255), (self.width // 2 + 5, self.height // 2), (self.width // 2 + 20, self.height // 2), 2)

        # Draw horizontal lines with space in the middle
          pg.draw.line(self.screen, (255, 255, 255), (self.width // 2, self.height // 2 - 20), (self.width // 2, self.height // 2 - 5), 2)
          pg.draw.line(self.screen, (255, 255, 255), (self.width // 2, self.height // 2 + 5), (self.width // 2, self.height // 2 + 20), 2)
          
          
    def get_texture(self, path, res=(TEXTURE_SIZE, TEXTURE_SIZE)):
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, res)
    
    
    def new_game(self):
        # Create an instance of the mini_map_1 class
        self.map = Map(self, mini_map_1)
        self.player = Player(self)
        self.object_renderer = ObjectRenderer(self)
        self.raycasting = RayCasting(self)
        self.object_handler = ObjectHandler(self)
        self.weapon = Weapon(self)
        self.sound = Sound(self)
        self.pathfinding = PathFinding(self)
        pg.mixer.music.play(-1)
        
   

    def update(self):
        self.player.update()
        self.raycasting.update()
        self.object_handler.update()
        self.weapon.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.object_renderer.draw()
        self.weapon.draw()
        #self.mini_map.draw()  # draw mini map
        self.draw_crosshair()  # Add this line to draw the crosshair
        self.map.draw() #2d map
       # self.player.draw() #2d map
        pg.display.flip()

    def check_events(self):
        self.global_trigger = False
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
               pygame.quit()
               sys.exit()
            elif event.type == self.global_event:
                self.global_trigger = True
            self.player.single_fire_event(event)
            

    
    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()
            


if __name__ == '__main__':
    game = Game()
    game.run()
