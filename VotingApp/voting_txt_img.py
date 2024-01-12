import pygame as pg
pg.init()

class TextAsset():
     def __init__(self, text_input, pos, font, base_color) -> None:
          self.x_pos = pos[0]
          self.y_pos = pos[1]
          self.font = font
          self.text_input = text_input
          self.base_color = base_color
          self.text = self.font.render(self.text_input, True, self.base_color)
          self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

     def update(self, screen):
          screen.blit(self.text, self.text_rect)

     def set_new_txt(self, new_input):
          self.text_input = new_input
          self.text = self.font.render(new_input, True, self.base_color)

# registration's text
class DianaVoteText(TextAsset):
     def __init__(self, text_input, pos=(169, 352), font=pg.font.SysFont("Times New Roman", 35), base_color="#d7fcd4") -> None:
          super().__init__(text_input, pos, font, base_color) 

class HansVoteText(TextAsset):
     def __init__(self, text_input, pos=(420, 352), font=pg.font.SysFont("Times New Roman", 35), base_color="#d7fcd4") -> None:
          super().__init__(text_input, pos, font, base_color)  

class NikoVoteText(TextAsset):
     def __init__(self, text_input, pos=(679, 352),  font=pg.font.SysFont("Times New Roman", 35), base_color="#d7fcd4") -> None:
          super().__init__(text_input, pos, font, base_color) 