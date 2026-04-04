from tkinter import *

root = Tk()
root.geometry('500x500')
root.title('My First GUI')


def topwindow():
    top = Toplevel()
    top.geometry('200x200')
    top.title('Top Window')
    Label(top, text='This is a top window').pack()

    top.mainloop()

l= Label(root, text='This is the main window')
btn  = Button(root, text='Open Top Window', command=topwindow)
l.pack()
btn.pack()