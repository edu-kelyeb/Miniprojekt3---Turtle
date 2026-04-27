import turtle

t = turtle.Turtle()
t.speed(10)

for steg in range(5, 150, 5):
    t.forward(steg)
    t.left(90)

turtle.done()
