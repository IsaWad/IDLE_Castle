from game_functions import *
from images import *
import pygame
# Constants
text_color = (255, 255, 255)
x, y = 0, 0
music_files_europa = ['.\\music\\beethoven-moonlight-sonata-1-movement-op-27-nr-2.mp3', '.\\music\\Battotai - Imperial Japanese Army March.mp3']

# Initiates pygames
pygame.init()
# Initiates music
pygame.mixer.init()
current_track = 0
pygame.mixer.music.load(music_files_europa[current_track])
pygame.mixer.music.play()

# Screen dimensions and fonts
screen = pygame.display.set_mode([1120, 630])
font = pygame.font.Font(None, 30)
font2 = pygame.font.Font(None, 15)

# This function is used to create the buttons where you can shoose Japan or Europa, one of the "buttons" is used a text displayer.
def button_scenario(button_image, font1, text_color, screen):
    button_information = ImageButton(950, 40, button_image,"Shoose", "Region", pygame.font.Font(None, 20), pygame.font.Font(None, 20), text_color, text_color, action=None) # Displays text
    button_europa = ImageButton(950, 110, button_image,"Europa", "", font1, font1, text_color, text_color, action=start_europa)
    button_japan = ImageButton(950, 180, button_image,"Japan", "", font1, font1, text_color, text_color, action=start_japan)
    button_information.draw(screen)
    button_europa.draw(screen)
    button_japan.draw(screen)

# When button Japan is clicked
def start_japan():
    global start
    global scenario
    global player
    scenario = "japan"
    start = False
    player = JapaneseCastle()# Creats the class JapaneesCastle

# When button Europa is clicked
def start_europa():
    global start
    global scenario
    global player
    scenario = "europa"
    start = False
    player = EuropeanCastle()# Creats the class CuropeanCastle

enlarged_frame_image = enlarge_by_x(frame_image, 7)
button_image = enlarge_by_x(button_image, 7)

running = True
start = True
player = None
tick = 0
clock = pygame.time.Clock()
FPS = 8
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    if not pygame.mixer.music.get_busy():
        # Move to the next track
        current_track = (current_track + 1) % len(music_files_europa)
        pygame.mixer.music.load(music_files_europa[current_track])
        pygame.mixer.music.play()

    if start:
        screen.blit(enlarged_frame_image, (x, y))
        button_scenario(button_image, font, text_color, screen)
        
    else:
        if scenario == "japan":
            scene(player,scenario, screen)
            screen.blit(enlarged_frame_image, (x, y))
            button_japan(button_image, font, font2, text_color, screen, player)
            player.treasury += player.tax(tick)    
            
        elif scenario == "europa":
            scene(player,scenario, screen)
            screen.blit(enlarged_frame_image, (x, y))
            button_europa(button_image, font, font2, text_color, screen, player)
            player.treasury += player.tax(tick)

    quit_button(screen)
            
            
    
    clock.tick(FPS)
    tick +=1
        
    pygame.display.update()

pygame.quit()