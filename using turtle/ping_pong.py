import turtle as tr
from random import uniform, choice
import time

#=== Window ===#
window = tr.Screen()
window.title("ping pong")
window.tracer(0)
window.bgcolor("#000")
window.listen()

width = window.window_width()/2
height = window.window_height()/2

#====== Game Object ======#
	# <Ball>
ball = tr.Turtle()
ball.speed(0)
ball.shape("circle")
ball.shapesize(stretch_len=1.5, stretch_wid=1.5)
ball.color("#999")
ball.goto(0, 0)
ball_dx, ball_dy = -1, -1
ball_speed = 5
ball.pensize(10)

	# <Center Line>
center_line = tr.Turtle()
center_line.speed(0)
center_line.shape("square")
center_line.color("white")
center_line.shapesize(stretch_len=30, stretch_wid=.01)
center_line.goto(0, 0)

	# <Center Circle>
center_circle = tr.Turtle()
center_circle.speed(1)
center_circle.color("white")
center_circle.penup()
center_circle.hideturtle()
center_circle.goto(0, -90)
center_circle.pendown()
center_circle.pensize(3)
for i in range(120):
	center_circle.forward(5)
	center_circle.left(3)

	# <Player1>
player1 = tr.Turtle()
player1.speed(0)
player1.shape("square")
player1.color("red")
player1.shapesize(stretch_len=5, stretch_wid=1)
player1.penup()
player1.goto(0, -(height-80))
player1_score = 0

	# <Player2>
player2 = tr.Turtle()
player2.speed(0)
player2.shape("square")
player2.color("blue")
player2.shapesize(stretch_len=5, stretch_wid=1)
player2.penup()
player2.goto(0, height-80)
player2_score = 0

	# <Score1>
score1 = tr.Turtle()
score1.speed(0)
score1.color("red")
score1.penup()
score1.goto(-200, -50)
score1.write(f"Player1: {player1_score}",
	align="center",
	font=("Courier", 8, "normal")
)
score1.hideturtle()

	# <Score2>
score2 = tr.Turtle()
score2.speed(0)
score2.color("blue")
score2.penup()
score2.goto(200, 20)
score2.write(f"Player2: {player2_score}",
	align="center",
	font=("Courier", 8, "normal")
)
score2.hideturtle()

#====== Object Movment ======#
	# <Player1 Movment>
def clickHandel(x=0, y=0):
	player1.setx(x)
window.onclick(clickHandel)

	# <Ball Movement>
def ballMove():
	ball.setx(ball.xcor() + (ball_dx * ball_speed))
	ball.sety(ball.ycor() + (ball_dy * ball_speed))

#====== Main Loop ======#
while True:
	window.update()
	ballMove()
	
	# <Responseve Ball>
	if float(ball.xcor()) <= -((width)-10):ball_dx *= -1
	if float(ball.xcor()) >= ((width)-10):ball_dx *= -1
	if float(ball.ycor()) <= -((height)-10):
		player2_score += 1
		score2.clear()
		score2.write(
			f"Player2: {player2_score}",
			align="center",
			font=("Courier", 8, "normal")
		)
		ball.goto(0, 0)
		ball_dy *= -1
		ball.clear()
	if float(ball.ycor()) >= ((height)-10):
		player1_score += 1
		score1.clear()
		score1.write(
			f"Player: {player1_score}",
			align="center",
			font=("Courier", 8, "normal")
		)
		ball.goto(0, 0)
		ball_dy *= -1
	# <Player2 Folow Ball>
	player2.setx(ball.xcor())
	
	# <Player1 Folow Ball>
	#player1.setx(ball.xcor())
	
	# <Ball Touching Players>
	if (ball.xcor() >= player1.xcor()-(20 * 4)
	and ball.xcor() <= player1.xcor()+(20 * 4)
	and ball.ycor() >= player1.ycor()-(20 * 1)
	and ball.ycor() <= player1.ycor()+(20 * 1)):
		#ball.color("#ffa1a1")
		ball.color("red")
		ball_dy *= -1
		ball.clear()
	
	if (ball.xcor() >= player2.xcor()-(20 * 4)
	and ball.xcor() <= player2.xcor()+(20 * 4)
	and ball.ycor() >= player2.ycor()-(20 * 1)
	and ball.ycor() <= player2.ycor()+(20 * 1)):
		#ball.color("lightblue")
		ball.color("blue")
		ball_dy *= -1
		ball.clear()
	ball_speed += .001