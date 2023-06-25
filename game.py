from pygame import *

SPRITE_RESOLUTION = (100, 100)
class GameSprite(sprite.Sprite):
    def __init__(
            self, x : int, y : int, 
            filename : str, speed : int, 
            resolution = SPRITE_RESOLUTION
            ):
        super().__init__()
        self.speed = speed

        # загрузка текстуры
        self.image = transform.scale(image.load(filename), resolution)

        # настройка хитбокса
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    # отображение спрайта
    def reset(self):
        window.blit(self.image, (self.rect.x , self.rect.y))
        
    # пересечение областей
    def colliderect(self, rect):
        return self.rect.colliderect(rect)

# Создание сцены
RESOLUTION = (1280, 720)
window = display.set_mode(RESOLUTION)
window.fill((255, 255, 255))

# Игровой счётчик
FPS = 60
clock = time.Clock()
clock.tick(FPS)

game = True

while game:

    # Закрытие приложения
    for e in event.get():
        if e.type == QUIT:
            game = False
     
    if not finish:
        window.fill((255, 255, 255))

# Смена кадра
    display.update()
