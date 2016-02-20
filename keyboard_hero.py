import pygame, sys, time
from pygame.locals import *

pygame.init ()


# Game setup and parameteres

#game window
windowwidth = 416
windowheight = 650
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
movespeed = 5

#blocks
#NOTE: NEED TO MAKE DIMENSIONS DYNAMICALLY CHANGE DEPENDING ON SIZE OF BOARD
leftblock = {"rect": pygame.Rect(15, 10, 80, 20), "color": green}
upblock = {"rect": pygame.Rect(117, 10, 80, 20), "color": yellow}
downblock = {"rect": pygame.Rect(219, 10, 80, 20), "color": blue}
rightblock = {"rect": pygame.Rect(321, 10, 80, 20), "color": red}

blocks = [leftblock, upblock, downblock, rightblock]


def get_board():
	#board dynamically changes based on size of board
	#resets board
	windowsurface.fill(black)
	#vertical lines
	pygame.draw.line(windowsurface, gray, (4, 5), (4, windowheight-5), 2)
	pygame.draw.line(windowsurface, gray, ((windowwidth-10)/4 + 4, 5), ((windowwidth-10)/4 + 4, windowheight-5), 2)
	pygame.draw.line(windowsurface, gray, (((windowwidth-10)/4)*2 + 4, 5), (((windowwidth-10)/4)*2 + 4, windowheight-5), 2)
	pygame.draw.line(windowsurface, gray, (((windowwidth-10)/4)*3 + 4, 5), (((windowwidth-10)/4)*3 + 4, windowheight-5), 2)
	pygame.draw.line(windowsurface, gray, (windowwidth -5, 5), (windowwidth -5, windowheight-5), 2)
	#horizontal event lines
	pygame.draw.line(windowsurface, yellowgray, (4, windowheight-100), (windowwidth-5, windowheight-100), 2)
	pygame.draw.line(windowsurface, yellowgray, (4, windowheight-50), (windowwidth-5, windowheight-50), 2)
	#horizontal border
	pygame.draw.line(windowsurface, gray, (4, 5), (windowwidth-5, 5), 2)
	pygame.draw.line(windowsurface, gray, (4, windowheight-5), (windowwidth-5, windowheight-5), 2)
	#arrows
	pygame.draw.polygon(windowsurface, white, ((45, 610), (45, 617), (70, 617), (70, 630), (45, 630), (45, 637), (35, 623)))
	pygame.draw.polygon(windowsurface, white, ((366, 560), (376, 573), (366, 587), (366, 580), (341, 580), (341, 567), (366, 567)))



#execute game

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	get_board()

	for b in blocks:
		b["rect"].top += movespeed

		pygame.draw.rect(windowsurface, b["color"], b["rect"])

	pygame.display.update()
	time.sleep(0.02)
	# resets surface to black 
	
