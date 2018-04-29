import turtle
curs = turtle.Turtle()
def polygon(x):
    y = 360/x
    i = 0
    l = 1000
    while i < x:
        curs.left(y)
        curs.forward(l/x)
        i = i + 1
while True:
    sides = int(input("Enter 0 to exit or Enter the number of sides: "))
    curs.clear()
    if sides == 0:
        break
    else:
        polygon(sides)
        


