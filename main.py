import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Start")
screen.tracer(0)

player_turtle = Player()


screen.listen()
screen.onkey(player_turtle.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    player_turtle.move_up()
    
    
screen.exitonclick()