import pygame

class Button:
    def __init__(self, x, y, width, height, text, inactive_color, active_color, action=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.inactive_color = inactive_color
        self.active_color = active_color
        self.font = pygame.font.Font(None, 36)
        self.active = False
        self.action = action

    def draw(self, screen):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if self.rect.collidepoint(mouse):
            pygame.draw.rect(screen, self.active_color, self.rect)
            self.active = True
            if click[0] == 1 and self.action is not None:
                self.action()
        else:
            pygame.draw.rect(screen, self.inactive_color, self.rect)
            self.active = False

        text_surface = self.font.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.center = self.rect.center
        screen.blit(text_surface, text_rect)

class Upgrade_button(Button):
    


# Example usage:
def button_action():
    print("Button Clicked!")

pygame.init()
screen = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()

button = Button(150, 100, 100, 50, "Click Me", (200, 100, 100), (200, 200, 200), action=button_action)

running = True
while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    button.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()


#Klass general button

#Wether

#Catle parts

#Wind
