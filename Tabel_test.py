from tkinter import *
from main3 import *
name = lessonn_check()
root = Tk()

height = 5
width = 5
for i in range(height): #Rows
    for j in range(width): #Columns
        b = Label(root, text="---------------")
        a = Label(root, text=name, fg="red")
        b.grid(row=i, column=j)
        a.grid(row=1, column=1)

mainloop()
