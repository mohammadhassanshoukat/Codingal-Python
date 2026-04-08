from tkinter import *
from tkinter import Message
from tkinter import messagebox
from PIL import Image, ImageTk

#setting up the main window
root = Tk()
root.title('Demonitation Calculator')
root.configure(bg='light blue')
root.geometry('650x400')

#adding images and labels in the main window
upload = Image.open('upload.png')
#resize the image using resize() method
upload = upload.resize((300, 300))
image = ImageTk.PhotoImage(upload)
label = Label(root, image=image, bg='light blue')
label.place(x=180, y=20)


label1 = Label(root, text='Hey User welcome to ruppe demonitation calculator application', bg='light blue') 
label1.place(relx=0.5, y=340, anchor=CENTER)

#function t diplay a message box to proceed if ok is clicked
def msg():
    Msgbox = messagebox.showinfo('alert', 'do you want to calculate the demonitation?')
    if Msgbox == 'ok':
       topwin()


#adding butoons to the main window
button1 = Button(root, text='Lets get started!', command=msg, bg='brown', fg='white')
Button.place(x=260, y=360)


def topwin():
    #topw window
    top = Toplevel(root)
    top.title('Currency Demonitation Calculator')
    top.configure(bg='grey')
    top.geometry('600x400')


    #centering widgets in the top window
    label.place(x-230, y-50)
    entry.place(x-200, у-80)
    btn.place(x-240, y = 120 )
    lbl.place(x=140, y =170)


    l1.place(x=180, y=200)
    l2.place(x=180, y=230)
    l3.place(x=180, y=260)
    

    t1.place(x=270, y=200)
    t2.place(x=270, y=230)
    t3.place(x=270, y=260)
    
    top.mainloop()

root.mainloop()