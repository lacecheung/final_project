import pygame, sys, time, random
from pygame.locals import *

pygame.init ()
mainclock = pygame.time.Clock()

# Game setup and parameters

#iterations per second
iterationspers = 50
#the number of pixels the blocks move per iteration
movespeed = 4


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


#key objects:

#colored blocks
leftblock = {"rect": pygame.Rect(15, 40, 80, 20), "color": green}
upblock = {"rect": pygame.Rect(117, 40, 80, 20), "color": yellow}
downblock = {"rect": pygame.Rect(219, 40, 80, 20), "color": blue}
rightblock = {"rect": pygame.Rect(321, 40, 80, 20), "color": red}

#area where the player must take an action to gain points
lefteventbox = {"rect": pygame.Rect(5, windowheight-99, (windowwidth-10)/4 - 1, 50), "color": black}
upeventbox = {"rect": pygame.Rect((windowwidth-10)/4 + 5, windowheight-99, (windowwidth-10)/4 - 1, 50), "color": black}
downeventbox = {"rect": pygame.Rect(((windowwidth-10)/4)*2 + 5, windowheight-99, (windowwidth-10)/4 - 1, 50), "color": black}
righteventbox = {"rect": pygame.Rect(((windowwidth-10)/4)*3 + 5, windowheight-99, (windowwidth-10)/4 + 1, 50), "color": black}

#show how much life the player has
lifepoints = pygame.Rect(windowwidth - 203, 9, 197, 17)

#end of the event area
bottomeventline = windowheight - 47



#redraw board each time so block trail does not show
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

	#draw life bar
	pygame.draw.rect(windowsurface, gray, (windowwidth - 205, 7, 200, 20), 2)


#generate random number: # of blocks to show per line
def blocksperline():
	return random.randint(0,4)


#generate which blocks to generate per line
def get_blocks():
	listblocks = []
	blocks = [leftblock, upblock, downblock, rightblock]

	for blocknumber in range(0, blocksperline()):
		blockchoice = random.choice(blocks)

		listblocks.append(blockchoice)
		blocks.remove(blockchoice)

	return listblocks


# How often to generate new blocks
def show_blocks():
	return random.choice([True, False, False, False])


#execute game

blockcombo = {}
iteration = 0
currentblocks = []


while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	# resets surface to black 
	get_board()

	if iteration%50 == 0:
		currentblocks.append(iteration)
		blockcombo[iteration] = get_blocks()

	# for every set of blocks currently showing
	for iteration in currentblocks:

		# for each block in that set of blocks, move the block downwards at movespeed
		for b in blockcombo[iteration]:
			b["rect"].top += movespeed
		
			# If blocks cross the bottom event line, shrink height of block
			if b["rect"].bottom >= bottomeventline:
				b["rect"].height -= movespeed

			# blocks disappear when height is zero, and remove it from currentblocks list
			if b["rect"].height <= 0: 
				currentblocks.remove(iteration)

				if lifepoints.width >= 0:
					lifepoints.width -= 5

				break

			pygame.draw.rect(windowsurface, b["color"], b["rect"])

	pygame.draw.rect(windowsurface, green, lifepoints)

	iteration += 1

	pygame.display.update()

	mainclock.tick(iterationspers)
	

	
