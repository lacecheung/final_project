import pygame, sys, time
from pygame.locals import *

pygame.init ()


# Game setup and parameteres

#game window
windowwidth = 416
windowheight = 600
windowsurface = pygame.display.set_mode((windowwidth, windowheight), 0, 32)

pygame.display.set_caption("Keyboard Hero")

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

#move speed (pixels per iteration)
movespeed = 2

#blocks
leftblock = {"rect": pygame.Rect(5, 105, 10, 20), "color": green}
upblock = {"rect": pygame.Rect(107, 207, 10, 20), "color": yellow}
downblock = {"rect": pygame.Rect(209, 309, 10, 20), "color": blue}
rightblock = {"rect": pygame.Rect(311, 411, 10, 20), "color": red}

blocks = [leftblock, upblock, downblock, rightblock]


#draw lines
#guitar "strings"
vline1 = pygame.draw.line(windowsurface, gray, (4, 5), (4, 595), 2)
vline2 = pygame.draw.line(windowsurface, gray, (106, 5), (106, 595), 2)
vline3 = pygame.draw.line(windowsurface, gray, (208, 5), (208, 595), 2)
vline4 = pygame.draw.line(windowsurface, gray, (310, 5), (310, 595), 2)
vline5 = pygame.draw.line(windowsurface, gray, (412, 5), (412, 595), 2)
#event line
hline1 = pygame.draw.line(windowsurface, yellowgray, (4, 525), (412, 525), 2)
hline1 = pygame.draw.line(windowsurface, yellowgray, (4, 550), (412, 550), 2)
#top and bottom border
hline3 = pygame.draw.line(windowsurface, gray, (4, 5), (412, 5), 2)
hline4 = pygame.draw.line(windowsurface, gray, (4, 595), (412, 595), 2)

#arrows
uparrow = pygame.draw.polygon(windowsurface, white, ((45, 560), (45, 567), (70, 567), (70, 580), (45, 580), (45, 587), (35, 573)))
downarrow = pygame.draw.polygon(windowsurface, white, ((366, 560), (376, 573), (366, 587), (366, 580), (341, 580), (341, 567), (366, 567)))


# Rendering surface






#execute game
pygame.display.update()

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	# resets surface to black 
	# windowsurface.fill(black)
