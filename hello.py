from tkinter import *
from tkinter import ttk

window = Tk()
window.geometry("480x380")
window.title("Welcome to Tkinter")

greeting = ttk.Label(
    text='Hello, Tkinter!',
    foreground='white',
    background='black',
    font=("Arial", 40),
    padding=10
    )
'''
foreground is also fg and background is also bg
color names: red, green, blue, yellow, orange, purple
RGB and Hex codes '#34A2FE' may also be used
width and height in text units relative to size of the system font
'''
greeting.pack(pady=20)

window.mainloop()