from turtle import Turtle, Screen

# Creating Turtle and Screen
t: Turtle = Turtle()
s: Screen = Screen()

#sideLength: int = int (input('Give me a side length: '))
sideLength: int = s.numinput('Input Window', 'Give me a side length:')

# Draw square
t.forward(sideLength)
t.right(90)
t.forward(sideLength)
t.right(90)
t.forward(sideLength)
t.right(90)
t.forward(sideLength)
t.right(90)