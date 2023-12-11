import pygame

pygame.init()
screen = pygame.display.set_mode([1120, 630])
original_image = pygame.image.load('.\\Images\\Frame.png')

original_width, original_height = original_image.get_width(), original_image.get_height()

# Enlarge the image by eight times
enlarged_image = pygame.transform.scale(original_image, (original_width * 7, original_height * 7))
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    x, y = 0, 0
    screen.blit(enlarged_image, (x, y))

    pygame.display.update()

#pygame.quit()
