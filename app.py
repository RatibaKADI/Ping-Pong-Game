
import turtle 
#screen setup

wind=turtle.Screen()#initialize screen 
wind.title("Ping Pong by Ratiba")#title of the window
wind.bgcolor("black")#background wolor
wind.setup(width=800,height=600)
wind.tracer(0)#stops the window from updating automatically

#main game loop
#raquelette1
madrab1=turtle.Turtle()#inialize turtle object(shape)
madrab1.speed(0)#set the speed of the animation
madrab1.shape("square")#set the shape of the object
madrab1.color("blue")#set the color of the shape
madrab1.shapesize(stretch_wid=5,stretch_len=1)#stretches the shape to meet the size
madrab1.penup()#stops the object from drawing lines
madrab1.goto(-350,0)#set the position of the object
#raquelette2
madrab2=turtle.Turtle()
madrab2.speed(0)
madrab2.shape("square")
madrab2.color("red")
madrab2.shapesize(stretch_wid=5,stretch_len=1)
madrab2.penup()
madrab2.goto(350,0)


#ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.5
ball.dy = 0.5
#functions

def madbrab1_up():#function to move the first raquelette up
    y=madrab1.ycor() 
    y+=20
    madrab1.sety(y)
def madbrab1_down():#function to move the first raquelette down
    y=madrab1.ycor() 
    y-=20
    madrab1.sety(y)

def madrab2_up():#function to move the first raquelette up
    y=madrab2.ycor() 
    y+=20
    madrab2.sety(y)
def madbrab2_down():#function to move the first raquelette down
    y=madrab2.ycor() 
    y-=20
    madrab2.sety(y)
#keyboard bindings
wind.listen()#tell the window to expect keyboard input
wind.onkeypress(madbrab1_up,"w")#when pressing w the function madbrab1_up is invoked
wind.onkeypress(madbrab1_down,"s")#when pressing s the function madbrab1_down is invoked
wind.onkeypress(madrab2_up,"Up")#when pressing Up the function madrab2_up is invoked
wind.onkeypress(madbrab2_down,"Down")#when pressing Down the function madbrab2_down is invoked
  
while True:
    wind.update()#updates screen evrytime the loop runs
    #move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy*=-1
    if ball.ycor() <-290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() >390:
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() <-390:
        ball.goto(0, 0)
        ball.dx *= -1    

    #tassadome al midrabe ou lkora
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < madrab2.ycor() + 40 and ball.ycor() > madrab2.ycor() -40 ):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < madrab1.ycor() + 40 and ball.ycor() > madrab1.ycor() -40 ):
        ball.setx(-340)
        ball.dx *= -1    


             
    
  
    



