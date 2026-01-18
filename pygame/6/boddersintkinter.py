from tkinter import *


window=Tk()
window.title("Borders in Tkinter")
window.geometry("300x200")


bodders_effect = [FLAT, RAISED, SUNKEN, GROOVE, RIDGE, SOLID]


for r in bodders_effect:
    frame = Frame(window, borderwidth=5, relief=r)
    frame.pack(pady=5)
    label = Label(frame, text=f"Border style: {r}")
    label.pack(padx=10, pady=10)

window.mainloop()