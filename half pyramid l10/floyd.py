#take input from the user
rows=int(input("Please enter the tottal amount of rows: "))
number=1 #intialize 1



print("floyd's triangle")
#outerloop for number of rows
for i in range (1,rows+1):
    #inner loop for number of columns
    for j in range (1, i+1):
        #display result
        print(number,end="     ")
        number=number+1
    print()