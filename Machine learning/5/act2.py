# program to find highest common facotor (HCF) or greatest divisor (GCD) of a number given by the input of the user

#enter two numbers from the user
number_largest = int(input('Enter the largest number: '))
number_smallest = int(input('Enter the smallest number: '))

#using eculiden algrothims

while(number_smallest):
    numberstore  = number_smallest
    number_smallest = number_largest % number_smallest
    number_largest = numberstore

print('The HCF of the given number is: ', number_largest)