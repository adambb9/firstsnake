#building the classic snake game
from turtle import Screen, Turtle
import time
from snake import Snake



screen  = Screen ()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

snake.initialise_snake(25)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(1)
    snake.move_snake()
    

    

        





screen.exitonclick()