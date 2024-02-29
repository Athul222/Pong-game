from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.y_move = 10
        self.x_move = 10
        self.move_time = 0.1
        
    def moving(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        
    def bounce_y(self):
        self.y_move *= -1
        
    def bounce_x(self):
        self.x_move *= -1
        self.move_time *= 1.0
        
    def reset_position(self):
        # self.home()
        self.goto(0,0)
        self.move_time = 0.1
        self.bounce_x()
        
        