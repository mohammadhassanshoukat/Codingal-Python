import turtle #importing library
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300,400)
polygon=turtle.Turtle()#defined variable
num_sides=4 #variable for how may sides
side_length=70 
angle=360/num_sides
#litererate loop for total number of sides
for i in range (num_sides):
    polygon.forward(side_length) 
    polygon.right(angle) 

turtle.done()