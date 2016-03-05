import pygame, sys, time, random
from pygame.locals import *

#game speed
#iterations per second
FPS = 40

#the number of pixels the blocks move per iteration
MOVESPEED1 = 8
movespeedincrease = 1
iterations_between_speedincrease = 400

#the number of pixels the blocks move per iteration
iterations_between_blocks1 = 45
iterations_between_blocks_decrement = 5
min_iterations_between_blocks = 10
iterations_between_blocks_decrement_change = 300


#block parameters
block_width = 80
block_height = 20


#windowsurface
#game window surface size
windowwidth = 416
windowheight = 650

#Set up window surface
#windowsurface = pygame.display.set_mode((windowwidth, windowheight), 0, 32)
windowsurface = pygame.display.set_mode((windowwidth, windowheight), pygame.FULLSCREEN)
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
darkgray = (50,50,50)


#objects
# Life points remaining
lifepoints = pygame.Rect(windowwidth - 201, 9, 195, 17)
lifepoints_outline = pygame.Rect(windowwidth - 203, 7, 198, 20)
#lifepoints = pygame.Rect(windowwidth - 201, 9, 10, 17)
lifepoints_decrement_percent = 0.03

#game blocks
leftblock = {"rect": pygame.Rect(15, 40, block_width, block_height), "color": green, "type": "left"}
upblock = {"rect": pygame.Rect(117, 40, block_width, block_height), "color": yellow, "type": "up"}
downblock = {"rect": pygame.Rect(219, 40, block_width, block_height), "color": blue, "type": "down"}
rightblock = {"rect": pygame.Rect(321, 40, block_width, block_height), "color": red, "type": "right"}


#event areas
lefteventbox = {"rect": pygame.Rect(5, windowheight-99, (windowwidth-10)/4 - 1, 50), "color": darkgray}
upeventbox = {"rect": pygame.Rect((windowwidth-10)/4 + 5, windowheight-99, (windowwidth-10)/4 - 1, 50), "color": darkgray}
downeventbox = {"rect": pygame.Rect(((windowwidth-10)/4)*2 + 5, windowheight-99, (windowwidth-10)/4 - 1, 50), "color": darkgray}
righteventbox = {"rect": pygame.Rect(((windowwidth-10)/4)*3 + 5, windowheight-99, (windowwidth-10)/4 + 1, 50), "color": darkgray}

eventboxes = [lefteventbox, upeventbox, downeventbox, righteventbox]

topeventline = windowheight - 99
bottomeventline = windowheight - 47

lefticonbox = {"rect": pygame.Rect(5, windowheight-50, (windowwidth-10)/4 - 1, 50), "color": black}
upiconbox = {"rect": pygame.Rect((windowwidth-10)/4 + 5, windowheight-50, (windowwidth-10)/4 - 1, 50), "color": black}
downiconbox = {"rect": pygame.Rect(((windowwidth-10)/4)*2 + 5, windowheight-50, (windowwidth-10)/4 - 1, 50), "color": black}
righticonbox = {"rect": pygame.Rect(((windowwidth-10)/4)*3 + 5, windowheight-50, (windowwidth-10)/4 + 1, 50), "color": black}

conseq_blocks_for_combo = 10

song1 = "Adele-Rolling_In_The_Deep.mp3"
song2 = "Kalimba.mp3"
song3 = "Weezer-Island_In_The_Sun.mp3"

songs = [song1, song2, song3]