from turtle import Turtle, Screen
from scoreboard import ScoreBoard
from Paddels import Paddel
from ball import Ball
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.tracer(0)
screen.title("Pong Game")
screen.bgcolor("black")

# Creating object for paddel class.
r_paddle = Paddel((350, 0))
l_paddle = Paddel((-350, 0))
    
# Creating Instance for Ball class
ball= Ball()

scoreboard = ScoreBoard()

screen.listen()   
screen.onkey(r_paddle.move_forward, "Up")
screen.onkey(r_paddle.move_backward, "Down")

screen.onkey(l_paddle.move_forward, "w")
screen.onkey(l_paddle.move_backward, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_time)
    screen.update()
    ball.moving()
    
    #Detect collision:
    if ball.ycor() > 280 or ball.ycor() < -280:
        #Needs to bounce the ball
        ball.bounce_y()
    
    #Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320: 
        ball.bounce_x()
    
    #Detect r-paddle misses    
    if ball.xcor() > 380:
        time.sleep(.4)
        scoreboard.l_point()
        ball.reset_position()
    
    #Detect l-paddle misses
    if ball.xcor() < -380:
        time.sleep(.4)
        scoreboard.r_point()
        ball.reset_position()
screen.exitonclick()



