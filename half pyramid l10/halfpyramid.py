#take input
print("half pyramid pattern of stars (*):")
n=int(input("enter the amount of rows: "))
#outer loop to handle the number of loops
for i in range(n):
    #inner loop to handle the number of comlumns
    for j in range (i+1):
        #diplay result
        print("*",end="")
    print()