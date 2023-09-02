from turtle import Turtle, Screen
import random

car_colors = ["black", "green", "blue", "orange", "red"]

class Car(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.shape("square")
        self.shapesize(1, 2.5)
        self.color(random.choice(car_colors))
        self.penup()
        self.goto(x_cor, y_cor)

    def move_left(self):
        self.backward(10)


# Example usage:
screen = Screen()
screen.setup(width=800, height=600)
cars_list = create_cars()

# This will create cars at different y_cor positions within the specified range.
