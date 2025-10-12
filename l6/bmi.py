height=float(input("Enter your height in : "))
weight=float(input("Enter your weight in kg: "))


BMI=weight/(height**2)
print("Your BMI is: ", BMI)

if BMI<18.5:
    print("You are underweight")
elif BMI<25:
    print("You have a normal weight")
elif BMI<30:
    print("You are slightly overweight")
elif BMI<35:
    print("You are obese")  
else:
    print("You are severly obese")