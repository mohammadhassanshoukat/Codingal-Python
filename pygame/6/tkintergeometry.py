from tkinter import *
window=Tk()

frame1 = Frame(window, width=100, height=100, bg="red")
frame1.pack()
frame2 = Frame(window, width=100, height=100, bg="blue")
frame2.pack()
frame3 = Frame(window, width=100, height=100, bg="green")
frame3.pack()

window.mainloop()