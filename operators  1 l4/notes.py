#taking total amount as input from user
amount=int(input ("Enter the total amount: "))


#calculating the number of notes different domintions
n1=amount//100
n2=amount%100//50
n3=amount%100%50//10


print("Number of 100 notes:",n1)
print("Number of 50 notes:",n2)
print("Number of 10 notes:",n3)