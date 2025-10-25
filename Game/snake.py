
from turtle import *
class Snake:
    def __init__(self):
        self.snake_parts = []
        self.snake_coordinates = [0,-20,-40]
        for coordinate in self.snake_coordinates:
            self.snake = Turtle()
            self.snake.shapesize(1.3)
            self.snake.penup()
            self.snake.shape("square")
            self.snake.color("green")
            self.snake.setx(coordinate)
            self.snake_parts.append(self.snake)

    def move(self):
        for index in range(len(self.snake_parts)-1,0,-1):
            self.snake.speed(0)
            self.snake_parts[index].goto(self.snake_parts[index-1].xcor(),self.snake_parts[index-1].ycor())
        self.snake_parts[0].forward(20)

    def up(self):
        if not self.snake_parts[0].heading() == 270:
            self.snake_parts[0].setheading(90)

    def down(self):
        if not self.snake_parts[0].heading() == 90:
            self.snake_parts[0].setheading(270)

    def right(self):
        if not self.snake_parts[0].heading() == 180:
            self.snake_parts[0].setheading(0)

    def left(self):
        if not self.snake_parts[0].heading() == 0:
            self.snake_parts[0].setheading(180)

    def check_border(self):
        if (self.snake_parts[0].xcor() >= 300 or self.snake_parts[0].xcor() <= -300 or self.snake_parts[0].ycor() >= 300
                or self.snake_parts[0].ycor() <= -300):
            return True

    def check_self_collision(self):
        head = self.snake_parts[0]
        # Baş ile gövdeyi kontrol et
        for part in self.snake_parts[1:]:
            if head.distance(part) < 15:
                return True
        return False

    def add_snake(self):
        for n in range(3):

            self.snake = Turtle(visible=False)
            self.snake.color("black")
            self.snake.hideturtle()
            self.snake.penup()
            self.snake.color("black")
            self.snake.shapesize(1.3)
            self.snake.shape("square")
            self.snake.color("green")
            self.snake_parts.append(self.snake)
            self.snake.showturtle()