from turtle import Turtle,Screen
STARTING_POSITION = [(0,0), (-20,0), (-40,0)]#constants are named in all capas
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        self.segement =[]#attribute: need to use self when working in a class
        self.create_snake()#method

    #TODO1: Crete snake body
    def create_snake(self):
         for position in STARTING_POSITION:
             self.add_segment(position)
            
    
            # segment_2 = Turtle()
            # segment_2.shape("square")
            # segment_2.color("white")
            # segment_2.goto(x= -20, y=0)#the segemet_1 is 20*20 from the orgin and we have to move the second square to the left to x=-20 and y=0

            # segment_3 = Turtle()
            # segment_3.shape("square")
            # segment_3.color("white")
            # segment_3.goto(x=-40,y=0)
    
    def add_segment(self,position): 
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segement.append(new_segment)
        

           


    def extend(self):
          # add a new segement to the snake
          self.add_segment(self.segement[-1].position())
                
    def move(self):
        for seg_num in range(len(self.segement)-1, 0,-1):# its start , stop and step
            new_x = self.segement[seg_num - 1].xcor()
            new_y = self.segement[seg_num - 1].ycor()
            self.segement[seg_num].goto(new_x, new_y)#last segment to go to 2nd position
        self.segement[0].forward(MOVE_DISTANCE)

    def up(self):
         if self.segement[0].heading() != DOWN:
            self.segement[0].setheading(UP)

    def down(self):
        if self.segement[0].heading() != UP:
            self.segement[0].setheading(DOWN)

    def  left(self):
        if self.segement[0].heading() != RIGHT:
            self.segement[0].setheading(LEFT)

    def right(self):
        if self.segement[0].heading() != LEFT:
                self.segement[0].setheading(RIGHT)    