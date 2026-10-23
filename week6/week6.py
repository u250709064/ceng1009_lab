import turtle
wn = turtle.Screen()
wn.bgcolor("pink")
tess=turtle.Turtle()

#functions
def drawPoly(someturtle, somesides, somesize):
    angle=360/somesides
    for i in range(somesides):
        someturtle.forward(somesize)
        someturtle.left(angle)

def drawSpiral(someturtle, angle):
  size = 1
  for i in range(100):
      someturtle.forward(size)
      someturtle.right(angle)
      size +=2

def drawEquitriangle(someturtle,somesize):
    drawPoly(someturtle,3,somesize)

def drawStar(someturtle,size):
    for i in range(5):
        someturtle.forward(size)
        someturtle.left(144)

def drawSprite(someturtle,legs, length):
    angle =360/legs
    for i in range(legs):
        someturtle.forward(length)
        someturtle.backward(length)
        someturtle.left(angle)

#exercises
#1
#tess.pencolor("hotpink")
#drawPoly(tess,8,50)
#wn.exitonclick()

#2
#tess.pencolor("blue")
#for i in range(20):
#  drawPoly(tess, 4, 100)
#  tess.left(18)
#  wn.exitonclick()


 #3
#tess.pencolor("red")
#tess.penup()
#tess.goto(-150,0)
#tess.pendown()
#drawSpiral(tess, 90)

#tess.pencolor("red")
#tess.penup()
#tess.goto(150,0)
#tess.pendown()
#drawSpiral(tess, 89)

#4
#drawEquitriangle(tess,100)

#5
#for i in range(5):
#    drawStar(tess,50)
#    tess.penup()
#    tess.forward(350)
#    tess.right(144)
#    tess.pendown()


#6
drawSprite(tess,15,120)










































print("ağlama idil oynaaa")









