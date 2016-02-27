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
	
def draw_remaining_life(lifepoints):
	pygame.draw.rect(windowsurface, lifepoints_color(lifepoints), lifepoints)
	


class BlockClass(object):
	def __init__(self, left, top, color):
		self.left = left
		self.top = top
		self.color = color
		self.width = block_width
		self.height = block_height
		self.givepoint =  False

	


#Chooses how many blocks to show, and which blocks to show
def blocksperline():
	choicelist = [0, 1, 1, 1, 1, 2, 2, 2, 3, 3, 4]
	return random.choice(choicelist)


def get_blocks():
	listblocks = []
	blocks = [leftblock, upblock, downblock, rightblock]

	for blocknumber in range(0, blocksperline()):
		blockchoice = random.choice(blocks)

		listblocks.append(blockchoice)
		blocks.remove(blockchoice)

	return listblocks



def time_to_get_new_blocks(iteration):
	if iteration%iterations_between_blocks(iteration) == 0:
		return True

def assign_blocks(blocklist, iteration, currentblocks):

	for index, block in enumerate(blocklist, 0):
		blockid = str(iteration), str(index)
		blockid = BlockClass(block["rect"].left, block["rect"].top, block["color"])
		currentblocks.append(blockid)


def movespeed(iteration):
	global movespeed1

	if iteration%iterations_between_speedincrease == 0 and iteration != 0:
		
		movespeed1 += movespeedincrease

	return movespeed1


def draw_blocks(currentblocks, iteration):
	currentmovespeed = movespeed(iteration)

	for blockid in currentblocks:
		blockid.top += currentmovespeed

		if (blockid.top + blockid.height) >= bottomeventline:
			blockid.height -= currentmovespeed

		pygame.draw.rect(windowsurface, blockid.color, (blockid.left, blockid.top, blockid.width, blockid.height))


def completed_blocks(currentblocks):
	blockstoremove = []

	for blockid in currentblocks:
		if blockid.height <= 0:
			blockstoremove.append(blockid)

	return blockstoremove


def life_points_remaining(blockid):
	if blockid.givepoint == False:
		if lifepoints.width > lifepoints_decrement - 1:
	 		lifepoints.width -= lifepoints_decrement


def iterations_between_blocks(iteration):
	global iterations_between_blocks1

	if iteration%iterations_between_blocks_decrement_change == 0 and iteration != 0:
		if iterations_between_blocks1 > min_iterations_between_blocks:
			iterations_between_blocks1 -= iterations_between_blocks_decrement

	print iteration, iterations_between_blocks1

	return iterations_between_blocks1


# player input
leftarrowkey = False
uparrowkeydown = False
downarrowkey = False
rightarrowkey = False