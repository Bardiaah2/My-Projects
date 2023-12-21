import turtle as tr
from random import randint, choice
from math import sqrt
from threading import Thread


def mean(a: int | float, b: int | float):
    """
    the average of two numbers
    :param a: one of the numbers
    :param b:
    :return: average of the numbers
    """
    return (a + b) / 2


t1 = tr.Turtle()
t2 = tr.Turtle()
t3 = tr.Turtle()
tr.title("THE SIERPINSKI TRIANGLE")
t1.shape("circle")
t2.shape("circle")
t3.shape("circle")
# t1.hideturtle()
# Find the prefect pensize, dot size
t1.pensize(2)
t2.pensize(2)
t3.pensize(2)
t1.speed(0)
t2.speed(0)
t3.speed(0)


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


vertexA, vertexB, vertexC = triangle(t1, 600)

# Locate a point in the triangle
# Problem: the probability of coordination in the triangle are not the same
# Problem: we probably want dots on around the middle of the triangle?
# confirmed that there would be a single dot that can ruin the triangle
init_x = randint(int(vertexC[0]), int(vertexB[0]))
max_y = vertexA[1] + (vertexB[1] - vertexA[1]) / (vertexB[0]) * abs(init_x)
init_y = randint(int(vertexB[1]), int(max_y))

t1.pu()
t2.pu()
t3.pu()
t1.goto(init_x, init_y)
t2.goto(init_x, init_y)
t3.goto(init_x, init_y)

# Randomly choose a vertex1 and move the turtle there, stamp
# repeat

t1.shapesize(0.1)
t2.shapesize(0.1)
t3.shapesize(0.1)
# t1.stamp()
# thread1 = Thread(target=lambda: t1.goto(mean(t1.xcor(), vertex1[0]), mean(t1.ycor(), vertex1[1])))
# thread2 = Thread(target=lambda: t2.goto(mean(t2.xcor(), vertex2[0]), mean(t2.ycor(), vertex2[1])))
# thread3 = Thread(target=lambda: t3.goto(mean(t3.xcor(), vertex3[0]), mean(t3.ycor(), vertex3[1])))
for i in range(3000):
    vertex1 = choice((vertexA, vertexB, vertexC))
    vertex2 = choice((vertexA, vertexB, vertexC))
    vertex3 = choice((vertexA, vertexB, vertexC))

    t1.goto(mean(t1.xcor(), vertex1[0]), mean(t1.ycor(), vertex1[1]))
    t2.goto(mean(t2.xcor(), vertex2[0]), mean(t2.ycor(), vertex2[1]))
    t3.goto(mean(t3.xcor(), vertex3[0]), mean(t3.ycor(), vertex3[1]))
    t1.stamp()
    t2.stamp()
    t3.stamp()

print("finish")
# t1.stamp()
# t1.fd(50)

tr.mainloop()
