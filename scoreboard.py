from turtle import Turtle

class Scoreboard(Turtle):

    def __init(self):
        super().init()
        self.color("white")
        self.write("Score: ", align="center")
        self.score = 0
