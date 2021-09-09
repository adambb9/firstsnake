from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.score = 0
        self.write(F"Score: {self.score}", align="center")

    #score board writes to screen but doesnt update
        
