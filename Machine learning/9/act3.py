#program to find two nbumbers thta are odd occuring 

def odd(arr, size):
    
    #xor of two will hold xor of the 2 odd occuring numbers
    xorof2 =  [0]
    
    #these will hold 2 odd occuring numbers
    x = 0 
    y = 0
    
    #this wil hold the right msot set bot for xor of 2
    Set bit = 0
    
    for i in range (1,size):
        xorof2 =xorof2 ^ arr[i]
        
    setbit = xorof2 & ~(xorof2 - 1)
    
    #if number is having set bit at location we need then XOR it with x else y 
    for i in range (size):
        if(arr[i] & setbit):
            x = x ^ arr[i]
            
        else:
            y = y^ arr[i]
            
    print ('THe two Odd elements are', x, '&', y)
        
#create an empty array
arr = []


#take array size and elmets as input 
arr_size = int(input('Enter the size of array : '))
for i in range (0,arr_size):
    z = int(input('enter element: '))
    arr.append(z)
    
odd(arr, arr_size)