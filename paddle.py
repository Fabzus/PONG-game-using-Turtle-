from turtle import Turtle
# imports

class Paddle(Turtle):

    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)
    # Will create a paddle

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
    # Paddle goes up

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
    # Paddle goes down