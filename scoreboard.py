from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        x_pos, y_pos = 0, 275
        self.goto(x_pos, y_pos)
        self.score = 0
        self.write(F"Score: {self.score}", align="center")

    #score board writes to screen but doesnt update
    def refresh(self):
        self.clear()
        x_pos, y_pos = 0, 275
        self.goto(x_pos, y_pos)
        self.write(F"Score: {self.score}", align="center")
        
        
