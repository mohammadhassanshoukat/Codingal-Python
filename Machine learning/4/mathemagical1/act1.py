#program to find  if a number is an armstrong number

#take input from the user
num  = int(input('enter a number:'))


#calculate number of digits
digits = len(str(num))

#find the sum of a^digits of each digit
temp = num
resultnumber = 0
while temp > 0:
    digit = temp % 10
    resultnumber += digit ** digits
    temp //= 10


#display the result
if num == resultnumber:
    print(num,' is an armstrong number')
else:
    print(num,' is not an armstrong number')

#if there is an alphabet instead of number in the input
try:
    num  = int(input('enter a number:'))
except ValueError:
    print('invalid input. please enter a valid number.')