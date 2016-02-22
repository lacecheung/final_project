import pygame, sys, time, random
from pygame.locals import *

pygame.init ()
mainclock = pygame.time.Clock()

# Game setup and parameters

#iterations per second
iterationspers = 50

#move speed (pixels per iteration)
movespeed = 5



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



# minimum iterations (0.02 / iteration) between block sets
cadence = 200

#blocks
leftblock = {"rect": pygame.Rect(15, 40, 80, 20), "color": green}
upblock = {"rect": pygame.Rect(117, 40, 80, 20), "color": yellow}
downblock = {"rect": pygame.Rect(219, 40, 80, 20), "color": blue}
rightblock = {"rect": pygame.Rect(321, 40, 80, 20), "color": red}

lifepoints = pygame.Rect(windowwidth - 203, 9, 197, 17)

#eventline
eventline = windowheight - 45

#redraw board each time so block trail does not show
def get_board():
	#board dynamically changes based on size of board
	#resets board
	windowsurface.fill(black)
	#vertical lines
	pygame.draw.line(windowsurface, gray, (4, 35), (4, windowheight-5), 2)
	pygame.draw.line(windowsurface, gray, ((windowwidth-10)/4 + 4, 35), ((windowwidth-10)/4 + 4, windowheight-5), 2)
	pygame.draw.line(windowsurface, gray, (((windowwidth-10)/4)*2 + 4, 35), (((windowwidth-10)/4)*2 + 4, windowheight-5), 2)
	pygame.draw.line(windowsurface, gray, (((windowwidth-10)/4)*3 + 4, 35), (((windowwidth-10)/4)*3 + 4, windowheight-5), 2)
	pygame.draw.line(windowsurface, gray, (windowwidth -5, 35), (windowwidth -5, windowheight-5), 2)
	#horizontal event lines
	pygame.draw.line(windowsurface, yellowgray, (4, windowheight-100), (windowwidth-5, windowheight-100), 2)
	pygame.draw.line(windowsurface, yellowgray, (4, windowheight-50), (windowwidth-5, windowheight-50), 2)
	#horizontal border
	pygame.draw.line(windowsurface, gray, (4, 35), (windowwidth-5, 35), 2)
	pygame.draw.line(windowsurface, gray, (4, windowheight-5), (windowwidth-5, windowheight-5), 2)
	#arrows
	pygame.draw.polygon(windowsurface, white, ((45, 610), (45, 617), (70, 617), (70, 630), (45, 630), (45, 637), (35, 623)))
	pygame.draw.polygon(windowsurface, white, ((366, 610), (376, 623), (366, 637), (366, 630), (341, 630), (341, 617), (366, 617)))
	#Life bar
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


combo = {}
seconds = 0


while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	get_board()

	combo[seconds] = get_blocks()

	#new part

	# lineswithblocks = []

	# if seconds%100 == 0 and show_blocks() == True:
	# 	lineswithblocks.append(seconds)

	# 	for line in lineswithblocks:


	# render blocks moving down at variable movespeed
	#NOTE: HOW TO DUPLICATE BELOW CODE FOR EVERY NEW SET OF BLOCKS?

	for b in combo[0]:
		b["rect"].top += movespeed
	

		# If blocks cross the bottom event line, shrink height of block
		if b["rect"].bottom >= eventline:
			b["rect"].height -= movespeed

			# blocks disappear when height is zero
		if b["rect"].height <= 0: 
			break

		pygame.draw.rect(windowsurface, b["color"], b["rect"])

	pygame.draw.rect(windowsurface, green, lifepoints)

	seconds += 1

	pygame.display.update()
	
	mainclock.tick(iterationspers)
	
	# resets surface to black 
	
