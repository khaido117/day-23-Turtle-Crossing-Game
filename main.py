from turtle import Turtle, Screen 
from game_turtle import GameTurtle


screen = Screen()
screen.setup(width=800, height=600)
screen.title("Turtle Crossing Game")
screen.tracer()
turtle = GameTurtle()

screen.listen()
screen.onkey(turtle.move_up, "Up")

screen.exitonclick()