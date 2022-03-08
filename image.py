from tkinter import *
from tkinter import ttk

window = Tk()
window.geometry('600x400')
window.title("Picture This!")
window.anchor(CENTER)

photo = PhotoImage(file="Atari-2600.png")

label = ttk.Label(window, image=photo)
label.grid()

mainloop()