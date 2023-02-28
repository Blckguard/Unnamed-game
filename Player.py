import pygame, spritesheet, time


class Player(pygame.sprite.Sprite):
    def __init__(self, colorkey, image):
        super().__init__()
        self.colorkey = colorkey

        # get sprite-sheet and create frames
        self.player_sprite_sheet = spritesheet.SpriteSheet(image)
        self.image = self.player_sprite_sheet.get_frame((0, 0), 16, 16, 4, self.colorkey)
        self.rect = self.image.get_rect(center = (640, 360))

        # movement values
        self.frame = 0
        self.movement_speed = 2

        # animation values
        self.animation_status = 0
        self.animation_cooldown = 100
        self.animation_speed = 300
    def player_input(self):
        # getting input from player and moving character on screen

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] and self.rect.top >= 0:
            self.rect.y -= 1 * self.movement_speed
            self.animation_status = 1
        if keys[pygame.K_s] and self.rect.bottom <= 720:
            self.rect.y += 1 * self.movement_speed
            self.animation_status = 0
        if keys[pygame.K_a] and self.rect.left >= 0:
            self.rect.x -= 1 * self.movement_speed
            self.animation_status = 2
        if keys[pygame.K_d] and self.rect.right <= 1280:
            self.rect.x += 1 * self.movement_speed
            self.animation_status = 3

    def animation(self, current_time):
        # getting status of character using according animation
        last_update = pygame.time.get_ticks()

        if self.animation_status >= 0 and current_time - last_update >= self.animation_cooldown:
            animation = [self.player_sprite_sheet.get_frame((i, self.animation_status), 16, 16, 4, self.colorkey) for i in range(5)]

            self.frame += 1 * self.animation_speed
            last_update = current_time
            if self.frame >= len(animation):
                self.frame = 0
            self.image = animation[self.frame]


    def update(self, current_time):
        self.player_input()
        self.animation(current_time)
