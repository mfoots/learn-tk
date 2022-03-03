from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Choose Wisely")
window.geometry("400x300")
window.anchor(CENTER)

color = StringVar()
color.set("#ffffff")

frame1 = ttk.Frame(window)
frame1.configure(
    borderwidth=4,
    relief="solid",
)
frame1.grid(
    padx=10,
    pady=10,
)

label = ttk.Label(frame1, text="Choose a Color")
label.grid(
    row=0,
    column=0,
    columnspan=3,
    pady=5,
)

radio_red = ttk.Radiobutton(frame1)
radio_red.configure(
    text="Red",
    value="#ff0000",
    variable=color,
)
radio_red.grid(
    row=1,
    column=0,
    padx=10,
)

radio_green = ttk.Radiobutton(frame1)
radio_green.configure(
    text="Green",
    value="#00ff00",
    variable=color,
)
radio_green.grid(
    row=1,
    column=1,
    padx=10,
)

radio_blue = ttk.Radiobutton(frame1)
radio_blue.configure(
    text="Blue",
    value="#0000ff",
    variable=color,
)
radio_blue.grid(
    row=1,
    column=2,
    padx=10,
)

def change_background():
    window.configure(
        bg=color.get()
    )

button1 = ttk.Button(frame1)
button1.configure(
    text="Submit",
    command=change_background,
)
button1.grid(
    row=3,
    column=0,
    columnspan=3,
    sticky=W+E,
)

# Part 2

size = IntVar()
typeface = IntVar()


frame2 = ttk.Frame(window)
frame2.configure(
    borderwidth=4,
    relief="solid",
)
frame2.grid(
    padx=10,
    pady=10,
)

label2 = ttk.Label(frame2, text="Other Choices")
label2.grid(
    row=0,
    column=0,
    columnspan=2,
    pady=5,
)

box1 = Checkbutton(frame2)
box1.configure(
    text="Large Font",
    font=("arial", 12),
    variable=size,
    onvalue=22,
    offvalue=12,
)
box1.grid(
    row=1,
    column=0,
    padx=5,
)
box2 = Checkbutton(frame2)
box2.configure(
    text="Monospace Font",
    font=("arial", 12),
    variable=typeface,
    onvalue=1,
    offvalue=0,
)
box2.grid(
    row=1,
    column=1,
    padx=5,
)

def change_font():
    font_name = ["arial", "courier"]
    box1.configure(
        font=(font_name[typeface.get()], size.get())
    )
    box2.configure(
        font=(font_name[typeface.get()], size.get())
    )

button2 = ttk.Button(frame2)
button2.configure(
    text="Submit",
    command=change_font,
)
button2.grid(
    row=3,
    column=0,
    columnspan=2,
    sticky=W+E,
)

mainloop()