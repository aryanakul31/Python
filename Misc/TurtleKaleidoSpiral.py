import turtle as t
import time 
from itertools import cycle

colors=cycle({'red','blue','green','purple','yellow','white','pink','brown','grey'})

def circle(size,angle,forw,shape):
    t.pencolor(next(colors))
    next_shape=''
    if shape=='circle':
        t.circle(size)
        next_shape='square'
    elif shape=='square':
        for i in range(4):
            t.forward(size+2)
            t.left(90)
        next_shape='circle'
    t.right(angle)
    t.forward(forw)
    circle(size+5,angle+1,forw+5,next_shape)

t.bgcolor('black')
t.speed('fast')
t.pensize(2)
circle(30,0,1,'circle')


t.hideturtle()
time.sleep(2)