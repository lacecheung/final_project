#set up
import pygame, sys, time, random
from pygame.locals import *
from helper_functions import *
from constants import bottomeventline, topeventline, conseq_blocks_for_combo

#initiating pygame
pygame.init ()
# instantiating pygame.time.clock
mainclock = pygame.time.Clock()


#counters
combo_iteration = - conseq_blocks_for_combo - FPS

#default value for player keys (when players press key, values = True, otherwise False)
pressdown = False
pressup = False
pressleft = False
pressright = False



#execute game loop
while True:
	is_game_over = False #reset game

	blockcombo = {} # dictionary, where key = block id, and value = blockclass object
	currentblocks = [] # list of active blocks
	iteration = 0 #iteration counter
	points = 0 #player points
	conseq_blocks = 0 #number of consecutive blocks player hit successfully

	lifepoints.width =  20 #lifepoints_outline.width - 2
	start_screen()

	#print "main screen loop"
	pygame.mixer.music.load("Kalimba.mp3")
	pygame.mixer.music.play(-1, 0.0)
	musicPlaying = True


	while True:

		for event in pygame.event.get():
			terminate_conditions(event)

		# sets up player input (allows player to use arrows or letters on the keyboard)
			if event.type == KEYDOWN:
				if event.key == K_LEFT or event.key == ord("d"):
					pressleft = True
				if event.key == K_RIGHT or event.key == ord("k"):
					pressright = True	
				if event.key == K_DOWN or event.key == ord("j"):
					pressdown = True
				if event.key == K_UP or event.key == ord("f"):
					pressup = True

			if event.type == KEYUP:
				if event.key == K_LEFT or event.key == ord("d"):
					pressleft = False
				if event.key == K_RIGHT or event.key == ord("k"):
					pressright = False	
				if event.key == K_DOWN or event.key == ord("j"):
					pressdown = False
				if event.key == K_UP or event.key == ord("f"):
					pressup = False


		#display board:
		get_board(points, lifepoints)
			
		# visually show which key is being pressed by highlighting the associated event block
		if pressdown == True:
			pygame.draw.rect(windowsurface, downeventbox["color"], downeventbox["rect"])
		if pressup == True:
			pygame.draw.rect(windowsurface, upeventbox["color"], upeventbox["rect"])
		if pressright == True:
			pygame.draw.rect(windowsurface, righteventbox["color"], righteventbox["rect"])
		if pressleft == True:
			pygame.draw.rect(windowsurface, lefteventbox["color"], lefteventbox["rect"])

		#at set intervals, generate a random set of blocks
		if time_to_get_new_blocks(iteration):
			blocklist = get_blocks()

			#instantiate blockclass instance for every block, and assign to a dictionary. (key = block id, value = blockclass object)
			assign_blocks(blocklist, iteration, currentblocks)

		#render blocks, moving downwards by movespeed every iteration
		draw_blocks(currentblocks, iteration)

		#did player hit the correct key at the right time. changes blockid.givepoint to True
		for blockid in currentblocks:
			blockid.givepoint = is_points_earned(blockid, pressleft, pressright, pressup, pressdown)
			if blockid.givepoint == True:
				blockid.color = white

		# for blockids that have reached the bottom: either decrease lifepoints for missed block or award points for earned blocks 
		for blockid in completed_blocks(currentblocks):
			if blockid.color != white:
	 			lifepoints.width -= lifepoints_outline.width * lifepoints_decrement_percent
	 			conseq_blocks = 0

			elif blockid.color == white:
			 	points += 5
				conseq_blocks += 1
		
			#if player is on a combo streak, award double points
			if conseq_blocks >= conseq_blocks_for_combo:
				combo_iteration = iteration
				points += 5

			currentblocks.remove(blockid)

			# display message if player successfully gets X consecutive blocks
		if iteration < (combo_iteration + FPS) and conseq_blocks > 10:
			render_text(30, "Combo! " + str(conseq_blocks) +  " blocks!", white, black, 0.5 * windowwidth, 0.5 * windowheight)


		if game_over(lifepoints) == True:
			pygame.mixer.music.stop()
			get_gameover_board(points)
			break
		


		pygame.display.update()
	 	iteration += 1
	 	mainclock.tick(FPS)




	 	




	 	

		

	
	
	
	
		 
	

