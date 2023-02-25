import pygame

class SpriteSheet():
    def __init__(self, image):
        self.sheet = image

    def get_frame(self, frame, width, height, scale, color):
        """ takes a spritesheet and returns a specific frame
        :param frame: tuple: (location on x-axis, location on y-axis)
        :param width: width of sprite
        :param height: height of sprite
        :param scale: scale of returned frame if needed
        :param color: spritesheet background color
        :return: specified frame or list of frames of spritesheet
        """
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0, 0), (width * frame[0], height * frame[1], width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(color)

        return image
