import tkinter as tk


def func():
    if button["state"] == tk.NORMAL:
        button.config(state=tk.DISABLED, bg="red")
    else:
        button.config(state=tk.NORMAL, bg="green")


root = tk.Tk()
button = tk.Button(text='Кнопощка', state=tk.DISABLED, font="Courier 20")
button.pack()
b = tk.Button(text="Активировать", command=func)
b.pack()
root.mainloop()