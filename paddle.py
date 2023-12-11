from turtle import Turtle
class CreatePaddle(Turtle):
    def __init__(self,pos):
        super().__init__()
        self.shape("square")
        self.color('white')
        self.shapesize(1,3,1)
        self.setheading(90)
        self.penup()
        self.goto(pos)

    def createline(self):
        self.shapesize(1,1,1)
        self.hideturtle()
        self.pendown()
        self.setheading(90)
        while self.ycor() > -310:
            self.pendown()
            self.backward(10)
            self.penup()
            self.backward(10)