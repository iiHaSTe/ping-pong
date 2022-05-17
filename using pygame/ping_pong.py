#====== Imports ======#
from random import uniform, choice
from pprint import pprint
from sys import exit
from pygame import *
from sprite import Sprite, render_all

init()

#====== Screen ======#
screen = display.set_mode()
display.set_caption("ping pong")
clock = time.Clock()
width = screen.get_width()
height = screen.get_height()

#====== Sprits ======#
	# <Ball>
ball = Sprite(
	(width/2, height/2),
	(40, 40),
	"White",
	screen,
	[5, 10]
)
	# <Player 1>
player1 = Sprite(
	((width/2)-60, height-100),
	(100, 30), 
	"Red",
	screen
)
player1_score = 0
	# <Player 2>
player2 = Sprite(
	((width/2)-60, 60),
	(100, 30),
	"Blue",
	screen
)
player2_score = 0

	# <Center Line>
line = Sprite(
	(0, 0),
	(width-40, 5),
	"White",
	screen
)
line.go_center()

	# <Score 1>
font = font.Font(None, 70)
score1 = font.render(f"Player1: {player1_score}", True, "Red")
score1_rect = score1.get_rect()
score1_rect.x = 20
score1_rect.y = ((height/2)-(score1_rect.size[1]/2))+30

	# <Score 2>
score2 = font.render(f"Player2: {player2_score}", True, "Blue")
score2_rect = score1.get_rect()
score2_rect.x = width-245
score2_rect.y = ((height/2)-(score1_rect.size[1]/2))-30

#====== Main Loop ======#
while True:
	# <Smoothly QUIT>
	for i in event.get():
		if i.type == QUIT:
			quit()
			exit()
	
	# <Clear Screen>
	screen.fill((0, 0, 0))
	#=====- Movment ======#
		# <Ball Movment>
	ball.move()
	if ball.rect.top < 0 or ball.rect.bottom > height:
		ball.speed[1] *= -1
	elif ball.rect.left < 0 or ball.rect.right > width:
		ball.speed[0] *= -1
	
		# <Player1 Movment>
	player1.set_x(mouse.get_pos()[0]-(player1.size[0]/2)) # Mouse or Touch Position
	
		# <Player2 Movment By Ball Position>
	player2.set_x(ball.get_x()-(ball.size[0]/2+20))
	
		# <When Ball Touch Player 1>
	if ball.colliderect(player1):
		ball.set_y(player1.get_y()-ball.size[1])
		ball.set_color("Red")
		player1.set_color("Grey")
		player2.set_color("Blue")
		ball.speed[1] *= -1
		
		# <When Ball Touch Player 2>
	elif ball.colliderect(player2):
		ball.set_y(player2.get_y()+ball.size[1])
		ball.set_color("Blue")
		player2.set_color("Grey")
		player1.set_color("Red")
		ball.speed[1] *= -1
	
	#====== Points System ======#
		# <Player 1 Was Take Goal>
	if ball.rect.top <= 0:
		ball.go_center()
		player1_score += 1
		score1 = font.render(f"Player1: {player1_score}", True, "Red")
	
		# <Player 2 Was Take Goal>
	elif ball.rect.bottom >= height:
		ball.go_center()
		player2_score += 1
		score2 = font.render(f"Player2: {player2_score}", True, "Blue")
	
	# <Render All method>
	render_all([
		line,
		player1,
		ball,
		player2
	])
	screen.blit(score1, score1_rect)
	screen.blit(score2, score2_rect)
	
	display.update()
	display.flip()
	clock.tick(60)