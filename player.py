from turtle import Turtle
STARTING_POINT = (0, -280)
MOVE_DISTANCE = 10 
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POINT)

    #Move the player forward.
    def move_up(self):
        self.forward(MOVE_DISTANCE)

    #Back to the original position when game started.
    def back_position(self):
        self.goto(STARTING_POINT)