import tkinter as tk

# root window    
root = tk.Tk()
root.geometry("400x400")
root.title("main")
l = tk.Label(root, text="This is root window")

# top window (created alongside root)
top = tk.Toplevel()
top.geometry("200x200")
top.title("top")
l1 = tk.Label(top, text="This is top windo3w")
l1.pack()

l.pack()

root.mainloop()