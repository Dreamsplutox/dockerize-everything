import pygame
from pygame.locals import *
from utils import *
import sys

if __name__ == '__main__':

	#init pygame
	pygame.init()

	screen = pygame.display.set_mode((640, 480))
	player = pygame.image.load('assets/img/dot.png').convert()
	player = pygame.transform.scale(player, (20, 20))
	player1 = GameObject(player, 2, 5)
	background = pygame.image.load('assets/img/bg.png').convert()
	
	screen.blit(background, (0, 0))
	screen.blit(background, player1.pos, player1.pos)
	
	

	while 1:
		
		for event in pygame.event.get():
			if event.type == QUIT:
				sys.exit()

		screen.blit(background, player1.pos, player1.pos)

		if pygame.key.get_pressed()[K_UP]:
			#print("right key arrow")
			player1.move("up")
			screen.blit(player1.image, player1.pos)

		if pygame.key.get_pressed()[K_DOWN]:
			#print("right key arrow")
			player1.move("down")
			screen.blit(player1.image, player1.pos)

		if pygame.key.get_pressed()[K_RIGHT]:
			#print("right key arrow")
			player1.move("right")
			screen.blit(player1.image, player1.pos)

		if pygame.key.get_pressed()[K_LEFT]:
			#print("right key arrow")
			player1.move("left")
			screen.blit(player1.image, player1.pos)


		screen.blit(player1.image, player1.pos)

		pygame.display.update()
		pygame.time.delay(10)