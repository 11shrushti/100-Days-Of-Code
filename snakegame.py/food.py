from turtle import Turtle
import random

# we are going to inheret the ablities of the turtle class in food class
class Food(Turtle):
    """It is going to create a small circle of the food and everytime the snake touches the food it is going to render to a new random location."""
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("white")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
          x_value = random.randint(-280,280)
          y_value = random.randint(-280,280)
          self.goto(x_value, y_value)