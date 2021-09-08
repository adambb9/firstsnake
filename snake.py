from turtle import Screen, Turtle
import time

MOVE_DISTANCE = 20

class Snake:

    def __init__(self):
        self.body = []
        self.length = 0
        self.x_pos = 0
        self.y_pos = 0
    
    def initialise_snake(self, length):
        for i in range(length):
            self.add_body()
            self.length += 1


    def add_body(self):
        new_snake = Turtle("square")
        new_snake.penup()
        new_snake.color("white")
        self.body.append(new_snake)
        new_snake.setpos((self.x_pos - (self.body.index(new_snake)*20)), 0)
        
    
    def move_snake(self):
        for segment in range(self.length - 1, 0, -1):
            new_x = self.body[segment -1].xcor()
            new_y = self.body[segment -1].ycor()
            self.body[segment].goto(new_x, new_y)
        self.body[0].forward(MOVE_DISTANCE)

    #def snake_heading(self):
        #screen.listen()
        #screen.onkey(key="w", fun=move_forwards)
        #screen.onkey(key="s", fun=move_backwards)
        #screen.onkey(key="a", fun=turn_left)
        #screen.onkey(key="d", fun=turn_right)
        #screen.onkey(key="c", fun=clear)

    


    def move_forwards():
        self.body[0].forward(10)

    def turn_right():
        self.body[0].right(10)

    def turn_left():
        self.body[0].left(10)

    def move_backwards():
        self.body[0].backward(10)

