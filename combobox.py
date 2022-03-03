from tkinter import *
from tkinter import ttk

window = Tk()
window.geometry("600x400")
window.title("More Choices")
window.anchor(CENTER)


frame = ttk.Frame(window)
frame.grid()

label = ttk.Label(frame)
label.configure(
    text="Choose a character:",
    font=('Tahoma', 20),
    foreground="#6fcb9f",
)
label.grid(
    pady=10,
)

choice = StringVar()

def change_label(_):
    label['text'] = f"Character chosen: {choice.get()}"

character = ttk.Combobox(frame)
character.configure(
    textvariable=choice,
    values=['Joe', 'Cameron', 'Gordon', 'Donna', 'Boz'],
    font=('Tahome', 20),
)
character.bind('<<ComboboxSelected>>', change_label)
character.grid()

mainloop()