import pygame as pg

# object classes
class Sprite(pg.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()

        self.image = pg.Surface([width, height])
        self.image.fill((0,0,0))
        self.image.set_colorkey((0,0,0))

        pg.draw.rect(
            self.image,
            color,
            pg.Rect(0, 0, width, height)
        )

        self.rect = self.image.get_rect()
