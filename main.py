from turtle import Turtle, Screen 
from game_turtle import GameTurtle
from car import Car
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)
turtle = GameTurtle()

screen.listen()
screen.onkey(turtle.move_up, "Up")

game_is_on = True 

while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    

screen.exitonclick()