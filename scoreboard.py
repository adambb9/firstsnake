from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        x_pos, y_pos = 0, 275
        self.goto(x_pos, y_pos)
        self.score = 0
        self.update_score()

    #score board writes to screen but doesnt update
    def update_score(self):
        self.write(F"Score: {self.score}", align=ALIGNMENT, font=FONT)
        
    
    def increase_score(self, num):
        self.score += num
        self.clear()
        self.update_score()
