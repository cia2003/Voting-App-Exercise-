from VotingApp.voting_service import VotingService
from VotingApp.voting_assets import AssetLoader
from VotingApp.voting_txt_img import *
from VotingApp.voting_buttons import *
import pygame as pg

## Idea by: Timothy Rudolf Tan
class VotingUi:
    def __init__(self) -> None:
        self.service = VotingService()
    
    def run(self):
        pg.init()

        # make base screen
        SCREEN = pg.display.set_mode((800, 500))
        pg.display.set_caption("Voting App")
        
        # load assets
        assets = AssetLoader()

        # initialize scenes
        scene_main_menu = SceneMainMenu(SCREEN, assets, self.service)
        scene_voting = SceneVoting(SCREEN, assets, self.service)

        # run the main loop
        current_scene = scene_main_menu

        running = True
        do_once = True

        while running:
            # set the background of the scene(s)
            if type(current_scene.background) != str:
                SCREEN.blit(current_scene.background, (0,0))
            else:
                SCREEN.fill(current_scene.background)

            if do_once:
                current_scene.do_once()
            do_once = False

            mouse_coords = pg.mouse.get_pos()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                elif event.type == pg.MOUSEBUTTONDOWN:
                    current_scene.play_mouse_click(mouse_coords)
            
            update_output = current_scene.update(SCREEN, mouse_coords)
            if update_output is not None:
                do_once = True
                if update_output == "menu_scene":
                    current_scene = scene_main_menu
                elif update_output == "voting_scene":
                    current_scene = scene_voting
            update_output = None
            
            pg.display.update()
            
###########################################################
class Scene():
    def __init__(self, screen, asset_loader: AssetLoader, _service: VotingService) -> None:
        self.service = _service
        self.subject_output = None
        self.screen = screen

    def do_once(self):
        self.subject_output = None

    def play_mouse_click(self):
        pass

    def update(self):
        if self.subject_output is not None:
            return self.subject_output
        
class SceneMainMenu(Scene):
    def __init__(self, screen, asset_loader: AssetLoader, _service: VotingService) -> None:
        super().__init__(screen, asset_loader, _service)

        # button(s)
        self.letsvoting_button = LetsVotingButton()
        # assets
        self.background = asset_loader.img_menu[0]
        self.buttons = [self.letsvoting_button]

    def do_once(self):
        self.subject_output = None

    def play_mouse_click(self, mouse_coords: tuple[int, int]):
        for button in self.buttons:
            if button.checkinput(mouse_coords) == True:
                if button.return_button_name() == "letsvotingbutton":
                    self.subject_output = "voting_scene"

    def update(self, screen, mouse_coords) -> (str|str):
        if self.subject_output is not None:
            return self.subject_output
        
        for button in self.buttons:
            button.change_appearence(mouse_coords)
            button.update(screen)

class SceneVoting(Scene):
    def __init__(self, screen, asset_loader: AssetLoader, _service: VotingService) -> None:
        super().__init__(screen, asset_loader, _service)

        # candidate's vote
        self.all_candidate_vote = self.count_all_voters()

        self.diana_vote = DianaVoteText(str(self.all_candidate_vote[0].vote))
        self.hans_vote = HansVoteText(str(self.all_candidate_vote[1].vote))
        self.niko_vote = NikoVoteText(str(self.all_candidate_vote[2].vote))

        # buttons
        self.back_button = BackButton()
        self.reset_button = ResetButton()
        self.diana_button = DianaButton(asset_loader.img_voting[0], asset_loader.img_voting[1])
        self.hans_button = HansButton(asset_loader.img_voting[4], asset_loader.img_voting[5])
        self.niko_button = NikoButton(asset_loader.img_voting[2], asset_loader.img_voting[3])

        # voting's assets
        self.background = "#f68500"
        self.buttons = [self.back_button, self.reset_button, self.diana_button, self.hans_button,
                        self.niko_button]
        self.texts_imgs = [self.diana_vote, self.hans_vote,self.niko_vote]

    def do_once(self):
        self.subject_output = None

    def play_mouse_click(self, mouse_coords: tuple[int, int]):
        for button in self.buttons:
            if button.checkinput(mouse_coords) == True:
                if button.return_button_name() == "backbutton":
                    self.subject_output = "menu_scene"
                elif button.return_button_name() == "resetbutton":
                    self.delete_all_vote()
                elif button.return_button_name() == "dianabutton":
                    self.increase_one_vote("Diana")
                elif button.return_button_name() == "hansbutton":
                    self.increase_one_vote("Hans")
                elif button.return_button_name() == "nikobutton":
                    self.increase_one_vote("Niko")

                self.all_candidate_vote = self.count_all_voters()
                for id in range(len(self.texts_imgs)):
                    self.texts_imgs[id].set_new_txt(str(self.all_candidate_vote[id].vote))

    def update(self, screen, mouse_coords) -> (str|str):
        if self.subject_output is not None:
            return self.subject_output
        
        self.all_candidate_vote = self.count_all_voters()
        for button in self.buttons:
            button.change_appearence(mouse_coords)
            button.update(screen)
        
        for txt_img in self.texts_imgs:
            txt_img.update(screen)

    def count_all_voters(self):
        return self.service.show_all_voters()
    
    def increase_one_vote(self, _name_candidate):
        return self.service.add_one_voting(_name_candidate)
    
    def delete_all_vote(self):
        return self.service.delete_all_vote()