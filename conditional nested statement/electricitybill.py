#take input of number of units consumed form the user
units=int(input("PLease enter number of units consumed: "))


#check condition of units consumed
#then calsulate amount and surcharge accordingly
if(units)<=50:
    amount=units*2.60
    tax=25

#check units lesstan 100
elif(units<=100):
    amount=130+(units-50)*3.25
    tax=35
    
#check units lessthan or equal 200
elif(units<=200):
    amount=130+162.50+(units-100)*5.26
    tax=45

#chheck for all cases othet than mentioned above
else:
    amount=130+162.50+526+(units-200)*8.45
    tax=55

#calculate total amount
#total amount and syrcharge
total_amount=amount+tax
print("Your total electricity bill is: ",total_amount)

