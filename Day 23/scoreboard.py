from turtle import Turtle

class Score(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.setpos(-250,250)
        self.hideturtle()
        score = 0
        self.increase_score(score)
        

    def increase_score(self,score):
        self.clear()
        self.write(arg=f"Score: {score}", font=('Comic Sans',15,'normal'))
        

