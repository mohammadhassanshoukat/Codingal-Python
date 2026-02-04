from tkinter import *


root = Tk()
root.geometry("400x400")
root.title("main")


def topwind():
    top = Toplevel()
    top.geometry("100x100")
    top.title("top")
    l2 = Label(top, text="This is top window")
    l2.pack()

l = Label(root, text="This is root window")
btn = Button(root, text="open top window", command=topwind)
l.pack()
btn.pack()

root.mainloop()
