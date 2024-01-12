import os
import pygame as pg

class AssetLoader():
    def __init__(self):
        self.main_dir = os.path.split(os.path.abspath(__file__))[0]
        self.assets_dir = os.path.join(self.main_dir, "assets")

        # Main menu's assets
        self.img_menu = [self.load_image("bg_desain.png")]

        # Voting's assets
        self.img_voting = [self.load_image("diana.png"),
                           self.load_image("diana_cover.png"),
                           self.load_image("niko.png"),
                           self.load_image("niko_cover.png"),
                           self.load_image("hans.png"),
                           self.load_image("hans_cover.png")]
    
    def load_image(self, file_name: str):
        file_path = os.path.join(self.assets_dir, file_name)
        surface = pg.image.load(file_path)
        return surface
