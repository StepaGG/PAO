from tkinter import *
from tkinter import ttk
import tkinter as tk
MTG= {'Blood Artist': [50, 'Существо'], 'Yawgmoth': [2300, 'Существо'], 'Gravecravler': [100, 'Существо'], 'Swamp': [200, 'Земля'], 'Island': [444, 'Земля']}
def sale(event):
    global MTG
    for i in MTG:
        Card = MTG[i]
        price = Card[0]
        type = Card[1]
        if price >= 100:
            price -= 20
            MTG[i] = [price,type]
        else:
            price -= 5
            MTG[i] = [price,type]
        if type == 'Земля':
            price += 30
            MTG[i] = [price,type]
    print(MTG)
root=Tk()
root.title("GOYDA")
root.geometry("250x250")
but = Button(root)
but["text"] = "С ПАБЕДОЙ"
but.bind("<Button-1>",sale)
but.pack(expand=True)
root.mainloop()