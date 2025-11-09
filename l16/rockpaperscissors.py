import random


options={"rock", "paper", "scissors"}


userchoice=input("choose rock, paper or scissors: ")


computerchoice = random.choice(options)
print("You chose", userchoice)
print("The copputer chose", computerchoice)