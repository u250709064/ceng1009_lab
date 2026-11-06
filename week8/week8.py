"""
#1
def gradef(grade):
    if grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    elif grade >= 60:
        return "D"
    else:
        return "F"
grade=float(input("Enter your grade: "))
print(gradef(grade))

#2
import turtle
def chooseColor(height):
    if height >= 200:
        return "red"
    elif height >= 100:
        return "yellow"
    else:
        return "green"


def drawBar(t,height,gap):
    t.penup()
    t.left(90)
    t.forward(height+gap)
    t.write(" " + str(height))
    t.backward(height + gap)
    t.right(90)
    t.pendown()

    t.fillcolor(chooseColor(height))
    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()


def barChart(data):
    maxheight=max(data)
    num_bars=len(data)
    border=10

    gap= (maxheight - border)/25

    wn=turtle.Screen()
    wn.bgcolor("lightgreen")

    right = 40 * num_bars + border
    top = maxheight + 4 * border

    wn.setworldcoordinates(-border,-border,right,top)
    t = turtle.Turtle()
    t.color("blue")
    t.fillcolor()
    t.pensize(3)

    for height in data:
        drawBar(t,height,gap)
    wn.exitonlick()

data= [48,117,200,240,160,260,220]
barChart(data)


"""
#3

import turtle
def chooseColor(height):
    if height >= 200:
        return "red"
    elif height >= 100:
        return "yellow"
    else:
        return "green"


def drawBar(t,height,gap):
    if(height>=0):
        labelY= height + gap
    else:
        labelY= gap
    t.penup()
    t.left(90)
    t.forward(labelY)
    t.write(" " + str(height))
    t.backward(labelY)
    t.right(90)
    t.pendown()

    t.fillcolor(chooseColor(height))
    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()


def barChart(data):
    maxheight=max(data)
    minheight=min(data)
    num_bars=len(data)
    border=10

    gap= (maxheight + border)/25

    wn=turtle.Screen()
    wn.bgcolor("lightgreen")

    right = 40 * num_bars + border
    top = maxheight + 4 * border
    bottom=min(minheight, 0) - border

    wn.setworldcoordinates(-border,bottom,right,top)
    t = turtle.Turtle()
    t.color("blue")
    t.fillcolor()
    t.pensize(3)

    for height in data:
        drawBar(t,height,gap)
    wn.exitonlick()

data= [48,117,-60,240,160,-110,220]
barChart(data)




"""
#4
def findHypot():
    side1=float(input("Enter a side 1: "))
    side2=float(input("Enter a side 2: "))
    hypot=(side1**2 + side2**2)**0.5
    print(hypot)
findHypot()
"""