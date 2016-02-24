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

eventboxes = [lefteventbox, upeventbox, downeventbox, righteventbox]


#end of the event area
topeventline = windowheight - 99
bottomeventline = windowheight - 47



#setting up font
def render_points(points):
	textfont = pygame.font.SysFont(None, 25)
	text = textfont.render("Points: " + str(points), True, white, black)
	textrect = text.get_rect()
	textrect.top = 9
	textrect.left = 7

	windowsurface.blit(text, textrect)


#show how much life the player has. Color changes depending on life left (width of life bar)
lifepoints = pygame.Rect(windowwidth - 201, 9, 195, 17)

def lifepoints_color(lifepoints):
	if lifepoints.width < 50:
		color = red
	elif lifepoints.width < 140:
		color= yellow
	else: color = green

	return color  


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

	#draw life bar and life points
	pygame.draw.rect(windowsurface, gray, (windowwidth - 203, 7, 198, 20), 2)
	pygame.draw.rect(windowsurface, lifepoints_color(lifepoints), lifepoints)

	#text box for player score
	render_points(points)


#For chosen iteration, add that iteration to currentblocks list. Call get_blocks(), then add it as an entry to blockcombo dict
def new_blocks(iteration, currentblocks, blockcombo):
	if iteration%30 == 0:
		choseniteration = iteration
		currentblocks.append(choseniteration)
		blockcombo[choseniteration] = get_blocks()

	return currentblocks, blockcombo


#generate # of blocks to generate per line, and which blocks to show
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


def show_blocks(currentblocks, blockcombo, lifepoints, pointsflag):
	for b in blockcombo[choseniteration]:
		b["rect"].top += movespeed

# If blocks cross the bottom event line, shrink height of block
		if b["rect"].bottom >= bottomeventline:
			b["rect"].height -= movespeed

# blocks disappear when height is zero, and remove it from currentblocks list
		if b["rect"].height <= 0: 
			currentblocks.remove(choseniteration)

			if pointsflag == False:
				if lifepoints.width > 4:
					lifepoints.width -= 5

			elif pointsflag == True:
				points =+ 1

			break

		pygame.draw.rect(windowsurface, b["color"], b["rect"])




#Checks if rect is inside the event lines
def is_overlap(blockcombo, topeventline, bottomeventline):
	for b in blockcombo[choseniteration]:
		if b["rect"].top > topeventline and b["rect"].bottom < bottomeventline:
			return True


#_________________________________________________________________________________________________

#execute game

blockcombo = {} # dictionary of choseniteration: set of blocks for that choseniteration
currentblocks = [] # list of which choseniterations are currently active
iteration = 0
points = 0 
pointsflag = False


while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	# resets surface to black 
	get_board()

	# choose when to show blocks, and what blocks to show
	new_blocks(iteration, currentblocks, blockcombo)


	# render blocks, moving downwards. For 

	for choseniteration in currentblocks:
		show_blocks(currentblocks, blockcombo, lifepoints, pointsflag)

		#if is_overlap(blockcombo, topeventline, bottomeventline):
				#pseudo: if player clicked, pointsflag = True

	
	#pseudo: if life points <= 0, game ends. play again?


	iteration += 1

	pygame.display.update()

	mainclock.tick(iterationspers)
	

	
