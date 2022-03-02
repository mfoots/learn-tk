from tkinter import *
from tkinter import ttk
from tkinter import font
from turtle import color


window = Tk()
window.geometry("480x380")
window.title("Welcome to Tkinter")

myfont = font.Font(
    family='impact',
    size=40,
)

greeting = ttk.Label(
    text='Hello, Tkinter!',
    padding=20,
    font=myfont,
    foreground='lime'
    )
'''
foreground is also fg and background is also bg
color names: red, green, blue, yellow, orange, purple
RGB and Hex codes '#34A2FE' may also be used
width and height in text units relative to size of the system font
'''
greeting.grid(pady=20, sticky=E+W)

window.mainloop()