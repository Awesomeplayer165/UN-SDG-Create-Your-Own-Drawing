import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("UN SDG - Create Your Own Drawing")

class Circle:
	x = 0
	y = 0
	radius = 50
	width = 10

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def draw(self):
		pygame.draw.circle(screen, (255, 255, 255), (self.x, self.y), self.radius, self.width)
		pygame.display.update()


circles = [
	Circle(300, 200), # top
	Circle(250, 250), # top-left
	Circle(350, 250), # top-right
	Circle(275, 300), # bottom-left
	Circle(325, 300)  # bottom-right
]

screen.fill((0, 0, 175))
for circle in circles: circle.draw()

while True:

	for event in pygame.event.get():
			if event.type == QUIT:
					pygame.quit()
					exit()


	pygame.display.update()