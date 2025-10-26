def add (P, Q):
   #This function is used for adding two numbers return P+Q
 def subtract (P, Q):
    # This function is used for subtracting two numbers return PQ
  def multiply(P, Q):
    # This function is used for multiplying two numbers return P Q
   def divide(P, Q):
     # This function is used for dividing two numbers
     return P/Q


#Now we will take inputs from the user
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

choice=input("Enter choice(1/2/3/4):")

num_1=int(input("Enter first number: "))
num_2=int(input("Enter second number: "))

if choice=='1':
     print(num_1,"+",num_2,"=", add(num_1,num_2))

    elif choice =='2':
        print(num_1,"-",num_2,"=", subtract(num_1,num_2))
    elif choice=='3' :
        print(num_1,"*",num_2,"=", multiply(num_1,num_2))
    elif choice=='4':   
        print(num_1,"/",num_2,"=", divide(num_1,num_2))
    else:
        print("Invalid input")