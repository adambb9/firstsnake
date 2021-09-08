#building the classic snake game
from turtle import Screen, Turtle
import time

screen  = Screen ()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake_body = []



x_pos = 0

length_of_snake = 3

for i in range(length_of_snake):
    new_snake = Turtle("square")
    new_snake.penup()
    new_snake.pencolor("white")
    new_snake.fillcolor("white")
    snake_body.append(new_snake)
    new_snake.setpos((x_pos - (snake_body.index(new_snake)*20)), 0)



game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(1)

    for segment in range(len(snake_body) - 1, 0, -1):
        new_x = snake_body[segment -1].xcor()
        new_y = snake_body[segment -1].ycor()
        snake_body[segment].goto(new_x, new_y)
    snake_body[0].forward(20)

        





screen.exitonclick()