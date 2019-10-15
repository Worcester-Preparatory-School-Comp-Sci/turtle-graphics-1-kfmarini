import turtle
bob = turtle.Turtle()
import math
steve = turtle.Turtle()

def bobsquare():
	 bob.forward(30)
	 bob.right(90)
	 bob.forward(30)
	 bob.right(90)
	 bob.forward(30)
	 bob.right(90)
	 bob.forward(30)

angle = input('What angle would you like the hill to incline?')
angle = int(angle)

bob.right(180)
bob.forward(100)

rightturn= 180 - angle
rightturn=int(rightturn)
bob.right(rightturn)
hypotenuse = 100/math.cos(angle*math.pi/180)
bob.forward(hypotenuse)
bob.right(90+angle)
opposite=100*math.tan(angle*math.pi/180)
bob.forward(opposite)

bob.right(180)
bob.forward(opposite)
bob.right(270-angle)
bobsquare()

def bobsquare():
	 bob.forward(30)
	 bob.right(90)
	 bob.forward(30)
	 bob.right(90)
	 bob.forward(30)
	 bob.right(90)
	 bob.forward(30)
	 
bob.right(90)
bob.forward(15)
bob.right(90)
bob.penup()
bob.forward(15)
bob.pendown()
bob.right(360)
bob.forward(40)
bob.penup()
bob.right(360)
bob.forward(25)
bob.pendown()
bob.right(angle)
bob.forward(40)




turtle.done()
