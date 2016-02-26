#set up
import pygame, sys, time, random
import copy
from pygame.locals import *
from helper_functions import *

pygame.init ()
mainclock = pygame.time.Clock()

#counters
blockcombo = {} # dictionary of choseniteration: set of blocks for that choseniteration
currentblocks = [] # list of which choseniterations are currently active
iteration = 0
points = 0 
pointsflag = False



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
		currentblocks.append(iteration)
		blockcombo[iteration] = get_blocks()

	for each_iteration in currentblocks:
		#print "each iteration:", each_iteration
		draw_blocks(blockcombo, each_iteration)

	

#loop setup:
	pygame.display.update()

	iteration += 1

	mainclock.tick(iterationspers)