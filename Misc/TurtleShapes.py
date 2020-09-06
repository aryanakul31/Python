import turtle as t
t.pendown()
# Square
for i in range(1,5):
    t.forward(200)
    t.right(90)

# Circle
t.penup()
t.goto(0,0)
t.pendown()
t.circle(20)
t.circle(200)

t.speed(100)
for i in range(1,150):
    t.circle(i)

for i in range(1,150):
    t.circle(i)
    t.left(90)

# Star
t.goto(150,-250)
t.speed(2)
for i in range(1,10):
    t.forward(150)
    t.left(135)