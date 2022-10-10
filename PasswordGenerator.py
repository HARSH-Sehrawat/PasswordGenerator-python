from tkinter import*
import pyperclip
import random

tk = Tk()
tk.geometry('400x400')

passstr =StringVar()
passlen =IntVar()
passlen.set(0)

def genertae():
    pass1 =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
            'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
            'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
            'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8',
            '9', '0', ' ', '!', '@', '#', '$', '%','^', '&','*','(', ')']
    password =''
    for x in range(passlen.get()):
        password += random.choice(pass1)
    
    passstr.set(password)
    
def CopytoClipboard():
    random_password = passstr.get()
    pyperclip.copy(random_password)
    
Label(tk,text='Password Generator Application', font='calibri 20 bold').pack()
Label(tk,text='Enter password length.').pack(pady=3)
Entry(tk,textvariable=passlen).pack(pady=3)
Button(tk,text='Genterate Password',command=genertae).pack(pady=7)
Entry(tk,textvariable=passstr).pack(pady=3)
Button(tk,text='Copy to clipboard',command=CopytoClipboard).pack()

tk.mainloop()

