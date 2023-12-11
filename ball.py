from turtle import Turtle
import random
class CreateBall(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.shapesize(0.5)
        self.penup()
