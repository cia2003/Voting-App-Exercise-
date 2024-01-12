import pygame as pg
pg.init()

# Source: https://youtu.be/al_V4OGSvFU?si=CGZIYrNVavZV_z_y
class Button():
    def __init__(self, image, hovering_image, pos, text_input, font, base_color, hovering_color):
        self.old_image = image
        self.base_image = image
        self.hovering_image = hovering_image

        self.x_pos = pos[0]
        self.y_pos = pos[1]

        self.font = font

        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)

        if self.base_image is None:
            self.base_image = self.text
        self.rect = self.base_image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
    
    def update(self, screen):
        if self.base_image is not None:
            screen.blit(self.base_image, self.rect)
        screen.blit(self.text, self.text_rect)
    
    def checkinput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False
    
    def change_appearence(self, position):
        if self.base_image is not None:
            if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                self.base_image = self.hovering_image
            else:
                self.base_image = self.old_image

        else:
            if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                self.text = self.font.render(self.text_input, True, self.hovering_color)
            else:
                self.text = self.font.render(self.text_input, True, self.base_color)
    
    def return_button_name(self):
        pass

# main menu's button(s)
class LetsVotingButton(Button):
    def __init__(self, image=None, hovering_image= None,pos=(400, 360), text_input="LET'S VOTE", font=pg.font.SysFont("cambria", 40), base_color="#f29804", hovering_color="black"):
        super().__init__(image, hovering_image, pos, text_input, font, base_color, hovering_color)

    def return_button_name(self):
        return "letsvotingbutton"
    
# voting's button(s)
class DianaButton(Button):
    def __init__(self, image, hovering_image, pos=(169, 222), text_input=None, font=pg.font.SysFont("Times New Roman", 75), base_color="#d7fcd4", hovering_color="white"):
        super().__init__(image, hovering_image, pos, text_input, font, base_color, hovering_color)
    
    def return_button_name(self):
        return "dianabutton"
    
class NikoButton(Button):
    def __init__(self, image, hovering_image, pos=(669, 222), text_input=None, font=pg.font.SysFont("Times New Roman", 75), base_color="#d7fcd4", hovering_color="white"):
        super().__init__(image, hovering_image, pos, text_input, font, base_color, hovering_color)

    def return_button_name(self):
        return "nikobutton"
    
class HansButton(Button):
    def __init__(self, image, hovering_image, pos=(420, 222), text_input=None, font=pg.font.SysFont("Times New Roman", 75), base_color="#d7fcd4", hovering_color="white"):
        super().__init__(image, hovering_image, pos, text_input, font, base_color, hovering_color)
        self.click_count = 0
    
    def return_button_name(self):
        return "hansbutton"
    
class BackButton(Button):
    def __init__(self, image=None, hovering_image=None, pos=(100, 450), text_input="BACK", font=pg.font.SysFont("Times New Roman", 35), base_color="#d7fcd4", hovering_color="black"):
        super().__init__(image, hovering_image, pos, text_input, font, base_color, hovering_color)

    def return_button_name(self):
        return "backbutton"
    
class ResetButton(Button):
    def __init__(self, image=None, hovering_image=None, pos=(700, 450), text_input="RESET", font=pg.font.SysFont("Times New Roman", 35), base_color="#d7fcd4", hovering_color="black"):
        super().__init__(image, hovering_image, pos, text_input, font, base_color, hovering_color)

    def return_button_name(self):
        return "resetbutton"