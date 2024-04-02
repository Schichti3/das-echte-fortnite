import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, name, x, y):
        super().__init__()
        self.character_name = name
        self.walking_right_sprites = [pygame.image.load(f".\\sprites\\{name}_Walking\\{name}_walking_r_1.png"), pygame.image.load(f".\\sprites\\{name}_Walking\\{name}_walking_r_2.png"), 
                                      pygame.image.load(f".\\sprites\\{name}_Walking\\{name}_walking_r_3.png"), pygame.image.load(f".\\sprites\\{name}_Walking\\{name}_walking_r_4.png"),
                                      pygame.image.load(f".\\sprites\\{name}_Walking\\{name}_walking_r_5.png"), pygame.image.load(f".\\sprites\\{name}_Walking\\{name}_walking_r_6.png"), 
                                      pygame.image.load(f".\\sprites\\{name}_Walking\\{name}_walking_r_7.png"), pygame.image.load(f".\\sprites\\{name}_Walking\\{name}_walking_r_8.png")]
        
        self.walking_left_sprites =  [pygame.image.load(f".\\sprites\\{name}_Walking\\{name}_walking_l_1.png"), pygame.image.load(f".\\sprites\\{name}_Walking\\{name}_walking_l_2.png"), 
                                      pygame.image.load(f".\\sprites\\{name}_Walking\\{name}_walking_l_3.png"), pygame.image.load(f".\\sprites\\{name}_Walking\\{name}_walking_l_4.png"),
                                      pygame.image.load(f".\\sprites\\{name}_Walking\\{name}_walking_l_5.png"), pygame.image.load(f".\\sprites\\{name}_Walking\\{name}_walking_l_6.png"), 
                                      pygame.image.load(f".\\sprites\\{name}_Walking\\{name}_walking_l_7.png"), pygame.image.load(f".\\sprites\\{name}_Walking\\{name}_walking_l_8.png")]
        
        self.test = []
        for sprite in self.walking_right_sprites:
            sprite = pygame.transform.scale(sprite, (102,102))
            self.test.append(sprite)

        self.walking_right_sprites.clear()
        self.walking_right_sprites = self.test
        
        self.test2 = []
        for sprite in self.walking_left_sprites:
            sprite = pygame.transform.scale(sprite, (102,102))
            self.test2.append(sprite)

        self.walking_left_sprites.clear()
        self.walking_left_sprites = self.test2


        self.standing_sprite_right = pygame.image.load(f".\\sprites\\{name}_Walking\\{name.lower()}_standing_r.png")

        self.standing_sprite_right = pygame.transform.scale(self.standing_sprite_right, (102,102))

        self.standing_sprite_left = pygame.image.load(f".\\sprites\\{name}_Walking\\{name.lower()}_standing_l.png")

        self.standing_sprite_left = pygame.transform.scale(self.standing_sprite_left, (102,102))


        self.current_sprite = 0
        self.image = self.standing_sprite_right
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)



        #movement flags (keine Ahnung ob das sinnvoll ist)
        self.standing_right = False
        self.standing_left = False
        self.jumping_right = False
        self.jumping_left = False
        self.falling = False
        self.walking_right = False
        self.walking_left = False

        self.movement_speed = 4


    def set_behaviour(self, standing_right=False, standing_left=False, jumping_right=False, jumping_left=False, falling=False, walking_right=False, walking_left=False):
        self.standing_right = standing_right
        self.standing_left = standing_left
        self.jumping_right = jumping_right
        self.jumping_left = jumping_left
        self.falling = falling
        self.walking_right = walking_right
        self.walking_left = walking_left


    def __moving_right(self):
        self.rect.x += self.movement_speed
    def __moving_left(self):
        self.rect.x -= self.movement_speed

    def standing_animation_right(self):
        self.image = self.standing_sprite_right

    def standing_animation_left(self):
        self.image = self.standing_sprite_left

    def walking_right_animation(self):
        self.image = self.walking_right_sprites[int(self.current_sprite)]

        self.current_sprite += 0.20

        if self.current_sprite >= len(self.walking_right_sprites):
            self.current_sprite = 0

        self.image = self.walking_right_sprites[int(self.current_sprite)]

    def walking_left_animation(self):
        self.image = self.walking_left_sprites[int(self.current_sprite)]

        self.current_sprite += 0.20

        if self.current_sprite >= len(self.walking_left_sprites):
            self.current_sprite = 0

        self.image = self.walking_left_sprites[int(self.current_sprite)]

        
    def update(self):

        if self.standing_right == True and self.standing_left == False:
            self.standing_animation_right()

        if self.standing_left == True and self.standing_right == False:
            self.standing_animation_left()

        if self.walking_right == True and self.walking_left == False:
            self.walking_right_animation()
            self.__moving_right()

        if self.walking_left == True and self.walking_right == False:
            self.walking_left_animation()
            self.__moving_left()

        




