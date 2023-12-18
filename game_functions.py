import pygame
from castle_builder import *
from images import *
class Button:
    def __init__(self, x, y, width, height, text, inactive_color, active_color, action=None):
        # Initialize button properties
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.inactive_color = inactive_color
        self.active_color = active_color
        self.font = pygame.font.Font(None, 22)
        self.active = False
        self.action = action
    def draw(self, screen):
        # Get mouse position and click status
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        # Check if the mouse is over the button
        if self.rect.collidepoint(mouse):
            pygame.draw.rect(screen, self.active_color, self.rect)  # Draw active color if mouse is over the button
            self.active = True

            # Check for a click and execute the associated action
            if click[0] == 1 and self.action is not None:
                self.action()
        else:
            pygame.draw.rect(screen, self.inactive_color, self.rect)  # Draw inactive color if mouse is not over the button
            self.active = False

        # Render text surface and center it within the button's rectangular area
        text_surface = self.font.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.center = self.rect.center
        screen.blit(text_surface, text_rect)


class ImageButton(Button):
    def __init__(self, x, y, image_path, main_text, sub_text, main_font, sub_font, text_color, sub_text_color, action=None):
        # Initialize ImageButton properties
        image = image_path  # Image for the button
        width, height = image.get_width(), image.get_height()  # Get image dimensions
        super().__init__(x, y, width, height, main_text, (0, 0, 0, 0), (0, 0, 0, 0), action)  # Initialize the parent Button class
        self.image = image  # Store the image for the button
        self.main_font = main_font  # Font for the main text
        self.sub_font = sub_font  # Font for the sub text
        self.text_color = text_color  # Color for the main text
        self.sub_text = sub_text  # Sub text to be displayed below the main text
        self.sub_text_color = sub_text_color  # Color for the sub text
        self.clicked = False  # Flag to track if the button was clicked
        
    def draw(self, screen):
        mouse = pygame.mouse.get_pos()  # Get mouse position
        click = pygame.mouse.get_pressed()  # Get mouse click status

        # Check if the mouse is over the button
        if self.rect.collidepoint(mouse):
            screen.blit(self.image, self.rect)
            self.active = True
            # Check for a click and execute the associated action
            if click[0] == 1 and self.action is not None and not self.clicked:  # Check if it's the first click
                self.action()
                self.clicked = True
        else:
            screen.blit(self.image, self.rect)
            self.active = False
            if click[0] == 0:  # Reset the clicked flag if the mouse button is released
                self.clicked = False

        # Render and display the main text at the center of the button
        text_surface = self.main_font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

        # Render and display the sub text below the main text
        sub_text_surface = self.sub_font.render(self.sub_text, True, self.sub_text_color)
        sub_text_rect = sub_text_surface.get_rect(midtop=(text_rect.centerx, text_rect.bottom + 5))  # Adjust the position
        screen.blit(sub_text_surface, sub_text_rect)


# Enlarge by x times
def enlarge_by_x(image, x):
    image_width, image_height = image.get_width(), image.get_height()
    image = pygame.transform.scale(image, (image_width * x, image_height * x))
    return(image)

# Example usage:
def button_action():
    print("Button Clicked!")


# Draw japanese buttons
def button_japan(button_image, font1, font2, text_color, screen, player, ):
    # Each button displays information and upgrades respective part when clicked, except gold/treasury wich is a display that shows the amount of gold you have.
    player = player
    button1 = ImageButton(950, 40, button_image, f"{player.treasury}","Gold", font1, font2, text_color, text_color, action=button_action) #Tresury
    button2 = ImageButton(950, 110, button_image,"Main Keep", f"LVL:{player.mainKeepLVL} Price:{player.upgrading_price(player.mainKeepLVL + 1)}",font1, font2, text_color, text_color, action=lambda: player.upgrade_building("mainKeepLVL"))
    button3 = ImageButton(950, 180, button_image,"West Tower", f"LVL:{player.westTowerLVL} Price:{player.upgrading_price(player.westTowerLVL + 1)}",font1, font2, text_color, text_color, action=lambda: player.upgrade_building("westTowerLVL"))
    button4 = ImageButton(950, 250, button_image,"East Tower", f"LVL:{player.eastTowerLVL} Price:{player.upgrading_price(player.eastTowerLVL + 1)}",font1, font2, text_color, text_color, action=lambda: player.upgrade_building("eastTowerLVL"))
    button5 = ImageButton(950, 320, button_image,"Wall", f"LVL:{player.wallLVL} Price:{player.upgrading_price(player.wallLVL + 1)}",font1, font2, text_color, text_color, action=lambda: player.upgrade_building("wallLVL"))
    button6 = ImageButton(950, 390, button_image,"Dojo", f"LVL:{player.dojoLVL} Price:{player.upgrading_price(player.dojoLVL + 1)}",font1, font2, text_color, text_color, action=lambda: player.upgrade_building("dojoLVL"))
    button7 = ImageButton(950, 460, button_image,"Farm", f"LVL:{player.farmLVL} Price:{player.upgrading_price(player.farmLVL + 1)}",font1, font2, text_color, text_color, action=lambda: player.upgrade_building("farmLVL"))
    button8 = ImageButton(950, 530, button_image,"Weather",f"LVL:{player.weather} Price:{player.upgrading_price(player.weather + 1)}", font1, font2, text_color, text_color, action=lambda: player.upgrade_building("weather"))
    button1.draw(screen)
    button2.draw(screen)
    button3.draw(screen)
    button4.draw(screen)
    button5.draw(screen)
    button6.draw(screen)
    button7.draw(screen)
    button8.draw(screen)

