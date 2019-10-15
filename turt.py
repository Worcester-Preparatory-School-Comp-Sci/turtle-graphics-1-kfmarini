#Kathryn Marini 10/11/19
import turtle
bob = turtle.Turtle()
import math
steve = turtle.Turtle()

#This function draws the square on the hill. 
def bobsquare():
	 bob.forward(30)
	 bob.right(90)
	 bob.forward(30)
	 bob.right(90)
	 bob.forward(30)
	 bob.right(90)
	 bob.forward(30)

#User input for angle and mass and calculating gravity and normal force. 
angle = input('What angle does the hill incline in degrees?')
angle = int(angle)
mass = input('What is the mass of the box in kg?')
mass = int(mass)
mg = mass*9.8
normal = mg*math.cos(math.radians(angle))

#Moving Bob to the bottom left corner of the triangle to make the incline of the hill. 
bob.right(180)
bob.forward(100)

#Bob creates the incline and draws the hypotenuse and opposite side of the triangle. 
rightturn= 180 - angle
rightturn=int(rightturn)
bob.right(rightturn)
hypotenuse = 100/math.cos(math.radians(angle))
bob.forward(hypotenuse)
bob.right(90+angle)
opposite=100*math.tan(math.radians(angle))
bob.forward(opposite)

#Bob is moved to the top of the hill and draws the square there. 
bob.right(180)
bob.forward(opposite)
bob.right(270-angle)
bobsquare()

#Bob creates the normal force vector. 
bob.right(90)
bob.forward(15)
bob.right(90)
bob.penup()
bob.forward(15)
bob.pendown()
bob.color('violet')
bob.right(360)
bob.forward(normal)
bob.write(normal)

#Bob creates the gravity vector. 
bob.penup()
bob.right(180)
bob.forward(normal)
bob.pendown()
bob.color('cyan')
bob.right(angle)
bob.forward(mg)
bob.write(mg)

#Bye Steve!
steve.hideturtle()

#Good job, Bob! <3
turtle.done()
