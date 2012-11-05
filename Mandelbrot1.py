from __future__ import division

#Mandelbrot 1

import pygame, sys, time
from math import sqrt
from pygame.locals import *

def yield_px(array):
    print len(array), len(array[0])
    for i in range(len(array)):
        for j in range(len(array[i])):
            yield j, i
            
curr_left = -2.5
curr_right = 1
curr_top = 1
curr_bottom = -1
scr_h = 600
scr_w = 800
debug_dict = {}
    
def main():
    pygame.init()
    start_left = -2.5
    start_right = 1
    start_top = 1
    start_bottom = -1

    #clock
    fpsClock = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((scr_w,scr_h))
    pygame.display.set_caption("Mandelbrot 1")
    mousex, mousey = 0,0
    max_iter = 500
    Msurf = pygame.Surface((scr_w,scr_h))
    Msurf.fill((10,10,10))
    pxarray = pygame.PixelArray(Msurf)
    get_mandelbrot(pxarray,max_iter)
    del pxarray
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        DISPLAYSURF.blit(Msurf,(0,0))
        pygame.display.update()
        fpsClock.tick(30)

def get_mandelbrot(array, max_iter):
    increment_h = (abs(curr_right)+abs(curr_left))/scr_w
    increment_v = (abs(curr_top)+abs(curr_bottom))/scr_h
    for r, c in yield_px(array):
        x = 0
        y = 0
        x0 = curr_left + c*increment_h
        y0 = curr_top - r*increment_v
        it = 0
        while x*x + y*y < 2*2 and it < max_iter:
            temp_c = (x + y*1j)*(x + y*1j)
            x = temp_c.real + x0
            y = temp_c.imag + y0
            it = it + 1 
        array[c][r] = (max(255-it*5,0),10,10)

if __name__ == '__main__':
    main()























