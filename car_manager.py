from turtle import Turtle
import random

COLORS = ["red", "green", "blue", "pink", "yellow"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5 

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle(shape="square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-220, 250)
            new_car.goto(280, random_y)
            self.all_cars.append(new_car)
            new_car.backward(10)

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

    