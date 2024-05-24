#from module_nmae import, thing we want to import
# if we want to import everything from the module we can use the * sign
# from turtle import *
# Aliasing Modules: we import the module which we want and give it aalias name .. the name which is given by the user to the module
# it is used to represent the modules if the modules have a huge name
# eg: import turtle as t
from turtle import Turtle,Screen,colormode
import random



tim = Turtle()
colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "brown", "black", "white"]
tim.speed(0)
tim.shape("turtle")
tim.color("red")

#TODO1: Draw a square using the turtle
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

#TODO2: Draw a dash line
# for _ in range(20):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown() 

#TODO3: Draw a triangle , square,pentagon,,hexagon,heptagon,octagon,nonadon and decagon

# def draw_shape(num_sides):
#     angle = 360/ num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)

# for shape_side_n in range(3,11):
#     draw_shape(shape_side_n)

#TODO4: draw a random walk
#pensize(): decides the thickness of the  line
#speed(): sets turtles speed from 0 to 10. 6 is normal.
#colour(): colours which can be used for the turtle
#hideturtle(): Makes the turtle invisible.
#settheading(): sets the orientation of the turtle

# tim.speed(0)
# tim.pensize(15)
# direction = [0,90,180,270]
# for _ in range(200):
#     tim.hideturtle()
#     tim.color(random.choice(colors))
#     tim.forward(50)
#     tim.setheading(random.choice(direction))
    
#TODO5:Make a sirograph

#shapesize(): to decide the shape of the cirlce
#tilt(): rotates the turtle shape by angle from it
def draw_spirograph(size_of_gap):
    for _ in range (int(360/ size_of_gap)):
        tim.color(random.choice(colors))
        tim.circle(100)  
        # we need to tilt the current heading to draw another circle
        current_heading = tim.heading()
        tim.setheading(current_heading + size_of_gap)   
        

draw_spirograph(5)





screen = Screen()
screen.exitonclick()