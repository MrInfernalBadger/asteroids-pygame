import pygame
import math
from ship import Ship


pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


WIDTH = 1200
HEIGHT = 800
FPS = 30

screen = pygame.display.set_mode((WIDTH, HEIGHT))
surface = pygame.Surface((WIDTH, HEIGHT))
pygame.display.set_caption("Asteroids")
clock = pygame.time.Clock()

# roids = pygame.sprite.group()
# bullets = pygame.sprite.group()
    
        
player = Ship(WIDTH, HEIGHT)

# Display text on the screen for testing
font = pygame.font.Font('freesansbold.ttf', 32)


text = []
def update_text():
    text = [
        ["Angle: ", player.angle],
        # ["dx: ", player.dx],
        # ["dy: ", player.dy],
        # ["Sinθ ", math.sin(player.angle)],
        # ["Cosθ ", math.cos(player.angle)],
    ]
    return text


def draw_text(text):
    pos = 0
    for item in text:
        string = item[0] + str(item[1])        
        item = font.render(string, True, WHITE)
        itemRect = item.get_rect()
        itemRect.topleft = (5, pos*32)
        item = font.render(string, True, WHITE)
        screen.blit(item, itemRect)
        pos += 1

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    

    if keys[pygame.K_UP]:
        player.dx -= math.sin(math.radians(player.angle)) * player.speed
        player.dy += math.cos(math.radians(player.angle)) * player.speed
        
    if keys[pygame.K_DOWN]:
        player.dx += math.sin(math.radians(player.angle)) * player.speed
        player.dy -= math.cos(math.radians(player.angle)) * player.speed
        
    if keys[pygame.K_LEFT]:
        player.angle -= 8

        
    if keys[pygame.K_RIGHT]:
        player.angle += 8

            
            
    clock.tick(FPS)
    
    screen.fill(BLACK)    
    
    player.update()
    player.draw(screen)


    text = update_text()
    draw_text(text)
    pygame.display.flip()
    
pygame.quit()


# TODO create list of rotations for each object to save CPU time
# TODO create list of x/y vectors for each angle to save CPU time
# TODO refactor the vector calulation to a separate function, combine dx and dy into a single value as they are always used together