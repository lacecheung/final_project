#set up
import pygame, sys, time, random
from pygame.locals import *
from helper_functions import *
from constants import bottomeventline, topeventline

pygame.init ()
mainclock = pygame.time.Clock()




#counters
blockcombo = {} # dictionary of choseniteration: set of blocks for that choseniteration
currentblocks = [] # list of which choseniterations are currently active
iteration = 0
points = 0 

pressdown = False
pressup = False
pressleft = False
pressright = False


#execute game loop
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

		if event.type == KEYDOWN:
			if event.key == K_LEFT or event.key == ord("h"):
				pressleft = True
			if event.key == K_RIGHT or event.key == ord("l"):
				pressright = True	
			if event.key == K_DOWN or event.key == ord("k"):
				pressdown = True
			if event.key == K_UP or event.key == ord("j"):
				pressup = True

		if event.type == KEYUP:
			if event.key == K_LEFT or event.key == ord("h"):
				pressleft = False
			if event.key == K_RIGHT or event.key == ord("l"):
				pressright = False	
			if event.key == K_DOWN or event.key == ord("k"):
				pressdown = False
			if event.key == K_UP or event.key == ord("j"):
				pressup = False




#display board:
	get_board()
	show_points(points)


#game logic:
	if time_to_get_new_blocks(iteration):
		blocklist = get_blocks()

		assign_blocks(blocklist, iteration, currentblocks)

	draw_blocks(currentblocks, iteration)

	for blockid in currentblocks:
		blockid.givepoint = is_points_earned(blockid, pressleft, pressright, pressup, pressdown)

	for blockid in completed_blocks(currentblocks):
		#print iteration, blockid.type, blockid.givepoint, lifepoints.width
		life_points_remaining(blockid)
		if blockid.givepoint == True:
		 	points += 1

		currentblocks.remove(blockid)

	draw_remaining_life(lifepoints)

	if game_over(lifepoints):
		get_gameover_board()
		show_points(points)

#loop setup:
	pygame.display.update()
 
	iteration += 1

	mainclock.tick(iterationspers)