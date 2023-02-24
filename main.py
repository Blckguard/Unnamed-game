import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('unnamed game')
clock = pygame.time.Clock()

background_surf = pygame.image.load('../pygame-practice/graphics/Sky.png').convert_alpha()
background_surf = pygame.transform.rotozoom(background_surf, 0, 3)

player_surf = pygame.image.load('../pygame-practice/graphics/Player/player_stand.png').convert_alpha()
player_rect = player_surf.get_rect(center = (640, 360))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()  # checking pressed keys
    if keys[pygame.K_w]:
        player_rect.y -= 6
    if keys[pygame.K_s]:
        player_rect.y += 6
    if keys[pygame.K_a]:
        player_rect.x -= 6
    if keys[pygame.K_d]:
        player_rect.x += 6

    screen.blit(background_surf, (0,0))

    screen.blit(player_surf, player_rect)
    pygame.display.update()
    clock.tick(60)
