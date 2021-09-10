#building the classic snake game
from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard



screen  = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

snake.initialise_snake(10)

food = Food()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move_snake()
    
    #detect collision with food
    if snake.body[0].distance(food) < 15:
        scoreboard.increase_score(1)
        food.refresh()


    

        





screen.exitonclick()