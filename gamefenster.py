import sys
import pygame
from button import Button
from character_selection import Character_Selection_Screen



class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Das echte Fortnite')
        self.screen = pygame.display.set_mode((960, 540))
        self.clock = pygame.time.Clock()
        self.background = pygame.transform.scale(pygame.image.load('.\\Images\\hintergrund type ebat.png'), (self.screen.get_width(), self.screen.get_height()))
        

        #self.start_menu = Start_Menu_Screen()
        self.character_selection = Character_Selection_Screen(self)
        #self.fight_screen = Fighting_Screen()
        #self.victory_screen = Victory_Menu_Screen()


    def run(self):
        while True:
            events = pygame.event.get()
            
            if self.character_selection.visible:
                self.character_selection.display_screen(events)
            #if self.fight_screen.visible:
            #    pass

            pygame.display.update()
            self.clock.tick(60)




    




Game().run()


