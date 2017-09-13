import pygame
# we have to init to use pygame
#from math module get the fabs method
from math import fabs, hypot
from random import randint

pygame.init()

screen_size = (650, 465)
#screensize cant change
pygame_screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Goblin Chase")
clock = pygame.time.Clock()
#background_image = pygame.image.load("background.png")
#background_image = pygame.image.load("mk2title.png")
background_image = pygame.image.load("livingforest.jpg")


hero_img = pygame.image.load("hero.png")
goblin_img = pygame.image.load("goblin.png")
monster_img = pygame.image.load("lohan.jpg")
cupcake_img = pygame.image.load("cupcake.png")
# 8. Set up the hero location
hero = {
	"x": 100,
	"y": 100,
	"speed": 20,
	"wins": 0
}

goblin = {
	"x": 200,
	"y": 200,
	"speed": 2
}

monster = {
	"x": 100,
	"y": 200,
	"speed": 3,
	"dx": 1,
	"dy": 1,
}

keys = {
	"up": 273,
	"down": 274,
	"right": 275,
	"left": 276
}

keys_down = {
	"up": False,
	"down": False,
	"left": False,
	"right": False
}

game_over_text = ""

# 4. Create a game loop (while)
# Create a boolean for whether the game should be going or not
game_on = True
hero_alive = True
tick = 0
while game_on:
	tick += 1
	print tick
	# we are inside the main game loop.
	# it will keep running, as long as our bool is true
	# 5. Add a quit event (Python needs an escape)
	# Pygame comes with an event loop! (sort of like JS)
	for event in pygame.event.get():
		if (event.type == pygame.QUIT):
			# the user clicked the red x in the top left
			game_on = False
		elif event.type == pygame.KEYDOWN:
			# print "User pressed a key!"
			if event.key == keys['up']:
				# user pressed up!!
				# hero['y'] -= hero['speed']
				keys_down['up'] = True
			elif event.key == keys['down']:
				# hero['y'] += hero['speed']
				keys_down['down'] = True
			elif event.key == keys['left']:
				# hero['x'] -= hero['speed']
				keys_down['left'] = True
			elif event.key == keys['right']:
				# hero['x'] += hero['speed']
				keys_down['right'] = True
		elif event.type == pygame.KEYUP:
			# the user let go of a key. See if it's one that matters
			if event.key == keys['up']:
				# user let go of the upkey. Flip the bool
				keys_down['up'] = False
			if event.key == keys['down']:
				keys_down['down'] = False
			if event.key == keys['right']:
				keys_down['right'] = False
			if event.key == keys['left']:
				keys_down['left'] = False

	if hero_alive:
		# Move the hero
		if keys_down['up']:
			if hero['y'] > 0:
				hero['y'] -= hero['speed']
		elif keys_down['down']:
			if hero['y'] < (480-32):
				hero['y'] += hero['speed']
		if keys_down['left']:
			if hero['x'] > 0:
				hero['x'] -= hero['speed']
		elif keys_down['right']:
			if hero['x'] < (512-32):
				hero['x'] += hero['speed']

		# Move the bad guy
		dx = goblin['x'] - hero['x']
		dy = goblin['y'] - hero['y']
		dist = hypot(dx,dy)
		# print dist
		dx = dx / dist
		dy = dy / dist
		# print dx, dy
		goblin['x'] -= dx * goblin['speed']
		goblin['y'] -= dy * goblin['speed']

		if tick % 20 == 0:
		# change directions!
			monster['dx'] = randint(-1,1)
			monster['dy'] = randint(-1,1)

		monster['x'] += monster['dx'] * monster['speed']
		monster['y'] += monster['dy'] * monster['speed']


		# COLLISION DETECTION!!!
		distance_between = fabs(hero['x'] - goblin['x']) + fabs(hero['y'] - goblin['y'])
		if distance_between < 32:
			# the hero and goblin are touching!
			# print "collision!"
			goblin['x'] = 200
			goblin['y'] = 200
			goblin['speed'] += 1
			# hero_alive = False
		else:
			print "not touching"
	# hero_alive = false
	else:
		game_over_text = font.render(("The Hero has died!"), True, (0,0,0))

			

	# 6. Fill in the screen with a color (or image)
	# ACTUALLY RENDER SOMETHING
	# blit takes 2 arguments...
	# 1. What do you want to draw?
	# 2. Where do you watn you to draw it
	pygame_screen.blit(background_image, [0,0])

	# Make a font so we can write on the screen
	font = pygame.font.Font(None, 25)
	wins_text = font.render("Wins: %d" % (hero['wins']), True, (0,0,0))
	pygame_screen.blit(wins_text,[40,40])
	if game_over_text != "":
		pygame_screen.blit(game_over_text,[40,40])		
	
	pygame_screen.blit(hero_img, [hero['x'],hero['y']])
	pygame_screen.blit(goblin_img, [goblin['x'],goblin['y']])
	pygame_screen.blit(monster_img, [monster['x'],monster['y']])


	# 7. Repeat 6 over and over over...
