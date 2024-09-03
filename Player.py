import pygame


class Player:
    '''
    This is my Player class, so far just init it with the x,y,width,height posiitons
    Will implement other player functions later 
    '''

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.speed = 0.15
        self.color = (0,0,255)
        self.player = pygame.image.load('./assets/ship.png')
        self.player = pygame.Surface.convert_alpha(self.player)
        self.player = pygame.transform.scale(self.player,(self.player.get_width() / 8, self.player.get_height() / 8) )
        self.w = self.player.get_width()
        self.h = self.player.get_height()

    def move(self, dir):
        if dir == "up":
            # self.player.move_ip(0, -self.speed)
            self.y -= self.speed
        elif dir == "down":
            # self.player.move_ip(0, self.speed)
            self.y += self.speed
        elif dir == "right":
            # self.player.move_ip(self.speed, 0)
            self.x += self.speed
        elif dir == "left":
            # self.player.move_ip(-self.speed, 0)
            self.x -= self.speed
        elif dir == "upright":
            # self.player.move_ip(self.speed, -self.speed)
            self.x += self.speed
            self.y -= self.speed
        elif dir == "upleft":
            # self.player.move_ip(-self.speed, -self.speed)
            self.x -= self.speed
            self.y -= self.speed
        elif dir == "downright":
            # self.player.move_ip(self.speed, self.speed)
            self.x += self.speed
            self.y += self.speed
        elif dir == "downleft":
            # self.player.move_ip(-self.speed, self.speed)
            self.x -= self.speed
            self.y += self.speed
        