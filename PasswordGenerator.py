from tkinter import *
import string
import random
from tkinter import messagebox 



def generator():
    small_alphabets=string.ascii_lowercase
    capital_alphabets=string.ascii_uppercase
    numbers=string.digits
    special_charecters=string.punctuation

    all=small_alphabets+capital_alphabets+numbers+special_charecters
    password_length=int(length_Box.get())

    if choice.get()==1:
        entry2.insert(0,random.sample(small_alphabets,password_length))

    if choice.get()==2:
        entry2.insert(0,random.sample(small_alphabets+capital_alphabets,password_length))

    if choice.get()==3:
        entry2.insert(0,random.sample(all,password_length))

def clear():
    entry2.delete(0,END)
    entry1.delete(0,END)
    length_Box.delete(0,END)

def check_password():

        GLabel=entry2.get()
        ULabel=entry1.get()
        

        if(GLabel=="" and ULabel==""):
            messagebox.showinfo("","Blank Not Allowed")

        else:
            messagebox.showinfo("","Password is absolutely correct!!")


root=Tk()
choice=IntVar()

root.geometry("600x400")
root.title("Password Generator By Zeal Soni")
Font=('arial',13,'bold')



global entry1
global entry2

PLabel=Label(root,text='Password Generator', font=('Times New Roman', 20, 'bold', 'underline'), fg="blue")
PLabel.grid(padx=150,pady=0)

ULabel=Label(root,text="Enter user name:").place(x=120,y=50)
entry1=Entry(root,bd=5,font=Font)
entry1.place(x=250,y=50)

lengthLabel=Label(root,text='Enter password length:').place(x=120,y=100)
length_Box=Spinbox(root,from_=8,to_=18,bd=5,width=19,font=Font)
length_Box.grid(padx=250,pady=60)

GLabel=Label(root,text="Generated password:").place(x=120,y=150)
entry2=Entry(root,bd=5,font=Font)
entry2.place(x=250,y=150)

weakradioButton=Radiobutton(root,text='Weak',value=1,variable=choice,font=Font).place(x=200,y=200)

mediumradioButton=Radiobutton(root,text='Medium',value=2,variable=choice,font=Font).place(x=290,y=200)

strongradioButton=Radiobutton(root,text='Strong',value=3,variable=choice,font=Font).place(x=400,y=200)

generateButton=Button(root,text='Generate Password',font=Font,bg = "dark blue", fg = "white", command = generator)
generateButton.grid(pady=50)

acceptButton=Button(root,text='Accept',font=Font,bg = "white", fg = "blue",command = check_password).place(x=310,y=290)

resetButton=Button(root,text='Reset',font=Font,bg = "white", fg = "blue", command = clear).place(x=315,y=340)

root.mainloop()
