from tkinter import *
from tkinter import ttk
from turtle import bgcolor
# from PIL import ImageTk, Image



window = Tk()
window.geometry('600x400')
window.title("Picture This!")
window.anchor(CENTER)


# photo = ImageTk.PhotoImage(Image.open("Atari-2600.png"))
photo = PhotoImage(file="Atari-2600.png")

label = ttk.Label(window, image=photo)
label.grid()

mainloop()