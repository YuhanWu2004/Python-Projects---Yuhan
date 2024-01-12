#Turtle Grahics Games Michelle
'''My game might be a bit slow as I found if I set the tracer to 2 or 3
it would be too fast and hurt your eyes.'''
import turtle #1
import math #4
import random #4

#1 set up screen
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.tracer(1.8)

#draw border-3
mypen = turtle.Turtle()
mypen.penup()
mypen.setpos(-260,-260)
mypen.pendown()
mypen.pensize(3)
for side in range(4):
    mypen.fd(520)
    mypen.lt(90)
mypen.hideturtle()
mypen.speed(0)

#creat the score variable
score = 0

#1 create player turtle
player = turtle.Turtle()
player.color("pink")
player.shape("turtle")
player.penup()
player.speed(0)

#creat multiple goals - 7
maxGoals = 6
goals = []
for count in range(maxGoals):
    
#4 create goal
    goals.append (turtle.Turtle())
    goals[count].color("red")
    goals[count].shape("circle")
    goals[count].pu()
    goals[count].speed(0)
    goals[count].setpos(random.randint(-250,250), random.randint(-250,250))
     



#set speed variable - 1
speed = 1

#define functions

def turnleft():
    player.left(30)

def turnright():
    player.right(30)

def increasespeed():
    global speed
    speed += 1


# 5
def isCollision(t1,t2):
    
    d = math.sqrt(math.pow(t1.xcor() - t2.xcor(),2)+math.pow(t1.ycor() - t2.ycor(),2))
    if d <20:
        return True
    else:
        return False

#set keyboard bindings
turtle.listen()
turtle.onkey(turnleft,"Left")
turtle.onkey(turnright,"Right")
turtle.onkey(increasespeed,"Up")


while True:
    player.forward(speed)

    #Boundary checking
    if player.xcor()>250 or player.xcor()<-250:
        player.left(180)

    if player.ycor()>250 or player.ycor()<-250:
        player.right(180)
    

    #collision checking
    if isCollision(player, goals[count]):
        goals[count].setpos(random.randint(-250,250),random.randint(-250,250))
        goals[count].right(random.randint(0,360))
    #7
    for count in range(maxGoals):
        
        #Move the goal around #6
        goals[count].fd(3)

        #Boundary checking
        if goals[count].xcor()>235 or goals[count].xcor()<-235:
            goals[count].right(180)

        if goals[count].ycor()>235 or goals[count].ycor()<-235:
            goals[count].right(180)

        #collision checking
        if isCollision(player, goals[count]):
            goals[count].setpos(random.randint(-250,250),random.randint(-250,250))
            goals[count].right(random.randint(0,360))
            score += 1
            #draw the score on the screen
            mypen.undo()
            mypen.penup()
            mypen.hideturtle()
            mypen.setpos(-250,280)
            scorestring = "Score: %s" %score
            mypen.write(scorestring, False, align = "left", font=("Areial",14,"normal"))

delay = raw_inout("PressEnter to finish.")
