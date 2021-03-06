from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

# Control the screen of the game
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title(" Vintage Nokia 3310 snake game")
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")



game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(snake.move_speed)
    snake.move()
    #     collision between food and snake
    if snake.head.distance(food) < 20 :
        food.refresh()
        scoreboard.increase_score()
        snake.extent()
        snake.increse_speed()


        #     detect collision with wall
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        scoreboard.reset_scoreboard()
        snake.reset()
        # detect collision with tail
        # if head collides with any segment with the tail : trigger game over

    for segments in snake.segments[1:]:
        if snake.head.distance(segments) < 10:
            scoreboard.reset_scoreboard()
            snake.reset()





screen.exitonclick()
