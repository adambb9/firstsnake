from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

MOVE_DISTANCE = 20

class Snake:

    def __init__(self):
        self.body = []
        self.x_pos = 0
        self.y_pos = 0
    
    def initialise_snake(self, length):
        for i in range(length):
            new_snake = Turtle("square")
            new_snake.penup()
            new_snake.color("white")
            self.body.append(new_snake)
            new_snake.setpos((self.x_pos - (self.body.index(new_snake)*20)), 0)

    def add_body(self, position):
        new_snake = Turtle("square")
        new_snake.penup()
        new_snake.color("white")
        new_snake.goto(position)
        self.body.append(new_snake)
        
        
    def extend_snake(self):
        self.add_body(self.body[-1].position())
        
    
    def move_snake(self):
        for segment in range(len(self.body) - 1, 0, -1):
            new_x = self.body[segment -1].xcor()
            new_y = self.body[segment -1].ycor()
            self.body[segment].goto(new_x, new_y)
        self.body[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.body[0].heading() != DOWN:
            self.body[0].setheading(UP)

    def right(self):
        if self.body[0].heading() != LEFT:
            self.body[0].setheading(RIGHT)

    def left(self):
        if self.body[0].heading() != RIGHT:
            self.body[0].setheading(LEFT)

    def down(self):
        if self.body[0].heading() != UP:
            self.body[0].setheading(DOWN)

