import turtle as t
import time

def rectangle(hor,ver,col):
    t.pendown()
    t.pensize(1)
    t.color(col)
    t.begin_fill()
    for i in range(1,3):
        t.forward(hor)
        t.right(90)
        t.forward(ver)
        t.right(90)
    t.end_fill()
    t.penup()

t.penup()
# t.speed(100)
t.speed('slow')
# Background
t.bgcolor('Dodger blue')
# Left Foot
t.goto(-100,-150)
rectangle(50,20,'blue')
# Right Foot
t.goto(-30,-150)
rectangle(50,20,'blue')
# Left Leg
t.goto(-25,-50)
rectangle(15,100,'grey')
# Right Leg
t.goto(-65,-50)
rectangle(15,100,'grey')
# Stomach
t.goto(-90,100)
rectangle(100,150,'red')
# Left Arm
t.goto(-150,70)
rectangle(60,15,'grey')
# Right Arm
t.goto(-150,115)
rectangle(15,60,'grey')
# Left Upper Arm
t.goto(10,70)
rectangle(60,15,'grey')
# Right Upper Arm
t.goto(55,115)
rectangle(15,60,'grey')
# Neck
t.goto(-50,120)
rectangle(15,20,'grey')
# Face
t.goto(-85, 170)
rectangle(80,60,'red')
# Eyes
t.goto(-60,160)
rectangle(30,10,'white')
# Eyes Left Pupil
# t.goto(-55,155)
# # Left Pupil Modification
t.goto(-60,160)
rectangle(5,5,'black')
# Eyes Right Pupil
t.goto(-40,155)
rectangle(5,5,'black')
# Mouth
t.goto(-65,138)
# Mouth Modification
t.right(5)
rectangle(40,5,'black')
# Hand Left
t.goto(-155,130)
rectangle(25,25,'green')
t.goto(-147,130)
rectangle(10,10,t.bgcolor())
# Hand Right
# Hand Left
t.goto(50,130)
rectangle(25,25,'green')
t.goto(58,130)
rectangle(10,10,t.bgcolor())
t.hideturtle()
time.sleep(10)