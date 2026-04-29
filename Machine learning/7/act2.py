#program to check if the user entered  number is odd or even using only bitwise operator
#retrun true if n is even, else odd
def isEvenOdd(n):
    # XOR with 1 equals n+1
    if n^1 == n + 1:
        return True
    else:
        return False
    
num = int(input('Enter a number: '))

if  isEvenOdd(num):
    print(num, 'is an even number')
else:
    print(num, 'is an odd number')