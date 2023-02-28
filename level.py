import pygame
from pytmx.util_pygame import load_pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)
        self.offset = pygame.math.Vector2()
        self.display_surface = pygame.display.get_surface()
        self.half_w = self.display_surface.get_size()[0] // 2
        self.half_h = self.display_surface.get_size()[1] // 2

    def center_target_camera(self, target):
        self.offset.x = target.rect.centerx - self.half_w
        self.offset.y = target.rect.centerx - self.half_h

    def custom_draw(self, player):

        self.center_target_camera(player)
        keys = pygame.key.get_pressed()
        offset_pos = self.rect.topleft

        if keys[pygame.K_d]:
            offset_pos = self.rect.topleft - self.offset
        if keys[pygame.K_a]:
            offset_pos = self.rect.topleft + self.offset

        self.rect.topleft = offset_pos

    def update(self, player):
        self.custom_draw(player)
