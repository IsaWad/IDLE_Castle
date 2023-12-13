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

class ImageButton(Button):
    def __init__(self, x, y, image_path, main_text, sub_text, main_font, sub_font, text_color, sub_text_color, action=None):
        image = image_path
        width, height = image.get_width(), image.get_height()
        super().__init__(x, y, width, height, main_text, (0, 0, 0, 0), (0, 0, 0, 0), action)
        self.image = image
        self.main_font = main_font
        self.sub_font = sub_font
        self.text_color = text_color
        self.sub_text = sub_text
        self.sub_text_color = sub_text_color

    def draw(self, screen):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if self.rect.collidepoint(mouse):
            screen.blit(self.image, self.rect)
            self.active = True
            if click[0] == 1 and self.action is not None:
                self.action()
        else:
            screen.blit(self.image, self.rect)
            self.active = False

        text_surface = self.main_font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

        sub_text_surface = self.sub_font.render(self.sub_text, True, self.sub_text_color)
        sub_text_rect = sub_text_surface.get_rect(midtop=(text_rect.centerx, text_rect.bottom + 5))  # Adjust the position
        screen.blit(sub_text_surface, sub_text_rect)



# Example usage:
def button_action():
    print("Button Clicked!")

# Enlarge by seven
def enlarge_by_seven(image):
    image_width, image_height = image.get_width(), image.get_height()
    image = pygame.transform.scale(image, (image_width * 7, image_height * 7))
    return(image)

#Klass general button

#Wether

#Catle parts

#Wind
