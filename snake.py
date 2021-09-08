from turtle import Screen, Turtle
import time


class Snake:

    def __init__(self):
        self.body = []
        self.length = 3
        self.x_pos = 0
        self.y_pos = 0
    
    def initialise_snake(self):
        for i in range(self.length):
            self.add_body()


    def add_body(self):
        new_snake = Turtle("square")
        new_snake.penup()
        new_snake.pencolor("white")
        new_snake.fillcolor("white")
        self.body.append(new_snake)
        new_snake.setpos((self.x_pos - (self.body.index(new_snake)*20)), 0)
        
        

    def move_snake(self):
        for segment in range(self.length - 1, 0, -1):
            new_x = self.body[segment -1].xcor()
            new_y = self.body[segment -1].ycor()
            self.body[segment].goto(new_x, new_y)
        self.body[0].forward(20)

    