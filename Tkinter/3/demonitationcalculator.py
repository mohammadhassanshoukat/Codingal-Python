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


#adding buttons to the main window
button1 = Button(root, text='Lets get started!', command=msg, bg='brown', fg='white')
button1.place(x=260, y=360)


def topwin():
    # top window
    top = Toplevel(root)
    top.title('Currency Demonetization Calculator')
    top.configure(bg='grey')
    top.geometry('600x400')

    label_amount = Label(top, text='Enter amount in rupees:', bg='grey', fg='white', font=('Arial', 12, 'bold'))
    label_amount.place(x=60, y=40)

    amount_var = StringVar()
    entry_amount = Entry(top, textvariable=amount_var, width=20, font=('Arial', 12))
    entry_amount.place(x=260, y=40)

    result_label = Label(top, text='', bg='grey', fg='white', justify=LEFT, font=('Arial', 11))
    result_label.place(x=60, y=140)

    def calculate_denomination():
        try:
            amount = int(amount_var.get())
            if amount < 0:
                raise ValueError
        except ValueError:
            messagebox.showerror('Invalid input', 'Please enter a valid positive integer amount.')
            return

        denominations = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
        remaining = amount
        lines = []
        for denom in denominations:
            count, remaining = divmod(remaining, denom)
            lines.append(f'{denom} rupee: {count}')

        result_label.config(text='\n'.join(lines))

    calculate_button = Button(top, text='Calculate', command=calculate_denomination, bg='brown', fg='white')
    calculate_button.place(x=260, y=90)

    top.mainloop()

root.mainloop()