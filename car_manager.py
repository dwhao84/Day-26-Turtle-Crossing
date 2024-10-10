COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

# import framework.
from turtle import Turtle
import random

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(0, STARTING_MOVE_DISTANCE)
    
    def moving(self):
        new_y = self.ycor() + MOVE_INCREMENT
        self.goto(self.xcor(), new_y)