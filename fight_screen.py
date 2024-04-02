import pygame, sys
from button import Button


class Fight_Screen:
    def __init__(self, daddy):
        self.daddy = daddy
        self.visible = True

        self.background = pygame.transform.scale(pygame.image.load('.\\Images\\hintergrund type ebat.png'), (self.daddy.screen.get_width(), self.daddy.screen.get_height()))

        self.twavis_button = Button(self.daddy.screen, pygame.image.load(".\\Images\\Travis.png"), 50, 50, 128, 128)
        self.peter_button = Button(self.daddy.screen, pygame.image.load(".\\Images\\Peter.png"), 50, 250, 128, 128)
        self.ariana_button = Button(self.daddy.screen, pygame.image.load(".\\Images\\Ariana.png"), 250, 50, 128, 128)
        self.ben_button = Button(self.daddy.screen, pygame.image.load(".\\Images\\Ben.png"), 250, 250, 128, 128)
        self.vader_button = Button(self.daddy.screen, pygame.image.load(".\\Images\\Raider.png"), 450, 50, 128, 128)
        self.peter_button = Button(self.daddy.screen, pygame.image.load(".\\Images\\Spiderman.png"), 50, 250, 128, 128)
        self.peter_button = Button(self.daddy.screen, pygame.image.load(".\\Images\\Eren.png"), 50, 150, 128, 128)
        self.peter_button = Button(self.daddy.screen, pygame.image.load(".\\Images\\Vader.png"), 50, 150, 128, 128)

        self.character_buttons = [self.twavis_button, self.peter_button, self.ariana_button, self.ben_button, self.vader_button]

        self.clock = pygame.time.Clock()


    def display_screen(self, events):
            
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.twavis_button.checkForInput(pygame.mouse.get_pos()):
                        print("Ich will Twavis auswählen :(")
                    if self.peter_button.checkForInput(pygame.mouse.get_pos()):
                        print("Ich will Peter auswählen :(")
                    if self.twavis_button.checkForInput(pygame.mouse.get_pos()):
                        print("Ich will Ariana auswählen :(")
                    if self.peter_button.checkForInput(pygame.mouse.get_pos()):
                        print("Ich will Ben auswählen :(")
                    if self.twavis_button.checkForInput(pygame.mouse.get_pos()):
                        print("Ich will Raider auswählen :(")
                    if self.peter_button.checkForInput(pygame.mouse.get_pos()):
                        print("Ich will Spiderman auswählen :(")
                    if self.twavis_button.checkForInput(pygame.mouse.get_pos()):
                        print("Ich will Eren auswählen :(")
                    if self.peter_button.checkForInput(pygame.mouse.get_pos()):
                        print("Ich will Vader auswählen :(")



            self.daddy.screen.blit(self.background, (0,0))

            for button in self.character_buttons:
                button.update(pygame.mouse.get_pos())