# extract the colours from the image using colourgram
# import colorgram
# rgb_colors =[]
# colors = colorgram.extract("damien_hurst_dot.py/hirst_paintig.webp",40)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# Function to normalize RGB values to the range [0, 1]
def normalize_rgb(r, g, b):
    return (r / 255.0, g / 255.0, b / 255.0)
colors = [
    normalize_rgb(55, 111, 22),   # Example of custom color
    normalize_rgb(255, 0, 0),     # Red
    normalize_rgb(0, 255, 0),     # Green
    normalize_rgb(0, 0, 255),     # Blue
    normalize_rgb(255, 255, 0),   # Yellow
    normalize_rgb(255, 0, 255),   # Magenta
    normalize_rgb(0, 255, 255),   # Cyan
    normalize_rgb(128, 0, 0),     # Maroon
    normalize_rgb(0, 128, 0),     # Dark Green
    normalize_rgb(0, 0, 128)      # Navy
]

color_list = [(233, 232, 230), (234, 237, 242), (242, 233, 238), (231, 238, 235), (195, 168, 106), (132, 71, 93),  (57, 103, 133), (142, 91, 63), (175, 158, 52), (144, 168, 187), (119, 35, 58), (219, 201, 135), (143, 172, 156), (63, 110, 84), (31, 40, 72), (178, 95, 118), (71, 31, 41), (88, 155, 128), (44, 55, 99),  (216, 176, 189), (25, 61, 48), (175, 202, 190), (60, 151, 170), (173, 104, 94), (113, 117, 155), (117, 44, 36), (61, 38, 35), (11, 90, 107), (163, 204, 210), (178, 188, 211), (222, 178, 170), (235, 200, 13)]   
from turtle import Turtle, Screen
import random
tim = Turtle()
tim.speed(0)
tim.penup()
tim.hideturtle()

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
num_of_dots = 100
# to create the shape of the tim
for dot_count in range(1,num_of_dots+1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.left(90) 
        tim.forward(50) 
        tim.left(90)  
        tim.forward(500)# to start from the inital path
        tim.setheading(0)
    






screen = Screen()
screen.exitonclick()

   