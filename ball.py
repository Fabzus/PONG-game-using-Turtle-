from turtle import Turtle
import random
from time import sleep
# imports

RIGHT = 45
LEFT = 135
RANDOM_FIRST = [RIGHT, LEFT]
# constants

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.first_move()
        self.check_collision_top_and_bottom()
        self.RIGHT = RIGHT
        self.LEFT = LEFT
        self.move_speed = 0.1

    def move(self):
        self.forward(20)
        # the ball will start moving forward 20 px

    def first_move(self):
        self.setheading(random.choice(RANDOM_FIRST))
        # first ball movement will be randomized

    def check_collision_top_and_bottom(self):
        if self.ycor() > 280 or self.ycor() < -280:
            self.setheading(self.heading() * -1)
            # will check for top or bottom collision and will * -1 the heading

    def check_collision_sides(self):
        if self.xcor() > 400:
            return "right"
        elif self.xcor() < -400:
            return "left"
    # will check for side walls collision and will return the wall it hit

    def reset_ball(self, side):
        self.goto(0, 0)
        self.setheading(side)
    # Will reset the ball to 0,0 and pick a heading

    def paddle_collision(self, side):
        self.setheading(side)
    # Will set a new heading in case it hits a paddle

    def speed_increase(self):
        self.move_speed = self.move_speed*0.9
    # Will increase the speed of the ball

    def speed_reset(self):
        self.move_speed = 0.1
    # Will reset the speed of the ball