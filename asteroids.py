import pygame
from Player import Player

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


run = True

player = Player(100, 100)


while run:

    screen.fill(pygame.Color(0,0,0))


    key = pygame.key.get_pressed()

    if key[pygame.K_w] and key[pygame.K_a] and player.y > 0 and player.x > 0:
        player.move("upleft")
    elif key[pygame.K_w] and key[pygame.K_d] and player.y > 0 and player.x < SCREEN_WIDTH - player.w:
        player.move("upright")
    elif key[pygame.K_s] and key[pygame.K_a] and player.y < SCREEN_HEIGHT - player.h and player.x > 0:
        player.move("downleft")
    elif key[pygame.K_s] and key[pygame.K_d] and player.y < SCREEN_HEIGHT - player.h and player.x < SCREEN_WIDTH - player.w:
        player.move("downright")
    elif key[pygame.K_w] and player.y > 0:
        player.move("up")
    elif key[pygame.K_s] and player.y < SCREEN_HEIGHT - player.h:
        player.move("down")
    elif key[pygame.K_a] and player.x > 0:
        player.move("left")
    elif key[pygame.K_d] and player.x < SCREEN_WIDTH - player.w:
        player.move("right")

    

    if key[pygame.K_RIGHT]:
        player.rotate("right")
    elif key[pygame.K_LEFT]:
        player.rotate("left")


       
    rot_img = pygame.transform.rotate(player.player, player.angle)
    print(player.angle)
    screen.blit(rot_img, (player.x - (rot_img.get_width() / 2), player.y - (rot_img.get_height() / 2)))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()


pygame.quit()


