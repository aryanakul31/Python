import turtle as t
import random as rd
import time as ti

def inside_window():
    left_limit=-(t.window_width()/2)+100
    right_limit=(t.window_width()/2)-100
    top_limit=t.window_height()/2-100
    bottom_limit=(-t.window_height()/2)+100
    (x,y)=t.pos()
    inside=left_limit<x<right_limit and bottom_limit<y<top_limit
    return inside

def move_turle():
    if inside_window():
        angle=rd.randint(0,180)
        dist=rd.randint(50,300)
        t.right(angle)
        t.forward(dist)
    else:
        t.backward(200)


t.shape('turtle')
t.fillcolor('green')
t.bgcolor('black')
t.speed(1)
while True:
    move_turle()
ti.sleep(3)