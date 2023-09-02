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

    def move_left(self):
        self.backward(10)

    def create_car(self):
        y_position = []
        x_position = 390
        for y_cor in range(-240,240,10):
            y_position.append(y_cor)

