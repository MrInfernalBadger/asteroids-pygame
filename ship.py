import pygame
import math
from pygame.locals import RLEACCEL

class Ship(pygame.sprite.Sprite):
    def __init__(self, WIDTH, HEIGHT):
        super(Ship, self).__init__()
               
        self.ship_shape = [(0, 20), (-10, -20), (10, -20)]
        
        self.x = WIDTH / 2
        self.y = HEIGHT / 2
        
        self.acceleration = 0.4       
        self.dx = 0
        self.dy = 0
        # self.vector = (0, 0)
        self.screen_width = WIDTH
        self.screen_height = HEIGHT
        
        self.angle = 0
        
        self.speed = 1
        self.max_speed = 20
        
    def update(self):
        """Updates the position of the points that make up the ship
        Position, rotation, if off screen, resets ship to bottom/side/top
        """
        # self.update_movement_vector()
        
        # Check that max speed will not be exceeded
        if(self.dx > self.max_speed):
            self.dx = self.max_speed
        if(self.dx < -self.max_speed):
            self.dx = -self.max_speed
            
        if(self.dy > self.max_speed):
            self.dy = self.max_speed
        if(self.dy < -self.max_speed):
            self.dy = -self.max_speed
        
        # Change position based on current dx dy values
        self.x += self.dx
        self.y += self.dy
        
        if self.x > self.screen_width:
            self.x -= self.screen_width
        if self.x < 0:
            self.x += self.screen_width
            
        if self.y > self.screen_height:
            self.y -= self.screen_height
        if self.y < 0:
            self.y += self.screen_height
            
    def adjust_vector_rotation(self, ship):
        result = []
        angle = math.radians(self.angle)
        for point in ship:
            new_x = (point[0] * math.cos(angle)) - (point[1] * math.sin(angle))
            new_y = (point[1] * math.cos(angle)) + (point[0] * math.sin(angle))
            result.append((new_x, new_y))
        return result
    
    def adjust_vector_position(self, ship):
        true_position = []
        for point in ship:
            new_x = point[0] + self.x
            new_y = point[1] + self.y
            true_position.append((new_x, new_y))
            
        return true_position
    
    
    # def update_movement_vector(self):
    #     vx = math.cos(self.angle) * self.speed
    #     vy = math.sin(self.angle) * self.speed

    #     self.vector = (vx, vy)
        
    def draw(self, screen):
        ship = self.adjust_vector_rotation(self.ship_shape)
        ship = self.adjust_vector_position(ship)
        
        pygame.draw.polygon(screen, (255, 255, 255), ship)
        
        # rotated_self = pygame.transform.rotate(self.surf, self.angle)
        # surface.blit(rotated_self, (self.x, self.y))
        # surface.blit(self.surf, (self.x, self.y))