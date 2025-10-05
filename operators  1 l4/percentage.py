#take  as input from user
print("Enter the percentage:")
maths=int(input("maths:"))
english=int(input("English:"))
science=int(input("science"))
IT=int(input("IT:"))

#calculating the total percentage of marks
sum=maths+english+science+IT
percentage=(sum/400)*100
print("Percentage of marks:",percentage)