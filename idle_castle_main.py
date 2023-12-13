import py_game
import catlebuilder
import pygame
text = "Click Me"
text_color = (255, 255, 255)
start = True
pygame.init()
screen = pygame.display.set_mode([1120, 630])
original_image = pygame.image.load('.\\Images\\Frame.png')
button_image = pygame.image.load('.\\Images\\MenueButton2.png')
font = pygame.font.Font(None, 30)
font2 = pygame.font.Font(None, 15)




# Enlarge the image by eight times
enlarged_image = py_game.enlarge_by_seven(original_image)
button_image = py_game.enlarge_by_seven(button_image)
button1 = py_game.ImageButton(950, 40, button_image,"hej","på",font, font2, text_color, text_color, action=py_game.button_action)
button2 = py_game.ImageButton(950, 110, button_image,"hej","på",font, font2, text_color, text_color, action=py_game.button_action)
button3 = py_game.ImageButton(950, 180, button_image,"hej","på",font, font2, text_color, text_color, action=py_game.button_action)
button4 = py_game.ImageButton(950, 250, button_image,"hej","på",font, font2, text_color, text_color, action=py_game.button_action)
button5 = py_game.ImageButton(950, 320, button_image,"hej","på",font, font2, text_color, text_color, action=py_game.button_action)
button6 = py_game.ImageButton(950, 390, button_image,"hej","på",font, font2, text_color, text_color, action=py_game.button_action)
button7 = py_game.ImageButton(950, 460, button_image,"hej","på",font, font2, text_color, text_color, action=py_game.button_action)
button8 = py_game.ImageButton(950, 530, button_image,"hej","på",font, font2, text_color, text_color, action=py_game.button_action)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
    x, y = 0, 0
    screen.blit(enlarged_image, (x, y))
    if start:
        button1.draw(screen)
        button2.draw(screen)
        button3.draw(screen)
        button4.draw(screen)
        button5.draw(screen)
        button6.draw(screen)
        button7.draw(screen)
        button8.draw(screen)

        
    pygame.display.update()

#pygame.quit()
