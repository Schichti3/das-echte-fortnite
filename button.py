import pygame

class Button():
    def __init__(self, screen, image, x_pos, y_pos, w, h):
        self.screen = screen
        self.w = w
        self.h = h
        self.image = pygame.transform.scale(image, (self.w, self.h))
        self.x_pos = x_pos
        self.y_pos = y_pos

        self.rect = self.image.get_rect(left=self.x_pos, top=self.y_pos)
        self.frame = pygame.transform.scale(pygame.image.load(".\\Images\\Rahmen.png").convert_alpha(), (self.w, self.h))
        self.selection_border_width = 5
        self.selection_border = pygame.Rect(self.x_pos-self.selection_border_width, self.y_pos-self.selection_border_width, self.w+self.selection_border_width*2, self.h+self.selection_border_width*2)

        self.mouse_above = False

    def update(self, mouse_position):
        if mouse_position[0] in range(self.rect.left, self.rect.right) and mouse_position[1] in range (self.rect.top, self.rect.bottom):
            self.screen.blit(self.image, self.rect)
            self.screen.blit(self.frame, self.rect)
        else:
            self.screen.blit(self.image, self.rect)

    def checkForInput(self, mouse_position):
        if mouse_position[0] in range(self.rect.left, self.rect.right) and mouse_position[1] in range (self.rect.top, self.rect.bottom):
            return True
        else:
            return False