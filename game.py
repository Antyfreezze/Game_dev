import pygame as pg
import sys
''' global variables '''
WIN_WIDTH = 800
WIN_HEIGH = 640
DISPLAY = (WIN_WIDTH, WIN_HEIGH)
BACKGROUND_COLOR = "black"
''' platform constants '''
PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32
PLATFORM_COLOR = "#FF6262"

def main():
    pg.init()
    screen = pg.display.set_mode(DISPLAY)
    pg.display.set_caption("Black Jinja")
    ''' level form '''
    level = [
       "-------------------------",
       "-                       -",
       "-                       -",
       "-                       -",
       "-            --         -",
       "-                       -",
       "--                      -",
       "-                       -",
       "-                   --- -",
       "-                       -",
       "-                       -",
       "-      ---              -",
       "-                       -",
       "-   -----------        -",
       "-                       -",
       "-                -      -",
       "-                   --  -",
       "-                       -",
       "-                       -",
       "-------------------------"]
    ''' bg - background '''
    bg = pg.Surface(DISPLAY)
    bg.fill(pg.Color(BACKGROUND_COLOR))
    ''' main loop '''
    while 1:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                quit()
        
        screen.blit(bg, (0, 0))
        ''' drawing level '''
        x=y=0
        platf_size = (PLATFORM_WIDTH, PLATFORM_HEIGHT)
        for row in level:
            for col in row:
                if col == "-":
                    pf = pg.Surface(platf_size)
                    pf.fill(pg.Color(PLATFORM_COLOR)
                    screen.blit(pf, (x, y))

                x += PLATFORM_WIDTH
            y += PLATFORM_HEIGHT
            x = 0

        pg.display.flip()




''' drawing level func '''
# def create_lev(level, screen):
#     x=y=0
#     platf_size = (PLATFORM_WIDTH, PLATFORM_HEIGHT)
#     for row in level:
#         for col in row:
#             if col == "-":
#                 pf = pg.Surface(platf_size)
#                 pf.fill(pg.Color(PLATFORM_COLOR)
#                 screen.blit(pf, (x, y))

#             x += PLATFORM_WIDTH
#         y += PLATFORM_HEIGHT
#         x = 0

''' exit func '''
def quit():
    pg.quit()
    sys.exit(0)

if __name__ == "__main__":
    main()
