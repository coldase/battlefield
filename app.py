import pygame

pygame.init()

screen_width = 1280
screen_height = 720
screen_size = (screen_width, screen_height)
screen = pygame.display.set_mode(screen_size)

#colors
RED = (255,0,0)
BLACK = (0,0,0)
GREEN = (0,255,0)
WHITE = (255,255,255)

class Char:
	def __init__(self, name, color, pos_x, pos_y, size):
		self.name = name
		self.color = color
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.size = size

	def draw(self):
		pygame.draw.rect(screen, self.color, (self.pos_x, self.pos_y, self.size,self.size))
		
class Food:
	def __init__(self, color, pos_x, pos_y, size):
		self.color = color
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.size = size

	def draw(self):
		pygame.draw.rect(screen, self.color, (self.pos_x, self.pos_y, self.size,self.size))
		

	

#Config
FPS = 60

player_color = RED
player_size = 50
player_x = 100
player_y = 100
speed = 10

food_color = WHITE
food_size = 50
food_x = int((screen_width/2) - (food_size/2))
food_y = int((screen_height/2) - (food_size/2))


clock = pygame.time.Clock()
full_screen = False
run = True
while run:

	keys = pygame.key.get_pressed()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		if event.type == pygame.KEYUP:
			print(event)

	if keys[pygame.K_UP] and player_y > 0:
		player_y -= speed
	if keys[pygame.K_DOWN] and player_y < screen_height - player_size:
		player_y += speed
	if keys[pygame.K_LEFT] and player_x > 0:
		player_x -= speed
	if keys[pygame.K_RIGHT] and player_x < screen_width - player_size:
		player_x += speed
	
"""
	if keys[pygame.K_f]:
		if not full_screen:
			pygame.display.set_mode(screen_size, pygame.FULLSCREEN)
			full_screen = True
		else:
			pygame.display.set_mode(screen_size)
			full_screen = False
"""
	if keys[pygame.K_ESCAPE]:
		run = False

	clock.tick(FPS)
	screen.fill(BLACK)
	player = Char("player1", player_color, player_x, player_y, player_size)
	food = Food(food_color, food_x, food_y, food_size)
	player.draw()
	food.draw()
	pygame.display.flip()
pygame.quit()
