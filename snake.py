from turtle import Screen, Turtle
import time


class Snake:

    def __init__(self):
        self.body = []
        self.length = 3
        self.x_pos = 0
        self.y_pos = 0
    

    def add_body_part(self):
        for i in range(length_of_snake):
            new_snake = Turtle("square")
            new_snake.penup()
            new_snake.pencolor("white")
            new_snake.fillcolor("white")
            self.body.append(new_snake)
            new_snake.setpos((self.x_pos - (snake_body.index(new_snake)*20)), 0)

    


for segment in range(len(snake_body) - 1, 0, -1):
        new_x = snake_body[segment -1].xcor()
        new_y = snake_body[segment -1].ycor()
        snake_body[segment].goto(new_x, new_y)
    snake_body[0].forward(20)