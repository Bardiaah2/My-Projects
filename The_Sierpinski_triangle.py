# The Sierpinski triangle
# Author: Bardia Ahmadi
# Partner: Got the idea from someone in instagram
# Description: draws a Sierpinski triangle in Turtle with "random" dots
import turtle as tr
from random import randint, choice
from math import sqrt


def mean(a, b):
    return (a + b) / 2


t = tr.Turtle()
tr.title("THE SIERPINSKI TRIANGLE")
t.shape("circle")
# t.hideturtle()

# Find the prefect pensize, dot size
t.pensize(2)
t.shapesize(0.2)


# Draw a triangle and record the vertexes
def triangle(turtle: tr, a: int):
    h = sqrt(3) / 3 * a

    # pu, goto √3/3 a up, pd
    turtle.pu()
    vertex0 = (0, h)
    turtle.goto(0, h)
    turtle.pd()

    # rt 60, fd a
    turtle.rt(60)
    turtle.fd(a)
    vertex1 = (turtle.xcor(), turtle.ycor())

    # rt 120, fd a
    turtle.rt(120)
    turtle.fd(a)
    vertex2 = (turtle.xcor(), turtle.ycor())

    # rt 120, fd a
    turtle.rt(120)
    turtle.fd(a)

    # pu, goto √3/3 a down, pd
    turtle.pu()
    turtle.goto(0, 0)
    turtle.pd()
    turtle.setheading(0)
    return vertex0, vertex1, vertex2


vertex0, vertex1, vertex2 = triangle(t, 600)


# Locate a point in the triangle
# Problem: the probability of coordination in the triangle are not the same
# Problem: we probably want dots on around the middle of the triangle?
init_x = randint(int(vertex2[0]), int(vertex1[0]))
max_y = vertex0[1] + (vertex1[1] - vertex0[1]) / (vertex1[0]) * abs(init_x)
init_y = randint(int(vertex1[1]), int(max_y))

t.pu()
t.goto(init_x, init_y)


# Randomly choose a vertex and move the turtle there, stamp
# repeat
t.speed(0)
t.shapesize(0.1)
t.stamp()
for i in range(10000):
    vertex = choice((vertex0, vertex1, vertex2))
    t.goto(mean(t.xcor(), vertex[0]), mean(t.ycor(), vertex[1]))
    t.stamp()

print("finish")
tr.mainloop()
