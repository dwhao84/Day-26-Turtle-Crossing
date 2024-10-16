STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle

class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.go_to_start()
        self.setheading(90)
        
    def move_up(self):
        new_y = self.ycor() + 10
        self.goto(self.xcor(), new_y)
    
    def go_to_start(self):
        self.goto(STARTING_POSITION)
    
    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            print("Over the finish line")
            return True
        else:
            return False
            
            