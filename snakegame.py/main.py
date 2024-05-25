from turtle import Screen
from snake  import Snake
import time
from food import Food
from score_board import Score

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")# change the bgcolor of the screen
screen.title("My snake game")# sets title on the window screen
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

#TODO3: Control the snake
screen.listen()
screen.onkey(key="Up", fun = snake.up)
screen.onkey(key="Down", fun = snake.down)
screen.onkey(key="Right", fun = snake.right)
screen.onkey(key="Left",fun = snake.left)

#TODO2:Move the sanke
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)#adds 1s delay after all segments have moves
    snake.move()

    #Dectect collision with the food
    if snake.segement[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()


        
    #detect collision with the waal
    if snake.segement[0].xcor() > 280 or snake.segement[0].xcor() < -280 or snake.segement[0].ycor() > 280 or snake.segement[0].ycor() < -280:
        game_is_on = False
        score.game_over()

    #detect collision with the tail
    for segment in snake.segement[1:]:
        
        
        if snake.segement[0].distance(segment) < 10:
            game_is_on = False
            score.game_over()






screen.exitonclick()