import pygame, time, spritesheet
from settings import *
from player import *
from camera import *
from level import *


class Game:
    def __init__(self):
        # important variables
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Unnamed Game')

        # sprite handling
        player_spritesheet = pygame.image.load('graphics/Börg.png')
        self.player_sprite = Player((0, 0, 0), player_spritesheet)

        #sprite groups
        self.sprite_group = pygame.sprite.Group()
        self.player_group = pygame.sprite.GroupSingle()
        self.player_group.add(self.player_sprite)

    def get_tiled_layers(self):

        tmx_data = load_pygame('graphics/test.tmx')

        for layer in tmx_data.visible_layers:
            if hasattr(layer, 'data'):
                for x, y, surf in layer.tiles():
                    pos = (x * 512, y * 512)
                    Tile(pos=pos, surf=surf, groups=self.sprite_group)
    def run(self):
        while True:

            # event handler
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            self.screen.fill((50, 50, 50))
            current_time = pygame.time.get_ticks()

            self.player_group.update(current_time)
            self.player_group.draw(self.screen)
            # self.sprite_group.custom_draw(self.player_sprite)

            pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.run()









