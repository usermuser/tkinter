from tkinter import *

root = Tk()

def callback():
    print("click!")

b = Button(root, text="OK", command=callback)
b.pack()

mainloop()
