import random # Importing module

playing=True #initialize
number=str(random.randint(10,20)) #random built in function


print("I will generate a number from 10 to 20, and you have to guess the number one digit a time") 
print("The game ends when you get 1 hero!")
#literate loop till condition is true
while playing:
    guess=input("Give me ypur best guess \n")
    if guess == number:
        print("You win the the game and you got 1 hero!")
        print ("The number was",number)
        break
    else:
        print("Your guess isn't quiet right please try agian \n")