# imports
import objects
import pygame as pg

# main function
def main():

    # init game
    pg.init()

    # create screen
    screen = pg.display.set_mode((800,600)) # ((width,height))

    # add background sprites
    background = objects.background
    ground = objects.ground

    # doesn't work
    screen.blit(background, (0,0))
    screen.blit(ground, (0,0))

    # title
    pg.display.set_caption('Castle Wars')

    # game loop
    running = True
    while running:

        # screen color
        screen.fill((0,0,0))

        # check all events
        for event in pg.event.get():

            # allow to quit
            if event.type == pg.QUIT:
                running = False

# run script
if __name__ == "__main__":
    main()
