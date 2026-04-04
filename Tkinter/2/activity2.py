from tkinter import *
from tkinter import messagebox


root = Tk()
root.geometry('500x500')


def msg():
    messagebox.showinfo('alert', 'there is a virus')

button = Button(root, text='click me', command=msg)
button.place(x=200, y=200)

root.mainloop()