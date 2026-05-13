# program to find if a number is a power of 2 

def power2(number):

     #as the power of 2  will only have 1 set bit , then n-1 & n will always be zero for any power of 2

     if (number==0):
          return 0

     if ((number & (~(number - 1))) == number):
        return 1

     return 0

number =int(input('Enter the number: '))

if (power2(number)):
    print ('\nThe number is a power of 2')
else:
    print ('\nThe number is not a power of 2')