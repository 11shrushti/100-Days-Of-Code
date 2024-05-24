from turtle import Turtle, Screen
import random
is_race_on = False

screen = Screen()
screen.setup(width=500,height=400)# sets the size and the position of the main window.
#popup and ak the user to make the bet
#textinput(): it shows a popup window for the input 
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red","orange","yellow","green","blue","purple"]
y_positions =[-70, -40 ,-10,20,50,80]
all_turtles = []

for turtle_index in range(0,6):
    new_turtle = Turtle()
    new_turtle.penup()
    new_turtle.shape("turtle")
    new_turtle.color(colors[turtle_index])
    #goto(): defines the x and y values
    new_turtle.goto(x=-230 ,y=y_positions[turtle_index])
    all_turtles.append(new_turtle)
 
if user_bet:
    is_race_on = True 

while is_race_on:
    for turtles in all_turtles:
        rand_distance = random.randint(0, 10)
        turtles.forward(rand_distance)
        if turtles.xcor() > 230:
            is_race_on = False
            winning_color = turtles.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
    
        

screen.exitonclick()