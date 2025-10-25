from turtle import *
import random

class Apple(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.speed(0)
        random_x_coordinate = random.randint(-280,280)
        random_y_coordinate = random.randint(-280,280)
        self.goto(random_x_coordinate,random_y_coordinate)

    def random_move(self):
        self.hideturtle()
        self.goto(random.randint(-280,280),random.randint(-280,280))
        self.showturtle()