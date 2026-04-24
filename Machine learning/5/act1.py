#take  input from the user
num = int((input('ENter a number of which you want rto see if it is a planmindore number')))

#store the orignal number for comparision later
orignum = num
revernum = 0

#reverse the number
while num >0:
    digit = num % 10
    revernum  = revernum * 10 + digit
    num //= 10


# check if the orignal number and the reversed number are smae
if orignum == revernum:
    print(orignum, 'is a palindrome number')
else:
    print(orignum, 'is not a palindrome number')