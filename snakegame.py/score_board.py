
from turtle import Turtle
ALIGN = "center"
FONT = ("Arial",24,"normal")
class Score(Turtle):
    def __init__(self) -> None:
       super().__init__ ()
       self.score= 0
       self.color("white")
       self.penup()
       self.goto(x=0,y=270)
       self.hideturtle()
       self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGN,font= FONT)

    def game_over(self):
        self.goto(x=0, y=0) 
        self.write("GAME OVER",align=ALIGN,font= FONT) 
    def increase_score(self):
        self.score +=1
        self.clear()
        self.update_scoreboard()