import pygame, sys, time, random
from pygame.locals import *
from constants import *

# Renders number of player points
def show_points(points):
	textfont = pygame.font.SysFont(None, fontsize)
	text = textfont.render("Points: " + str(points), True, white, black)
	textrect = text.get_rect()
	textrect.top = 9
	textrect.left = 7

	windowsurface.blit(text, textrect)


#color of life points bar (red = low, yellow = mid, green = high)
def lifepoints_color(lifepoints):
	if lifepoints.width < 50:
		color = red
	elif lifepoints.width < 140:
		color= yellow
	else: color = green

	return color  


# draws board
def get_board():
	#resets board
	windowsurface.fill(black)

	#draw vertical lines
	pygame.draw.line(windowsurface, gray, (4, 35), (4, windowheight-5), 2)
	pygame.draw.line(windowsurface, gray, ((windowwidth-10)/4 + 4, 35), ((windowwidth-10)/4 + 4, windowheight-5), 2)
	pygame.draw.line(windowsurface, gray, (((windowwidth-10)/4)*2 + 4, 35), (((windowwidth-10)/4)*2 + 4, windowheight-5), 2)
	pygame.draw.line(windowsurface, gray, (((windowwidth-10)/4)*3 + 4, 35), (((windowwidth-10)/4)*3 + 4, windowheight-5), 2)
	pygame.draw.line(windowsurface, gray, (windowwidth -5, 35), (windowwidth -5, windowheight-5), 2)

	#draw horizontal event lines
	pygame.draw.line(windowsurface, yellowgray, (4, windowheight-100), (windowwidth-5, windowheight-100), 2)
	pygame.draw.line(windowsurface, yellowgray, (4, windowheight-50), (windowwidth-5, windowheight-50), 2)

	#draw horizontal border
	pygame.draw.line(windowsurface, gray, (4, 35), (windowwidth-5, 35), 2)
	pygame.draw.line(windowsurface, gray, (4, windowheight-5), (windowwidth-5, windowheight-5), 2)

	#draw arrows
	pygame.draw.polygon(windowsurface, white, ((45, 610), (45, 617), (70, 617), (70, 630), (45, 630), (45, 637), (35, 623)))
	pygame.draw.polygon(windowsurface, white, ((366, 610), (376, 623), (366, 637), (366, 630), (341, 630), (341, 617), (366, 617)))

	#draw life bar and life points
	pygame.draw.rect(windowsurface, gray, (windowwidth - 203, 7, 198, 20), 2)
	pygame.draw.rect(windowsurface, lifepoints_color(lifepoints), lifepoints)


	


#Chooses how many blocks to show, and which blocks to show
def blocksperline():
	return random.randint(0,4)

def get_blocks():
	listblocks = []
	blocks = [leftblock, upblock, downblock, rightblock]

	for blocknumber in range(0, blocksperline()):
		blockchoice = random.choice(blocks)

		listblocks.append(blockchoice)
		blocks.remove(blockchoice)

	return listblocks






def draw_blocks(blockcombo, each_iteration):
	for block in blockcombo[each_iteration]:
		block["rect"].top += movespeed
		#print "rect top: ", block["rect"].top

		pygame.draw.rect(windowsurface, block["color"], block["rect"])


def time_to_get_new_blocks(iteration):
	if iteration%iterations_between_blocks == 0:
		return True
