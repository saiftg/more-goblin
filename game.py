# Include pygane
# Init pygame
# Creat screen with particular size
# Crate game loop
# Add quit event
# Fill screen with color
# Repeat 6 over and over


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

#sound
winSound = pygame.mixer.Sound("win.wav")

monster_touch = False

#heo location
hero = {
	'x' : 40,
	'y' : 40,
	'speed' : 20,
	'wins': 0,
	'deaths': 0
}


goblin = {
	'x': 200,
	'y': 200,
	'speed': 15
}

monster = {
	'x': 240,
	'y': 250,
	'speed': 10
}

cupcake = {
	'x': 320,
	'y': 280,
	'speed': 15
}

keys = {
	"up": 273,
	"down": 274,
	"right": 275,
	"left": 276
}

keys_down = {
	'up': False,
	'down': False,
	'left': False,
	'right': False
}

#Creat a boolean for whehter the game should be going or not
game_on = True
tick = 0
while game_on:
	tick += 1
	print tick
	#we ar inside game loop, it will keep running as long as true
	for event in pygame.event.get():
		if (event.type == pygame.QUIT):
			game_on = False
		elif (event.type == pygame.KEYDOWN):
			#print"Pressed a key!"
			if event.key == keys['up']:
				keys_down['up'] = True
				#hero['y'] -= hero['speed']
			elif event.key == keys['down']:
				keys_down['down'] = True
					
				#hero['y'] += hero['speed']
			elif event.key == keys['left']:
				keys_down['left'] = True
				#hero['x'] -= hero['speed']
			elif event.key == keys['right']:
				keys_down['right'] = True
				#hero['x'] += hero['speed']
		elif (event.type == pygame.KEYUP):
			if event.key == keys['up']:
				keys_down['up'] = False
			if event.key == keys['down']:
				keys_down['down'] = False
			if event.key == keys['left']:
				keys_down['left'] = False
			if event.key == keys['right']:
				keys_down['right'] = False

	if keys_down['up']:
		if hero['y'] > 0:
			hero['y'] -= hero['speed']
	elif keys_down['down']:
		if hero['y'] < 465 -32:
			hero['y'] += hero['speed']
	if keys_down['left']:
		hero['x'] -= hero['speed']
	elif keys_down['right']:
		hero['x'] += hero['speed']

	if hero['x'] < 0:
		hero['x'] = 10
	elif hero['x'] > screen_size[1] - 10:
		hero['x'] = screen_size[1] - 10
	elif hero['y'] < 0:
		hero['y'] = 10
	elif hero['y'] > screen_size[1] - 64:
		hero['y'] = screen_size[1] - 64

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



	distance_between = fabs(hero['x'] - goblin['x']) + fabs(hero['y'] - goblin['y'])
	if distance_between < 32:
		goblin['x'] = 200
		goblin['y'] = 200
		goblin['speed'] += 1
					# hero_alive = False
	else:
		print "not touching"
	# hero_alive = false
		

	distance_between1 = fabs(hero['x'] - monster['x']) + fabs(hero['y'] - monster['y'])
	if distance_between1 < 32:
		monster_touch = True
		print "FATALITY!!!"
		print "Finish Him!!!"
	
	distance_between2 = fabs(hero['x'] - cupcake['x']) + fabs(hero['y'] - cupcake['y'])
	if distance_between2 < 32:
		print "Tasty!!!"
	else:
		print "Don't Share with Lindsey!"

	#blit takes 2 arguments. What do u want to draw
	#wherer do u want to draw
	pygame_screen.blit(background_image, [0,0])



	font = pygame.font.Font(None, 25)
	game_over_text = font.render(("The Hero has died!"), True, (0,0,0))
	wins_text = font.render("Wins: %d" % (hero['wins']), True, (0,0,0))
	pygame_screen.blit(wins_text,[40,40])

	if monster_touch == True:
		pygame_screen.blit(game_over_text,[50,50])
	
	pygame_screen.blit(hero_img, [hero['x'], hero['y']])
	pygame_screen.blit(goblin_img, [goblin['x'], goblin['y']])
	pygame_screen.blit(monster_img, [monster['x'], monster['y']])
	pygame_screen.blit(cupcake_img, [cupcake['x'], cupcake['y']])

	pygame.display.flip()
	clock.tick(60)













