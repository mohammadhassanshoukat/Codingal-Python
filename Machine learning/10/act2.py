#program ti check if a number is power of 4 

def power4(number):


    count  = 0

    #if only is set bit exists
    if (number & (~(number & (number -1)))):

        #count 0 bit before set bit
        while(number > 1):
            number >>= 1
            count += 1

        #if count is even true of false 
        if (count%2 ==0):
            return True 
        else:
            return False

            
number = int(input('Enter the number: '))
if power4(number):
    print(number, 'is a power of 4')
else:
    print(number, 'is not a power of 4')        
