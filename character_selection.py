import pygame, sys
from button import Button
##pygame.init()
#screen = pygame.display.set_mode((960, 520))
#pygame.display.set_caption('Menu')


class Character_Selection_Screen:
    def __init__(self, daddy):
        self.daddy = daddy
        self.visible = True

        self.background = pygame.transform.scale(pygame.image.load('.\\Images\\hintergrund type ebat.png'), (self.daddy.screen.get_width(), self.daddy.screen.get_height()))

        

        self.twavis_button = Button(self.daddy.screen, pygame.image.load(".\\Images\\Travis.png"), 90, 200, 128, 128)
        self.peter_button = Button(self.daddy.screen, pygame.image.load(".\\Images\\Peter.png"), 308, 200, 128, 128)
        self.ariana_button = Button(self.daddy.screen, pygame.image.load(".\\Images\\Ariana.png"), 526, 200, 128, 128)
        self.ben_button = Button(self.daddy.screen, pygame.image.load(".\\Images\\Ben.png"), 744, 200, 128, 128)
        self.raider_button = Button(self.daddy.screen, pygame.image.load(".\\Images\\Raider.png"), 90, 372, 128, 128)
        self.spiderman_button = Button(self.daddy.screen, pygame.image.load(".\\Images\\Spiderman.png"), 308, 372, 128, 128)
        self.eren_button = Button(self.daddy.screen, pygame.image.load(".\\Images\\Eren.png"), 526, 372, 128, 128)
        self.vader_button = Button(self.daddy.screen, pygame.image.load(".\\Images\\Vader.png"), 744, 372, 128, 128)

        self.character_buttons = [self.twavis_button, self.peter_button, self.ariana_button, self.ben_button, self.raider_button, self.spiderman_button, self.eren_button, self.vader_button]

        self.clock = pygame.time.Clock()


    def run(self):
        while self.visible:
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.twavis_button.checkForInput(pygame.mouse.get_pos()):
                        print("Ich will Twavis auswählen :(")
                    if self.peter_button.checkForInput(pygame.mouse.get_pos()):
                        print("Ich will Peter auswählen :(")
                    if self.ariana_button.checkForInput(pygame.mouse.get_pos()):
                        print("Ich will Ariana auswählen :(")
                    if self.ben_button.checkForInput(pygame.mouse.get_pos()):
                        print("Ich will Ben auswählen :(")
                    if self.raider_button.checkForInput(pygame.mouse.get_pos()):
                        print("Ich will Raider auswählen :(")
                    if self.spiderman_button.checkForInput(pygame.mouse.get_pos()):
                        print("Ich will Spiderman auswählen :(")
                    if self.eren_button.checkForInput(pygame.mouse.get_pos()):
                        print("Ich will Eren auswählen :(")
                    if self.vader_button.checkForInput(pygame.mouse.get_pos()):
                        print("Ich will Vader auswählen :(")



            self.daddy.screen.blit(self.background, (0,0))

            for button in self.character_buttons:
                button.update(pygame.mouse.get_pos())
                
            pygame.display.update()
            self.clock.tick(60)

