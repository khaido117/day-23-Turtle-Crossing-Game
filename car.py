from turtle import Turtle 
import random

car_colors = ["black", "green", "blue", "orange", "red"]

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(1,2.5)
        self.color(random.choice(car_colors))
        self.penup()
        self.goto(390, 100)

    def move_left(self):
        self.backward(10)