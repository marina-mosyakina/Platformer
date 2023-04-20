from pygame import *
window = display.set_mode((1000,700))
display.set_caption('')
fon = transform.scale(image.load('фон.jpg'),(1000,700))
clock = time.Clock()
costum = 0
class GameSprite(sprite.Sprite):
    def __init__(self, img, x, y, w, h, speed):
        super().__init__()
        self.imgs = img
        self.w = w
        self.h = h
        self.image = transform.scale(image.load(img[0]),(w,h))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite):
    def move(self):
        global costum
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
            costum = (costum+1)%len(self.imgs)
            self.image = transform.scale(image.load(self.imgs[costum]),(self.w,self.h))
        if keys[K_d] and self.rect.x < 900:
            self.rect.x += self.speed
            costum = (costum+1)%len(self.imgs)
            self.image = transform.scale(image.load(self.imgs[costum]),(self.w,self.h))
            self.image = transform.flip(self.image,True,False)
cat_img = ['0.gif','1.gif','2.gif','3.gif','4.gif','5.gif']
cat = Player(cat_img,10,300,100,70,10)
game = True
while game:
    clock.tick(30)
    window.blit(fon,(0,0))
    cat.move()
    cat.reset()
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()