# Simple Pong in Python 3 for Beginners
# By @TokyoEdTech
# Part 10: Simplifying Your Code (One Year and a Half Later!)
import random
import turtle
import os

wn = turtle.Screen()
wn.title("Pong by @TokyoEdTech")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball1 = turtle.Turtle()
ball1.speed(0)
ball1.shape("square")
ball1.color("green")
ball1.penup()
ball1.goto(0, 0)
ball1.dx = 0.60
ball1.dy = -0.60

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Function
def paddle_a_up():
    y1 = paddle_a.ycor()
    y1 += 40
    if (y1 > 250):
        y1=250
        paddle_a.sety(y1)
    paddle_a.sety(y1)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 40
    if(y<-250):
        y=-250
    paddle_a.sety(y)









# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "Up")
wn.onkeypress(paddle_a_down, "Down")
aispeed=0.55
def ai(ai,ball):

    aiy=ai.ycor()
    bally=ball.ycor()
    if(aiy>bally and aiy>-215):
        ai.sety(aiy-aispeed)
    if(aiy<bally and aiy<215):
        ai.sety(aiy+aispeed)



while True:
    wn.update()
    ai(paddle_b,ball1)

    ball1.setx(ball1.xcor() + ball1.dx)
    ball1.sety(ball1.ycor() + ball1.dy)

    # Border checking
    if ball1.ycor() > 290:
        ball1.sety(290)
        ball1.dy *= -1
        os.system("afplay bounce.wav&")

    if ball1.ycor() < -290:
        ball1.sety(-290)
        ball1.dy *= -1
        os.system("afplay bounce.wav&")

    if ball1.xcor() > 390:
        ball1.goto(0, 0)
        y=random.randint(-290,290)
        ball1.sety(y)
        ball1.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball1.xcor() < -390:
        ball1.goto(0, 0)
        y=random.randint(-290,290)
        ball1.sety(y)    
        ball1.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collisions
    if (ball1.xcor() > 340 and ball1.xcor() < 350) and (ball1.ycor() < paddle_b.ycor() + 50 and ball1.ycor() > paddle_b.ycor() -50):
        ball1.setx(340)
        ball1.dx *= -1
        os.system("afplay bounce.wav&")

    if (ball1.xcor() < -340 and ball1.xcor() > -350) and (ball1.ycor() < paddle_a.ycor() + 50 and ball1.ycor() > paddle_a.ycor() -50):
        ball1.setx(-340)
        ball1.dx *= -1
        os.system("afplay bounce.wav&")

