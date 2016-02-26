import pygame, sys, time, random
from pygame.locals import *

#game speed
#iterations per second
iterationspers = 50

#the number of pixels the blocks move per iteration
movespeed = 4

#the number of pixels the blocks move per iteration
iterations_between_blocks = 30


#block parameters
block_width = 80
block_height = 20



#windowsurface
#game window surface size
windowwidth = 416
windowheight = 650

#Set up window surface
windowsurface = pygame.display.set_mode((windowwidth, windowheight), 0, 32)
window_caption = pygame.display.set_caption("Keyboard Hero")

#font
fontsize = 25



#colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (225, 225, 0)
gray = (128, 128, 128)
yellowgray = (150, 150, 80)
purple = (128, 0, 128)


#objects
# Life points outline box
lifepoints = pygame.Rect(windowwidth - 201, 9, 195, 17)

#game blocks
leftblock = {"rect": pygame.Rect(15, 40, block_width, block_height), "color": green}
upblock = {"rect": pygame.Rect(117, 40, block_width, block_height), "color": yellow}
downblock = {"rect": pygame.Rect(219, 40, block_width, block_height), "color": blue}
rightblock = {"rect": pygame.Rect(321, 40, block_width, block_height), "color": red}


#event areas
lefteventbox = {"rect": pygame.Rect(5, windowheight-99, (windowwidth-10)/4 - 1, 50), "color": black}
upeventbox = {"rect": pygame.Rect((windowwidth-10)/4 + 5, windowheight-99, (windowwidth-10)/4 - 1, 50), "color": black}
downeventbox = {"rect": pygame.Rect(((windowwidth-10)/4)*2 + 5, windowheight-99, (windowwidth-10)/4 - 1, 50), "color": black}
righteventbox = {"rect": pygame.Rect(((windowwidth-10)/4)*3 + 5, windowheight-99, (windowwidth-10)/4 + 1, 50), "color": black}

eventboxes = [lefteventbox, upeventbox, downeventbox, righteventbox]

topeventline = windowheight - 99
bottomeventline = windowheight - 47