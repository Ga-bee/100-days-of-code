from turtle import Turtle

class Score(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.count =0
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.setpos(0,250)
        self.write(f"Score: {self.count}", move= False, align='center', font = ("Comic Sans", 24, "normal"))
        self.count += 1

    # def update_score(self):
        