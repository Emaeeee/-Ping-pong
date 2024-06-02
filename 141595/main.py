from pygame import *
from random import randint

win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))

#класс-родитель для других спрайтов
class GameSprite(sprite.Sprite):
#конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        #вызываем конструктор класса (Sprite):
        sprite.Sprite.__init__(self)
        #каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
#метод, отрисовывающий героя на окне
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
#класс главного игрока
class Player(GameSprite):
    #метод для управления спрайтом стрелками клавиатуры
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_width - 80:
            self.rect.y += self.speed

    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width - 80:
            self.rect.y += self.speed

lose = GameSprite('lose.png', 0, 0, 600, 500, 0)
lose2 = GameSprite('lose.png', 0, 0, 600, 500, 0)

game = True
finish = False
clock = time.Clock()
FPS = 60

backk = 'pyaterochka.jpg'

back = transform.scale(image.load(backk), (win_width, win_height))

speed_x = 3
speed_y = 3

raketka = Player('palka.png', 30, 200, 100, 150, 4)
raketka2 = Player('palka.png', 520, 200, 100, 150, 4)
ball = GameSprite('ball.png', 200, 200, 50, 50, 4)

#класс спрайта-врага 
class Enemy(GameSprite):
    #движение врага
    def update(self):
        self.rect.y += self.speed
        global lost
        #исчезает, если дойдёт до края экрана
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0
            lost = lost + 1

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.blit(back, (0, 0))
        raketka.update_l()
        raketka2.update_r()
        ball.rect.x += speed_x
        ball.rect.y -= speed_y
        if sprite.collide_rect(raketka, ball) or sprite.collide_rect(raketka2, ball):
            
            speed_x *= -1
            ball.rect.x += speed_x * 0.000000001
            speed_y *= 1

        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1
        
        if ball.rect.x < 0:
            finish = True
            lose.reset()

        if ball.rect.x > 600:
            finish = True
            lose2.reset()
            
        
        raketka.reset()
        raketka2.reset()
        ball.reset()
        display.update()
        clock.tick(60)