# Draw european buttons
def button_europa(button_image, font1, font2, text_color, screen, player):
    # Each button displays information and upgrades respective part when clicked, except gold/treasury wich is a display that shows the amount of gold you have.
    button1 = ImageButton(950, 40, button_image, f"{player.treasury}", "Gold",font1, font2, text_color, text_color, action=button_action) #Tresury
    button2 = ImageButton(950, 110, button_image,"Main Keep", f"LVL:{player.mainKeepLVL} Price:{player.upgrading_price(player.mainKeepLVL+1)}",font1, font2, text_color, text_color, action=lambda: player.upgrade_building("mainKeepLVL"))
    button3 = ImageButton(950, 180, button_image,"West Tower", f"LVL:{player.westTowerLVL} Price:{player.upgrading_price(player.westTowerLVL + 1)}",font1, font2, text_color, text_color, action=lambda: player.upgrade_building("westTowerLVL"))
    button4 = ImageButton(950, 250, button_image,"East Tower", f"LVL:{player.eastTowerLVL} Price:{player.upgrading_price(player.eastTowerLVL+1)}",font1, font2, text_color, text_color, action=lambda: player.upgrade_building("eastTowerLVL"))
    button5 = ImageButton(950, 320, button_image,"Wall", f"LVL:{player.wallLVL} Price:{player.upgrading_price(player.wallLVL+1)}",font1, font2, text_color, text_color, action=lambda: player.upgrade_building("wallLVL"))
    button6 = ImageButton(950, 390, button_image,"Gate", f"LVL:{player.gateLVL} Price:{player.upgrading_price(player.gateLVL+1)}",font1, font2, text_color, text_color, action=lambda: player.upgrade_building("gateLVL"))
    button7 = ImageButton(950, 460, button_image,"Farm", f"LVL:{player.farmLVL} Price:{player.upgrading_price(player.farmLVL+1)}",font1, font2, text_color, text_color, action=lambda: player.upgrade_building("farmLVL"))
    button8 = ImageButton(950, 530, button_image,"Weather", f"LVL:{player.weather} Price:{player.upgrading_price(player.weather+1)}",font1, font2, text_color, text_color, action=lambda: player.upgrade_building("weather"))
    button1.draw(screen)
    button2.draw(screen)
    button3.draw(screen)
    button4.draw(screen)
    button5.draw(screen)
    button6.draw(screen)
    button7.draw(screen)
    button8.draw(screen)

def quit_button(screen):
    # Creates a button, when clicked it quits the game
    quit_button = Button(0, 0, 35, 35, "EXIT", (200, 100, 100), (200, 200, 200), action=pygame.quit)
    quit_button.draw(screen)

  
def scene(player, scenario, screen):
    # Shows diffrent images deppending on the level of the diffrent parts of the castle and deppending on if the scenario is set to Europa or Japan.

    # Weather    
    if player.weather == 1:
        screen.blit(enlarge_by_x(weather_LVL1_image, 7),(0, 35))
    elif player.weather == 2:
        screen.blit(enlarge_by_x(weather_LVL2_image, 7), (0, 35))
    
    
    if scenario == "japan":
        # Weather and landsape
        final_imadge = enlarge_by_x(weater_LVL3_japan_image, 7)
        landscape = enlarge_by_x(landscape_japan_image, 7)
        if player.weather >= 3:
            screen.blit(final_imadge, (0,35))
        screen.blit(landscape, (0, 35))
        # Castle
        if player.mainKeepLVL >= 1:
            screen.blit(enlarge_by_x(main_keep_japan_image, 7), (0, 35))
        if player.westTowerLVL >= 1:
            screen.blit(enlarge_by_x(west_tower_japan_image, 7), (0, 35))
        if player.eastTowerLVL >= 1:
            screen.blit(enlarge_by_x(east_tower_japan_image, 7), (0, 35))
        if player.wallLVL >= 1:
            screen.blit(enlarge_by_x(wall_japan_image, 7), (0, 35))
        if player.dojoLVL >= 1:
            screen.blit(enlarge_by_x(dojo_japan_image, 7), (0, 35))
        if player.farmLVL >= 1:
            screen.blit(enlarge_by_x(fishery, 7), (0, 35))

    elif scenario == "europa":
        # Weather and landsape
        final_imadge = enlarge_by_x(weather_LVL3_europa_image, 7)
        landscape = enlarge_by_x(landscape_europa_image, 7)
        if player.weather >= 3:
            screen.blit(final_imadge, (0,35))
        screen.blit(landscape, (0,35))
        # Castle
        if player.mainKeepLVL >= 1:
            if player.gateLVL >= 1:
                screen.blit(enlarge_by_x(main_keep_europa_image, 7), (100, 35))
            else:
                screen.blit(enlarge_by_x(main_keep_europa_image, 7), (100, 175))
        if player.westTowerLVL >= 1:
            screen.blit(enlarge_by_x(west_tower_europa_image, 7), (100, 35))
        if player.eastTowerLVL >= 1:
            screen.blit(enlarge_by_x(east_tower_europa_image, 7), (100, 35))
        if player.wallLVL >= 1:
            screen.blit(enlarge_by_x(wall_europa_image, 7), (100, 35))
        if player.gateLVL >= 1:
            screen.blit(enlarge_by_x(gate_europa_image, 7), (100, 35))
        if player.farmLVL >= 1:
            screen.blit(enlarge_by_x(windmill, 7), (50, 35))



