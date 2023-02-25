import pygame
import spritesheet

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.colorkey = (0, 0, 0)
        self.image = pygame.image.load('graphics/Börg.png').convert_alpha()
        self.player_sprite_sheet = spritesheet.SpriteSheet(self.image)
        self.image = self.player_sprite_sheet.get_frame((0, 0), 16, 16, 4, self.colorkey)
        self.rect = self.image.get_rect(center = (640, 360))

        self.last_update = pygame.time.get_ticks()
        self.animation_cooldown = 100
        self.frame = 0
    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.top >= 0:
            self.rect.y -= 1
        if keys[pygame.K_s] and self.rect.bottom <= 720:
            self.rect.y += 1
        if keys[pygame.K_a] and self.rect.left >= 0:
            self.rect.x -= 1
        if keys[pygame.K_d] and self.rect.right <= 1280:
            self.rect.x += 1

    def animation(self):
        keys = pygame.key.get_pressed()
        status = -1

        if keys[pygame.K_s]:
            status = 0
        if keys[pygame.K_w]:
            status = 1
        if keys[pygame.K_a]:
            status = 2
        if keys[pygame.K_d]:
            status = 3

        if status >= 0 and current_time - self.last_update >= self.animation_cooldown:
            animation = [self.player_sprite_sheet.get_frame((i, status), 16, 16, 4, self.colorkey) for i in range(5)]
            self.frame += 1
            self.last_update = current_time
            if self.frame >= len(animation):
                self.frame = 0
            self.image = animation[self.frame]


    def update(self):
        self.player_input()
        self.animation()

pygame.init()
screen = pygame.display.set_mode((1280, 720))

player = pygame.sprite.GroupSingle()
player.add(Player())

game_active = True
while game_active:

    screen.fill((50, 50, 50))

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_active = False

    current_time = pygame.time.get_ticks()

    player.draw(screen)
    player.update()

    pygame.display.update()
pygame.quit()