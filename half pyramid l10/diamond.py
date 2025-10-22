#take input from the user
rowsize=int(input("please enter the number of rows: "))
if rowsize%2==0: #condition
    halfdimondrow=int(rowsize/2)
else:
    halfdiamondrow=int(rowsize/2)+1
space=halfdiamondrow-1
#loop for upper part
for i in range (1,halfdiamondrow+1): #loops for rows
    for  j in range (1,space+1): #loops for coloumns 
    print(end=" ")
space=space-1
num=1
    for j in range(2*i-1):
      print (end=str  (num))    
    #lincerementing number at each column 
      num=num+1
    print()
space=1
#loop for upper part
for i in range(1, halfDiamRow): #loop for rows
   for j in range(1, space+1): #loop for columns print(end="")
       print(end=" ")
    space=space+1
    num=1
   for j in range(1, 2*(halfDiamRow-i)):
         print(end=str(num)) # diaplay result
         #incrementing number at each column
         num=num+1
         print()