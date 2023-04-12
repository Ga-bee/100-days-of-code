from turtle import Turtle

class Score(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0,200)
        self.l_score = 0
        self.r_score = 0
        self.write(arg=f"{self.l_score} - {self.r_score}",align='center', font=("Arial",50,'bold'))

        

    def left_point(self):
        self.l_score += 1
        self.clear()
        self.write(arg=f"{self.l_score} - {self.r_score}",align='center', font=("Arial",50,'bold'))

    def right_point(self):
        self.r_score += 1
        self.clear()
        self.write(arg=f"{self.l_score} - {self.r_score}",align='center', font=("Arial",50,'bold'))