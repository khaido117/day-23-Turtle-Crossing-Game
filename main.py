from turtle import Turtle, Screen 
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time

#Screen setup.
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)

#Create objects. 
player = Player()
score = Scoreboard()
car_manager = CarManager()

#Screen keyboard.
screen.listen()
screen.onkey(player.move_up, "Up")

#Game start here.
game_is_on = True 

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()

    #Detect when player hit the car.
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            score.game_over()
            game_is_on = False

    #Detect when player hit the top edge of the screen.
    if player.ycor() == -100:
        score.increase_level()
        score.update_score()
        player.back_position()
        car_manager.level_up()
   
screen.exitonclick()