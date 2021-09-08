#building the classic snake game
from turtle import Screen, Turtle

screen  = Screen ()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

snake_body = []

x_pos = 0

length_of_snake = 3

for i in range(length_of_snake):
    new_snake = Turtle("square")
    new_snake.penup()
    new_snake.pencolor("white")
    new_snake.fillcolor("white")
    snake_body.append(new_snake)
    new_snake.setpos(x_pos - (snake_body.index(new_snake)*20) - (snake_body.index(new_snake)*1), 0)






screen.exitonclick()