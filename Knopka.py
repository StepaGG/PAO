from tkinter import *
from tkinter import ttk
import tkinter as tk
def printer(event):
    print('GOOOLL')
root=Tk()
root.title("GOYDA")
root.geometry("250x250")
but = Button(root)
but["text"] = "С ПАБЕДОЙ"
but.bind("<Button-1>",printer)
but.pack(expand=True)
root.mainloop()