from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk


root=Tk()
root.title("Demonination Calculator")
root.configure(bg="light blue")
root.geometry("6500x400")


upload =Image.open("image.png")
upload = upload.resize((300,300))
image = ImageTk.PhotoImage(upload)

label = Label(root, image=image, bg="light blue")
label.place(x=180, y=20)

label1 = Label(root, text="Welcome to Demonination Calculator", font=("Arial", 24, "bold"), bg="light blue")

label1.place(relx=0.5, y=340, anchor=CENTER)


def msg():
    Msg = messagebox.askokcancel("Alert", "Do you want to use the  demonination calculator application?")
    if Msg == "ok":
        topwin()

button1 = Button(root, text="Click Here to Start", font=("Arial", 16, "bold"), bg="yellow", command=msg)