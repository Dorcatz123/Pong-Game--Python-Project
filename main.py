from turtle import Turtle, Screen
from paddle import CreatePaddle
from ball import CreateBall
import random, time
from score import Score
FONT = ("Ariel", 30, "normal")

# Create screen:
screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title("Pong Game")


#controls the animation:
screen.tracer(0)

#Create paddle from paddle class:

paddle1= CreatePaddle((350,0))
paddle2 = CreatePaddle((-350,0))
paddle3 = CreatePaddle((0,300))
paddle3.createline()
createball = CreateBall()
createscore = Score()

# move functions:
def move_up_pad1():
  if paddle1.ycor() < 280:
    paddle1.forward(20)

def move_down_pad1():
  if paddle1.ycor() > -280:
    paddle1.backward(20)

def move_up_pad2():
  if paddle2.ycor() < 280:
    paddle2.forward(20)

def move_down_pad2():
  if paddle2.ycor() > -280:
    paddle2.backward(20)



screen.listen()
screen.onkeypress(fun=move_up_pad1, key="w")
screen.onkeypress(fun=move_down_pad1, key="s")
screen.onkeypress(fun=move_up_pad2, key="8")
screen.onkeypress(fun=move_down_pad2, key="2")

game_is_on = True
direction = random.randint(0,360)
while game_is_on:
    time.sleep(0.05)
    screen.update()
    createball.forward(20)
    if paddle1.distance(createball) < 23:
       createscore.increase(1)
       createscore.scorereset()
       direction = random.randint(100,160)
       createball.setheading(direction)

    if paddle2.distance(createball) < 23:
       createscore.increase(2)
       createscore.scorereset()
       direction = random.randint(290,430)
       createball.setheading(direction)

    if createball.ycor() >= 300  or createball.ycor() <= -300:
        direction = 360 - direction
        createball.setheading(direction)

    if createball.xcor() > 400 or createball.xcor() < -400:
        game_is_on = False
        paddle3.goto(-115,0)
        paddle3.write("Game Over!!!",font=FONT)

screen.exitonclick()
