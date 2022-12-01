from turtle import Turtle
# imports

ALIGN = "center"
FONT = ("Arial", 50, "normal")
# constants

class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.goto(position)
        self.color("white")
        self.hideturtle()
        self.write(f"{self.score}", align=ALIGN, font=FONT)
    # Makes a scoreboard item at certain position

    def update_scoreboard(self):
        self.clear()
        self.score += 1
        self.write(f"{self.score}", align=ALIGN, font=FONT)
