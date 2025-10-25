from turtle import *
class Score:
    def __init__(self):
        self.score = 0
        self.turtle = Turtle()
        self.turtle.color("white")
        self.turtle.hideturtle()
        self.turtle.penup()
        self.turtle.speed(0)
        self.turtle.goto(-100,270)
    def add_score(self):
        self.score = self.score + 1
    def show_score(self):
        self.turtle.clear()
        self.turtle.write(f"Score:{self.score}",font=("Arial",30,"normal"),align="left")
    def game_over(self):
        self.turtle.goto(0,0)
        self.turtle.write(f"GAME OVER", font=("Arial", 30, "normal"), align="center")
    def reset_score(self):
        self.score = 0