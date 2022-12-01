from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
# imports

# SCREEN SETTINGS
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My pong game")
screen.tracer(0)

# PADDLE POSITION
LEFT_POS = -screen.window_width() / 2 + 20
RIGHt_POS = screen.window_width() / 2 - 20

# DOTTED LINE
line = Turtle()
line.hideturtle()
line.color("white")
line.penup()
line.goto(0, -screen.window_height())
line.pendown()
line.left(90)
while line.ycor() <= screen.window_height():
    line.forward(20)
    line.penup()
    line.forward(20)
    line.pendown()

# PADDLES
l_paddle = Paddle((LEFT_POS, 0))
r_paddle = Paddle((RIGHt_POS, 0))
# initialize paddles using Paddle Object

# SCORE
l_score = Scoreboard((-40, 220))
r_score = Scoreboard((40, 220))
# initialize scores using Scoreboard Object

# BALL
ball = Ball()
# initialize ball using Ball Object

# SCREEN LISTEN FOR INPUTS
screen.listen()

# PLAYER ON THE LEFT
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# PLAYER ON THE RIGHT
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

game_is_on = True
# game status
while game_is_on:
    screen.update()
    # screen.tracer is set to 0 we have to update it manually
    time.sleep(ball.move_speed)
    # refresh rate, the closer to 0 the faster
    ball.move()
    ball.check_collision_top_and_bottom()

    # CHECK COLLISIONS:
    # SIDES COLLISION

    if ball.check_collision_sides() == "left":
        ball.reset_ball(ball.RIGHT)
        r_score.update_scoreboard()
        ball.speed_reset()
    elif ball.check_collision_sides() == "right":
        ball.reset_ball(ball.LEFT)
        l_score.update_scoreboard()
        ball.speed_reset()

    # function will return left or right
    # used to update scoreboard, reset ball speed, set ball heading

    # PADDLE COLLISION
    if l_paddle.distance(ball) < 40:
        ball.paddle_collision(ball.RIGHT)
        ball.speed_increase()
    elif r_paddle.distance(ball) < 40:
        ball.paddle_collision(ball.LEFT)
        ball.speed_increase()

    # if ball is in 40px distance of the paddle it will register it as a hit

screen.exitonclick()
