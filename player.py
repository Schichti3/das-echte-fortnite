import pygame

class player:
    def __init__(self):
        pass



        #movement flags (keine Ahnung ob das sinnvoll ist)
        self.idle = False
        self.jumping = False
        self.falling = False
        self.walking_right = False
        self.walking_left = False
        self.


    def draw(self):
        pass

    def jump(self):
        pass

movement = [False, False]
for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            
        if event.key == pygame.K_UP:
            pass