from turtle import Turtle, Screen
MOVE_DISTANCE = 20
up = 90
down = 270
left = 180
right = 0

class Snake:
    def __init__(self) -> None:
        
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.body = self.segments[1:]

    def add_new_segments(self):
        self.snake = Turtle(shape='square')
        self.snake.penup()
        self.snake.color('white')
        self.last_x_cor = self.segments[-1].xcor()
        self.last_y_cor = self.segments[-1].ycor()
        self.snake.setpos(self.last_x_cor,self.last_y_cor)
        self.segments.append(self.snake)

    def create_snake(self):
        o_position = 0
        for body in range (3):
            self.snake = Turtle(shape='square')
            self.snake.penup()
            self.snake.color('white')
            self.snake.setpos(o_position, 0)
            o_position -= 20
            self.segments.append(self.snake)

       

    def move(self):
        for num in range(len(self.segments)-1,0,-1):
            new_x = self.segments[num-1].xcor()
            new_y = self.segments[num-1].ycor()
            self.segments[num].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != down:   
            self.head.seth(90)
        

    def down(self):
        if self.head.heading() != up:
            self.head.seth(270)
        

    def left(self):
        if self.head.heading() != right:
            self.head.seth(180)
        

    def right(self):
        if self.head.heading() != left:
            self.head.seth(0)
        
    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head =self.segments[0]
        self.move()
        


    
    


  