import turtle #importing library

my_wn=turtle.Screen()
my_wn.bgcolor("Lightblue")# screen background color
my_wn.title("Drawing Patterns")
my_pen=turtle.Turtle()
size=0
my_pen.speed(5)
my_pen.hideturtle()
my_pen.color;("Darkblue")
while True: #literate loop
    for i in range (4):
        my_pen.fd(size+1)
        my_pen.left(90)
        size=size-5
    size=size+1