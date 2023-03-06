import turtle 


win = turtle.Screen()
win.title("Ping Pong")
win.bgcolor("brown")
win.setup(width=800, height=600)
win.tracer(0) 


#Score
board = turtle.Turtle()
board.speed(0)
board.color("black")
board.penup()
board.hideturtle()
board.goto(0, 250)
board.write("Player 1: 0        Player 2: 0" , align="center", font=("Courier new", 18))


#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("black")
paddle_a.shapesize(stretch_wid=6, stretch_len=1, outline=1)
paddle_a.penup()
paddle_a.goto(-350, 0)



#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("black")
paddle_b.shapesize(stretch_wid=6, stretch_len=1, outline=1)
paddle_b.penup()
paddle_b.goto(350, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("pink")
ball.penup()
ball.goto(0, 0)
ball.dx=0.15
ball.dy=0.15


#Functions
def paddle_a_up():
    y=paddle_a.ycor()
    y+=30
    paddle_a.sety(y)

def paddle_a_down():
    y=paddle_a.ycor()
    y-=30
    paddle_a.sety(y)

def paddle_b_up():
    y=paddle_b.ycor()
    y+=30
    paddle_b.sety(y)

def paddle_b_down():
    y=paddle_b.ycor()
    y-=30
    paddle_b.sety(y)    

#Keyboard bindings
win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")


# Main Game Loop
while True:
    win.update()
    #ball movement
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #Borders
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *=-1

    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy *=-1

    if ball.xcor()>390:
        ball.goto(0, 0)
        ball.dx*=-1
        ball.dx=0.15
        ball.dy=0.15

    if ball.xcor()<-390:
        ball.goto(0, 0)
        ball.dx*=-1
        ball.dx=0.15
        ball.dy=0.15
   
    #Bounce
    if (ball.xcor()>340 and ball.xcor()<350)and(ball.ycor()<paddle_b.ycor()+60 and ball.ycor()>paddle_b.ycor()-60):
        ball.setx(340)
        ball.dx*=-1
        ball.dx*=1.01
        ball.dy*=1.01

    if (ball.xcor()<-340 and ball.xcor()>-350)and(ball.ycor()<paddle_a.ycor()+60 and ball.ycor()>paddle_a.ycor()-60):
        ball.setx(-340)
        ball.dx*=-1
        ball.dx*=1.5
        ball.dy*=1.5