#Создай собственный Шутер!

from pygame import *
from random import *


window = display.set_mode((700, 500))
display.set_caption('ping pong')

background = transform.scale(image.load('трибуны.png'),(700, 500))а что не верно тут


#mixer.music.play()



class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed=0,imge_width=65,image_hieght=65):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(imge_width,image_hieght))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.imge_width = imge_width
        self.image_hieght = image_hieght
    def reset(self):
        window.blit(self.image, (self.rect.x,self.rect.y))

class Player(GameSprite):
    def update(self):
       
        keys_pressed = key.get_pressed()

        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < 595:
            self.rect.x += self.speed
        if keys_pressed[K_SPACE]:
            bullet = Bullet('bullet.png',self.rect.centerx,self.rect.y,1.80,10,20) 
            #kick.play() 
            bullets.add(bullet)



class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 570:
            self.rect.y = -70  
            self.rect.x = randint(10,690)
            global lost2     
            lost2 += 1




class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed 



bullets = sprite.Group()
bullets.draw(window)
bullets.update()


sprite1 = Player('ракетка 2.png')
sprite2 = Enemy(' ракетка 2.png')
sprite2 = Enemy('мячик 2.png')



Enemys = sprite.Group()
Enemys.add(sprite2,sprite3,sprite4,sprite5,sprite6)
Enemys.draw(window)
Enemys.update()




finish = False
font.init() 
font = font.SysFont('Arial',40)               
lose = font.render('You lose(',True,(0,0,0))
win = font.render('YOU WIN!!!',True,(255,255,255))
boss_kill = 10
kill = 0
lost2 = 0
game = True
count = font.render('Счет:' + str(kill),True,(255,255,255))
lost = font.render('Пропушено:' + str(lost2),True,(255,255,255))
while game:
    if not finish:
        window.blit(background,(0,0))
        count = font.render('Счет:' + str(kill),True,(255,255,255))
        window.blit(count,(0,0)) 
        lost = font.render('Пропушено:' + str(lost2),True,(255,255,255))
        window.blit(lost,(0,30))
        sprite1.update()
        sprite1.reset()
        #if kill >= 15:
        if sprite.spritecollide(sprite8,bullets,True):
            boss_kill -= 1
        if boss_kill == 0:
            window.blit(win,(300,200))
            finish = True  
        Enemys.draw(window) 
        Enemys.update()
        bullets.draw(window)
        bullets.update()
        enemy_kill = sprite.groupcollide(Enemys,bullets,True,True)
        for enemy in enemy_kill:
            kill += 1
            sprite7 = Enemy('ufo.png',randint(10,690),0,1) 
            Enemys.add(sprite7)
        if lost2 >= 10: 
                kick.play()
                window.blit(lose,(300,200))
                finish = True
        if kill >= 20: 
            window.blit(win,(300,200))
            finish = True
    for ewent in event.get(): 
        if ewent.type == QUIT:
            game = False
    display.update()
















