from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.pl1 = 0
        self.pl2 = 0
        self.scorereset()

    def increase(self,player):
        if player == 1:
            self.pl1 += 1
        if player == 2:
            self.pl2 += 1

    def scorereset(self):
        self.clear()
        self.goto(-100, 260)
        self.write(f" {self.pl1}", align=ALIGNMENT, font=FONT)
        self.goto(100, 260)
        self.write(f" {self.pl2}", align=ALIGNMENT, font=FONT)
