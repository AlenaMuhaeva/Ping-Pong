from random import randint
from pygame import *
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('Ping-pong')
class GameSprite(sprite.Sprite):
    def __init__(self, pl_image, pl_x, pl_y, pl_sped,size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(pl_image), (size_x, size_y))
        self.speed = pl_sped
        self.rect = self.image.get_rect()
        self.rect.x = pl_x
        self.rect.y = pl_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_L(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_R(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

background = transform.scale(image.load('fon.jpg'),(win_width, win_height))
player1 = Player('player.jpg', 90, 100, 5, 30, 90)
player2 = Player('player.jpg', 600, 100, 5, 30, 90)
ball = GameSprite('ball.png', 250, 250, 5,60,60)
clock = time.Clock()
FPS = 60
run = True
speed_x = 3
speed_y = 3
finish = False
font.init()
font1 = font.Font(None, 35)
lose1 = font1.render('PLAYER 1 LOSE!!!', True, (180, 0, 0))
lose2 = font1.render('PLAYER 2 LOSE!!!', True, (180, 0, 0))
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    window.blit(background, (0,0))
    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y 
    if ball.rect.y > win_height-50 or ball.rect.y < 0:
        speed_y *= -1
    if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
        speed_x *= -1
    if ball.rect.x > win_width - 50:
        finish = True
        window.blit(lose2,(255,200))
    if ball.rect.x < 10:
        finish =True
        window.blit(lose1,(255,200))
    
    
    player1.update_L()
    player1.reset()
    player2.update_R()
    player2.reset()
    
    ball.reset()
    display.update()
    clock.tick(FPS)