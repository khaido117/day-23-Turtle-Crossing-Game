from turtle import Turtle
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-240, 270)
        self.level = 1 
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Level: {self.level}", align="center", font=FONT)
    
    def increase_level(self):
        self.clear()
        self.level += 1

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align="center", font=FONT)
        
