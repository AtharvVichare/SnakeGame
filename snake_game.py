import snake
import turtle
import time
from Score_board import Score

from food import Food

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

Snake = snake.Snake()
food = Food()
score = Score()
screen.listen()
screen.onkey(Snake.up, "Up")
screen.onkey(Snake.down, "Down")
screen.onkey(Snake.left, "Left")
screen.onkey(Snake.right, "Right")

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    Snake.move()
    if Snake.head.distance(food) < 15:
        score.inc_score()
        food.change_pos()
        Snake.update()
    if Snake.collision():
        Snake.reset()
        score.reset()



screen.exitonclick()
