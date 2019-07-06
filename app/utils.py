import pygame
from pygame.locals import *

def create_screen(width, height):
	return pygame.display.set_mode((width, height))

def load_player_image():
	return pygame.transform.scale(pygame.image.load('assets/img/dot.png'), (20, 20))

def load_background_image():
	return (255, 255, 255)

class GameObject:

	def __init__(self, image, height, speed):
		self.speed = speed
		self.image = image
		self.pos = image.get_rect().move(0, height)

	def move(self, direction):

		if direction == "down":
			self.pos = self.pos.move(0, self.speed)

		if direction == "up":
			self.pos = self.pos.move(0, -self.speed)

		if direction == "right":
			self.pos = self.pos.move(self.speed, 0)
		
		if direction == "left":
			self.pos = self.pos.move(-self.speed, 0)

		if self.pos.right > 600:
			self.pos.left = 0