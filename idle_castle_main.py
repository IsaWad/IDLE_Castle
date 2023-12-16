from game_functions import *
from images import *
import pygame
text = "Click Me"
text_color = (255, 255, 255)
start = True
player = None
pygame.init()

screen = pygame.display.set_mode([1120, 630])
font = pygame.font.Font(None, 30)
font2 = pygame.font.Font(None, 15)

def button_scenario(button_image, font1, text_color, screen):
    button_europa = ImageButton(950, 40, button_image,"Europa", "", font1, font1, text_color, text_color, action=start_europa)
    button_japan = ImageButton(950, 110, button_image,"Japan", "", font1, font1, text_color, text_color, action=start_japan)
    button_europa.draw(screen)
    button_japan.draw(screen)

def start_japan():
    global start
    global scenario
    global player
    scenario = "japan"
    start = False
    player = JapaneseCastle()
def start_europa():
    global start
    global scenario
    global player
    scenario = "europa"
    start = False
    player = EuropeanCastle()
# Enlarge the image by eight times
enlarged_image = enlarge_by_x(frame_image, 7)
button_image = enlarge_by_x(button_image, 7)

running = True
tick = 0
tax = 5
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
    x, y = 0, 0

    screen.blit(enlarged_image, (x, y))

    
    if start:
        button_scenario(button_image, font, text_color, screen)
    else:
        if scenario == "japan":
            button_japan(button_image, font, font2, text_color, screen, player, tax)
            tax += player.tax(tick)
        elif scenario == "europa":
            button_europa(button_image, font, font2, text_color, screen, player, tax)
            tax += player.tax(tick)
    

    tick +=1
        
    pygame.display.update()

#pygame.quit()