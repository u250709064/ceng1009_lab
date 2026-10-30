
#1

n=int(input("Enter a number:"))
sumTo=0
for i in range(1,n+1):
    sumTo+=i
print(sumTo)


#2
import turtle
def drawStar(t,n,size):
    angle=180 -180/n
    for i in range(n):
        t.forward(size)
        t.right(angle)
wn=turtle.Screen()
t=turtle.Turtle()
t.pensize(3)

drawStar(t,11,100)
wn.exitonlick()

#3

def sumTo(n):
    total=0
    for i in range(1,n+1):
        total+=i
    return total

n=int(input("Enter a number:"))
print(f"The sum is {sumTo(n)}")

#4
def mySqrt(x):
    guess= x/2
    for i in range(20):
        guess = (1 / 2) * (guess + x / guess)
    return guess
n=int(input("Enter a number:"))
print(mySqrt(n))

#5
import turtle
def drawSprite(someturtle, legs, length):
    angle=360/legs
    for i in range(legs):
        someturtle.forward(length)
        someturtle.backward(length)
        someturtle.left(angle)
def fancySquare(t,size):
    for corner in range(4):
        drawSprite(t,8,20)
        t.forward(size)
        t.left(90)
wn=turtle.Screen()
t=turtle.Turtle()
t.color("pink")
t.speed(6)
t.pensize(2)

fancySquare(t,100)
wn.exitonlick()


#6
def myFunc(n):
    if n>0:
        text="positive"
    elif n<0:
        text="negative"
    elif n==0:
        text="zero"
    else:
        text="not an integer"
    return text
n=int(input("Enter a number:"))
print(f"your number is {myFunc(n)}")


#7
import turtle
def drawBar(t,height,gap):
    t.penup()
    t.left(90)
    t.forward(height+gap)
    t.write(" " + str(height))
    t.backward(height + gap)
    t.right(90)
    t.pendown()

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
    t.fillcolor("red")
    t.pensize(3)

    for height in data:
        drawBar(t,height,gap)
    wn.exitonlick()

data= [48,117,200,240,160,260,220]
barChart(data)
















