from turtle import Turtle, Screen 
from game_turtle import GameTurtle
from car import Car
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Turtle Crossing Game")
screen.tracer()
turtle = GameTurtle()

screen.listen()
screen.onkey(turtle.move_up, "Up")


car = Car()
# car.backward(30)
game_is_on = True 

while game_is_on:
    car.move_left()
    time.sleep(0.1)

screen.exitonclick()