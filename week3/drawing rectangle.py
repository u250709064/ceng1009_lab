import turtle
ok = turtle.Turtle()
ok.speed(1)

ok.forward(250)
ok.right(90)
ok.forward(250)
ok.right(90)
ok.forward(250)
ok.right(90)
ok.forward(250)
ok.right(45)
ok.forward(250)

for x in range(0,40):
    ok.forward(200)
    ok.right(175)

turtle.done()