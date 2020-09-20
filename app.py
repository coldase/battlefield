import pygame
from random import randint
from time import time

pygame.init()
pygame.font.init()

screen_width = 1280
screen_height = 720
screen_size = (screen_width, screen_height)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Battlefield")
pygame.mouse.set_visible(False)

myfont = pygame.font.SysFont("MS Comic Sans", 50)

#Colors
RED = (255,0,0)
BLACK = (0,0,0)
GREEN = (0,255,0)
WHITE = (255,255,255)

def hit():
	if player.check_collision((food.pos_x, food.pos_y), food.size):
		return True
	if enemy.check_collision((food.pos_x, food.pos_y), food.size):
		return True

class Char:
	def __init__(self, name ,color=RED, size=50, keys="arrows", points=0):
		self.name = name
		self.size = size

		if name == "player":
			self.pos_x = int(self.size)
			self.pos_y = int((screen_height/2)-(self.size/2))
		elif name == "enemy":
			self.pos_x = int(screen_width - self.size*2)
			self.pos_y = int((screen_height/2)-(self.size/2))
		self.color = color
		self.keys = keys
		self.points = points

	def draw(self):
		pygame.draw.rect(screen, self.color, (self.pos_x, self.pos_y, self.size,self.size))
		if self.name == "player":
			p = str(self.points)
			count = myfont.render(f'Player: {p}', False, self.color)
			screen.blit(count, (50,50))
		if self.name == "enemy":
			p = str(self.points)
			count = myfont.render(f'Enemy: {p}', False, self.color)
			screen.blit(count, (50,100))

	def get_pos(self):
		pos_x, pos_y = self.pos_x, self.pos_y
		return pos_x, pos_y

	def check_collision(self, food_pos, food_size):
		if (self.pos_x + self.size > food_pos[0] and self.pos_x < food_pos[0] + food_size) and (self.pos_y + self.size > food_pos[1] and self.pos_y < food_pos[1] + food_size):
			self.points += 1
			print(f'{self.name}: {self.points}')
			return True
		else:
			return False

	def move(self):
		if self.keys == "arrows":
			if keys[pygame.K_UP] and self.pos_y > 0:
				self.pos_y -= speed
			if keys[pygame.K_DOWN] and self.pos_y < screen_height - self.size:
				self.pos_y += speed
			if keys[pygame.K_LEFT] and self.pos_x > 0:
				self.pos_x -= speed
			if keys[pygame.K_RIGHT] and self.pos_x < screen_width - self.size:
				self.pos_x += speed
		if self.keys == "wasd":
			if keys[pygame.K_w] and self.pos_y > 0:
				self.pos_y -= speed
			if keys[pygame.K_s] and self.pos_y < screen_height - self.size:
				self.pos_y += speed
			if keys[pygame.K_a] and self.pos_x > 0:
				self.pos_x -= speed
			if keys[pygame.K_d] and self.pos_x < screen_width - self.size:
				self.pos_x += speed

class Food:
	def __init__(self, color=WHITE,size=50):
		self.color = color
		self.size = size
		self.pos_x = int((screen_width / 2) + (self.size/2))
		self.pos_y = int((screen_height/2) - (self.size/2))

	def draw(self):
		pygame.draw.rect(screen, self.color, (self.pos_x, self.pos_y, self.size,self.size))
		
	def get_pos(self):
		pos_x, pos_y = self.pos_x, self.pos_y
		return pos_x, pos_y

	def random_pos(self):
		self.pos_x = int(randint(0, screen_width-self.size))
		self.pos_y = int(randint(0, screen_height-self.size))


#Config - game
FPS = 60
speed = 10

player = Char(name="player")
enemy = Char(name="enemy",color=GREEN, keys="wasd")
food = Food(size=30)
clock = pygame.time.Clock()

full_screen = False
run = True

while run:
	keys = pygame.key.get_pressed()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		elif event.type == pygame.KEYUP:
			if keys[pygame.K_ESCAPE]:
				run = False

			elif event.key == pygame.K_f:
				if not full_screen:
					pygame.display.set_mode(screen_size, pygame.FULLSCREEN)
					
					full_screen = True
				else:
					pygame.display.set_mode(screen_size)
					full_screen = False

	if hit():
		food.random_pos()

	screen.fill(BLACK)	
	player.move()
	enemy.move()
	player.draw()
	enemy.draw()
	food.draw()
	clock.tick(FPS)
	pygame.display.flip()

pygame.quit()