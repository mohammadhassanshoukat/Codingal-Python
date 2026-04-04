#make sure you upload the image in the same folder as the visual stuio folder you are using
# import all the libraries that are needed for this project
# PIL stants for (python imaging library) provide image editing capabilities to the to the user
from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title('Image displayer')
root.geometry('500x500')


upload = Image.open('blue star.jpg')


image = ImageTk.PhotoImage(upload)


label = Label(root, image=image, height=400, width=400)
label.place(x=50, y=50)
label2 = Label(root, text='This how an image in tkinter will look like if uploaded to the program')
label2.place(x=40, y=360)

root.mainloop()