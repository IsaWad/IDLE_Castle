from game_functions import *
from images import *
import pygame
text = "Click Me"
text_color = (255, 255, 255)
start = True
player = None

pygame.init()
pygame.mixer.init()
music_files_europa = ['.\\music\\Battotai - Imperial Japanese Army March.mp3', '.\\music\\beethoven-moonlight-sonata-1-movement-op-27-nr-2.mp3']
current_track = 0
pygame.mixer.music.load(music_files_europa[current_track])
pygame.mixer.music.play()

screen = pygame.display.set_mode([1120, 630])
font = pygame.font.Font(None, 30)
font2 = pygame.font.Font(None, 15)

def button_scenario(button_image, font1, text_color, screen):
    button_information = ImageButton(950, 40, button_image,"Shoose", "Region", pygame.font.Font(None, 20), pygame.font.Font(None, 20), text_color, text_color, action=None)
    button_europa = ImageButton(950, 110, button_image,"Europa", "", font1, font1, text_color, text_color, action=start_europa)
    button_japan = ImageButton(950, 180, button_image,"Japan", "", font1, font1, text_color, text_color, action=start_japan)
    button_information.draw(screen)
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
#tax = 5
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

        # Add a short delay to reduce CPU usage
    #time.sleep(0.1)

    x, y = 0, 0

    
    #screen.blit(enlarge_by_x(weather_LVL2_image, 7),(0, 35))


    if start:
        screen.blit(enlarged_image, (x, y))
        button_scenario(button_image, font, text_color, screen)
    else:
        if scenario == "japan":
            scene(player,scenario, screen)
            screen.blit(enlarged_image, (x, y))
            button_japan(button_image, font, font2, text_color, screen, player)
            player.treasury += player.tax(tick)
            
            
        elif scenario == "europa":
            scene(player,scenario, screen)
            screen.blit(enlarged_image, (x, y))
            button_europa(button_image, font, font2, text_color, screen, player)
            player.treasury += player.tax(tick)

    quit_button(screen)
            
            
    
    clock.tick(FPS)
    tick +=1
        
    pygame.display.update()

pygame.quit()