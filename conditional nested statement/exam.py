#take the input for the student that he attend the exam
medical=input("Did you have any mediacal problem? yes or no: ")
#take the input of the attendance
attendance=int(input("Enter your attendance percentage: "))



#checking the user input predecting accordingaly
if medical=="yes":
    print("You are allowed to sit in the exam")
else:
    if attendance>=75:
        print("You are allowed to sit in the exam")
    else:
        print("You are not allowed to sit in the exam") 