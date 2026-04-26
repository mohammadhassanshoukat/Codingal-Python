#program to check if a number is an prime number

from math import sqrt

num = int(input('Enter a number: '))
print('\n')

#check if a number greater than 1
if num > 1:

    #check if a numnber divisible  2
    for i in range (2, int(sqrt(num)+1)):
        
        #check if devisible by any number1
        if (num% i) == 0:
            print(num, ' it is not a prime number')

        else:
            print(num,'it is a prime number')

else:
    print(num,'it is not a prime number')