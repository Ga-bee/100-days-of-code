from turtle import Turtle

class Score(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.count =0
        with  open('Day 20-21/snake_game/data.txt') as data:
            self.high_score = int(data.read())
        self.color('white')
        self.penup()
        self.hideturtle()
        self.setpos(0,250)
        self.update_score()

      
         
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.count}  High Score: {self.high_score}", move= False, align='center', font = ("Comic Sans", 24, "normal"))
        

    def reset(self) -> None:
        if self.count > self.high_score:
           self.high_score = self.count
           with open('Day 20-21/snake_game/data.txt', mode = 'w') as w_score:
              w_score.write(f"{self.high_score}")
        self.count = 0
        self.update_score()

    def increase_score(self):
        self.count += 1
        self.update_score()        
