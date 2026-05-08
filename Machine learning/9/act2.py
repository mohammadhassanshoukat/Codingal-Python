#program to find the element not making a pair

#functions to calculate the number that is odd occuring 

def oddocuring (arr):
    
    #initialize result 
    res = 0
    
    #traverse the array
    for element in arr:
        #xor with the result 
        res = res ^ element 
        
    return res
    
#initialize our array
arr = []

#take the size as the input
n = int(input('ENter array size: '))

#take array element input 
while(n):
    num =int(input('Enter number: '))
    arr.append(num)
    n-=1
    
print('\n\nOdd occuring number is: ',oddocuring (arr))