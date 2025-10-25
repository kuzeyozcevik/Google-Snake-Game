import time
import turtle
from turtle import *
from snake import Snake
from apple import Apple
from score import Score
#Screen Adjusting
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(1==2)
#Creating Snake Body
snake = Snake()
screen.update()
#Creating Apple
apple = Apple()
#Creating Score Object
score = Score()
#Main Game
def game():
    isContinue = True
    while isContinue:
        screen.update()
        score.show_score()
        snake.move()
        if snake.check_border():
            isContinue = False
            score.game_over()
            score.reset_score()
        time.sleep(0.04)
        if snake.snake_parts[0].distance(apple) < 20:

            apple.random_move()
            score.add_score()
            snake.add_snake()
        if snake.check_self_collision():
            isContinue = False
            score.game_over()
            score.reset_score()
def again_game():
    screen.reset()
    snake = Snake()
    apple = Apple()
    score = Score()
    turtle.listen()
    turtle.onkey(snake.up, "w")
    turtle.onkey(snake.down, "s")
    turtle.onkey(snake.right, "d")
    turtle.onkey(snake.left, "a")
    turtle.onkey(again_game, "c")
    isContinue = True
    while isContinue:
        screen.update()
        score.show_score()
        snake.move()
        if snake.check_border():
            isContinue = False
            score.game_over()
            score.reset_score()
        time.sleep(0.04)
        if snake.snake_parts[0].distance(apple) < 20:
            apple.random_move()
            score.add_score()
            snake.add_snake()
        if snake.check_self_collision():
            isContinue = False
            score.game_over()
            score.reset_score()
#Creating Functions and Listening Methods
turtle.listen()
turtle.onkey(snake.up,"w")
turtle.onkey(snake.down,"s")
turtle.onkey(snake.right,"d")
turtle.onkey(snake.left,"a")
turtle.onkey(again_game,"c")
#Creating Main GamePlay
game()
#Screen Mainloop
screen.mainloop()