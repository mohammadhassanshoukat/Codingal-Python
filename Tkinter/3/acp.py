#creating a rock paper scissors where player will play against the computer by using tkinter and PIL library to add images and buttons to the game
from tkinter import *
from PIL import Image, ImageTk
import random

#setting up the main window
root = Tk()
root.title('Rock Paper Scissors Game')
root.configure(bg='light blue')
root.geometry('600x400')
#adding images and labels in the main window
rock_img = Image.open('rock.png')
rock_img = rock_img.resize((100, 100))
rock_photo = ImageTk.PhotoImage(rock_img)
paper_img = Image.open('paper.png')
paper_img = paper_img.resize((100, 100))
paper_photo = ImageTk.PhotoImage(paper_img)
scissors_img = Image.open('scissors.png')
scissors_img = scissors_img.resize((100, 100))
scissors_photo = ImageTk.PhotoImage(scissors_img)
label = Label(root, text='Choose your move:', bg='light blue', font=('Arial', 14))
label.pack(pady=20)
result_label = Label(root, text='', bg='light blue', font=('Arial', 12))
result_label.pack(pady=20)
#function to play the game
def play(player_choice):
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)
    if player_choice == computer_choice:
        result = 'It\'s a tie!'
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        result = 'You win!'
    else:
        result = 'Computer wins!'
    result_label.config(text=f'You chose {player_choice}, computer chose {computer_choice}. {result}')
#adding buttons to the main window
button_rock = Button(root, image=rock_photo, command=lambda: play('rock'))
button_rock.pack(side=LEFT, padx=20)
button_paper = Button(root, image=paper_photo, command=lambda: play('paper'))
button_paper.pack(side=LEFT, padx=20)
button_scissors = Button(root, image=scissors_photo, command=lambda: play('scissors'))
button_scissors.pack(side=LEFT, padx=20)

root.mainloop()