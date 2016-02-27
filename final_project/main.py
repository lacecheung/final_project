#set up
import pygame, sys, time, random
from pygame.locals import *
from helper_functions import *

pygame.init ()
mainclock = pygame.time.Clock()




#counters
blockcombo = {} # dictionary of choseniteration: set of blocks for that choseniteration
currentblocks = [] # list of which choseniterations are currently active
iteration = 0
points = 0 




#execute game loop
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

#display board:
	get_board()
	show_points(points)


#game logic:
	if time_to_get_new_blocks(iteration):
		blocklist = get_blocks()

		assign_blocks(blocklist, iteration, currentblocks)

	draw_blocks(currentblocks, iteration)

	for blockid in completed_blocks(currentblocks):
		life_points_remaining(blockid)
		currentblocks.remove(blockid)

	draw_remaining_life(lifepoints)
		
#loop setup:
	pygame.display.update()

	iteration += 1

	mainclock.tick(iterationspers)