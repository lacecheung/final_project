import pygame, sys, time, random
from pygame.locals import *
from constants import *

# Renders number of player points
def show_points(points):
	render_text(25, "Points: " + str(points), white, black, windowwidth*.12, 17)


#color of life points bar (red = low, yellow = mid, green = high)
def lifepoints_color(lifepoints):
	if lifepoints.width < 50:
		color = red
	elif lifepoints.width < 140:
		color= yellow
	else: color = green

	return color  


# draws board
def get_board(points, lifepoints):
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
	#pygame.draw.polygon(windowsurface, white, ((45, 610), (45, 617), (70, 617), (70, 630), (45, 630), (45, 637), (35, 623)))
	#pygame.draw.polygon(windowsurface, white, ((366, 610), (376, 623), (366, 637), (366, 630), (341, 630), (341, 617), (366, 617)))

	#eventbox icon
	render_text(30, "D", white, black, lefticonbox["rect"].centerx, lefticonbox["rect"].centery)
	render_text(30, "F", white, black, upiconbox["rect"].centerx, upiconbox["rect"].centery)
	render_text(30, "J", white, black, downiconbox["rect"].centerx, downiconbox["rect"].centery)
	render_text(30, "K", white, black, righticonbox["rect"].centerx, righticonbox["rect"].centery)

	show_points(points)

	draw_remaining_life(lifepoints)

	
def draw_remaining_life(lifepoints):
	pygame.draw.rect(windowsurface, gray, lifepoints_outline, 2)
	pygame.draw.rect(windowsurface, lifepoints_color(lifepoints), lifepoints)
	


class BlockClass(object):
	def __init__(self, left, top, color, type):
		self.left = left
		self.top = top
		self.color = color
		self.width = block_width
		self.height = block_height
		self.givepoint =  False
		self.type = type
		self.bottom = self.top + self.height

	

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

def assign_blocks(blocklist, iteration, currentblocks,):
	for index, block in enumerate(blocklist, 0):
		blockid = str(iteration), str(index)
		blockid = BlockClass(block["rect"].left, block["rect"].top, block["color"], block["type"])
		currentblocks.append(blockid)


def movespeed(iteration):
	global MOVESPEED1

	if iteration%iterations_between_speedincrease == 0 and iteration != 0:
		MOVESPEED1 += movespeedincrease

	print iteration, MOVESPEED1

	return MOVESPEED1


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


def iterations_between_blocks(iteration):
	global iterations_between_blocks1

	if iteration%iterations_between_blocks_decrement_change == 0 and iteration != 0:
		if iterations_between_blocks1 > min_iterations_between_blocks:
			iterations_between_blocks1 -= iterations_between_blocks_decrement

	return iterations_between_blocks1


def is_points_earned(blockid, pressleft, pressright, pressup, pressdown):
	if blockid.top >= topeventline and blockid.bottom <= bottomeventline:
	#if blockid.top >= topeventline and blockid.height == 20:
		if (blockid.type == "left" and pressleft == True) or (blockid.type == "right" and pressright == True) or (blockid.type == "up" and pressup == True) or (blockid.type == "down" and pressdown == True):
			blockid.givepoint = True
		else:
			blockid.givepoint = False

	return blockid.givepoint


def game_over(lifepoints):
	if lifepoints.width < lifepoints_outline.width * lifepoints_decrement_percent:
		return True


def sort_highscores():
	with open("topscore.txt") as my_file:
		scores = my_file.readlines()

	score_in_int = []

	for score in scores:
		score_in_int.append(int(score))

	sorted_score = sorted(score_in_int, reverse = True)

	return sorted_score


def display_gameover_score_message(points):
	sorted_highscores = sort_highscores()
	if points in sorted_highscores[0:9]:
		score_message = "You got a high score!"
	else: score_message = "You did not get a high score"

	render_text(30, score_message, white, black, windowsurface.get_rect().centerx, windowheight*.3)


def show_highscore_board(points):
	sorted_highscores = sort_highscores()
	windowsurface.fill(black)
	show_points(points)
	render_text(40, "High scores:", white, black, windowsurface.get_rect().centerx, windowheight*.2)

	while True:
		for index, score in enumerate(sorted_highscores, 0):
			if index < 10:
				render_text(30, str(index+1) + ". " + str(sorted_highscores[index]).strip(), white, black, windowsurface.get_rect().centerx, windowheight*(index+1)/20 + windowheight*0.3)
		
		pygame.display.update()

		for event in pygame.event.get():
			terminate_conditions(event)
			if event.type == KEYDOWN:
				if event.key == K_SPACE:
					return


def get_gameover_board(points):
	while True:
		windowsurface.fill(black)
		render_text(40, "Game Over!", white, black, windowsurface.get_rect().centerx, windowheight*.2)
		render_text(30, "To see high scores: press 's'", white, black, windowsurface.get_rect().centerx, windowheight*.5)
		render_text(30, "To continue: press space bar", white, black, windowsurface.get_rect().centerx, windowheight*.55)
		render_text(30, "To quit: press ESC", white, black, windowsurface.get_rect().centerx, windowheight*.6)
		show_points(points)
		display_gameover_score_message(points)

		pygame.display.update()

		for event in pygame.event.get():
			terminate_conditions(event)
			if event.type == KEYDOWN:
				if event.key == ord("s"):
					show_highscore_board(points)
				if event.key == K_SPACE:
					return


def render_text(fontsize, text, textcolor, backgroundcolor, midrectx, midrecty):
	textfont = pygame.font.SysFont(None, fontsize)
	text = textfont.render(text, True, textcolor, backgroundcolor)
	textrect = text.get_rect()
	textrect.centery = midrecty
	textrect.centerx = midrectx

	windowsurface.blit(text, textrect)


def start_screen():
	#print "entered start screen function"
	while True:
		#print "start screen loop"
		windowsurface.fill(black)
		render_text(40, "Keyboard Hero:", white, black, 0.5*windowwidth, 0.22*windowheight)
		render_text(30, "Press space bar to play,", white, black, 0.5*windowwidth, 0.3*windowheight)
		render_text(30, "i for game instructions,", white, black, 0.5*windowwidth, 0.35*windowheight)
		render_text(30, "or ESC to exit", white, black, 0.5*windowwidth, 0.4*windowheight)

		pygame.display.update()

		for event in pygame.event.get():
			terminate_conditions(event)
			if event.type == KEYDOWN:
				if event.key == ord("i"):
					instructions_screen()
				if event.key == K_SPACE:
					return



def instructions_screen():
	while True:

		windowsurface.fill(black)
		render_text(25, "Instructions:", green, black, 0.5*windowwidth, 0.2*windowheight)
		render_text(20, "Use arrow keys or letter keys (D, F, J, K) as controls", gray, black, 0.5*windowwidth, 0.3*windowheight)
		render_text(20, "5 points per correct key", gray, black, 0.5*windowwidth, 0.35*windowheight)
		render_text(20, "Double points for combos!", gray, black, 0.5*windowwidth, 0.4*windowheight)
		render_text(20, "Negative points for hitting wrong key", gray, black, 0.5*windowwidth, 0.45*windowheight)
		render_text(25, "Hit space bar to continue", green, black, 0.5*windowwidth, 0.7*windowheight)

		pygame.display.update()

		for event in pygame.event.get():
			terminate_conditions(event)
			if event.type == KEYDOWN:
				if event.key == K_SPACE:
					return


def terminate():
	pygame.quit()
	sys.exit()


def terminate_conditions(event):
	if event.type == QUIT:
		terminate()
	if event.type == KEYDOWN:
		if event.key == K_ESCAPE:
			terminate()

		