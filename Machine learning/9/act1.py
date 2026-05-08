# program to check if the user input number are equal without using any comparisson operator

def checkifsame (number1, number2):

    #user xor operator as a ^ a is always 0
    if number1 ^ number2 ==0:
        print ('The numbers are equal')
    else:
        print('Both numbers are not equal')

#taking input
number1 = int(input('Enter the first number: '))
number2 = int(input('Enter the second number: '))

checkifsame(number1, number2)