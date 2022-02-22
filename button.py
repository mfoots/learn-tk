from tkinter import *
from tkinter import ttk

window = Tk()
window.geometry("480x380")
window.title("Push That Button")

messages = [
    'Ouch, stop that!',
    'Don\'t you have something better to do?',
    'You need another hobby.',
    'I\'m not impressed.'
]
msg_index = 0

def change_msg():
    global msg_index
    greeting['text'] = messages[msg_index]
    if msg_index < len(messages) - 1:
        msg_index += 1
    else: msg_index = 0

greeting = ttk.Label(
    text='Hello, Tkinter!',
    foreground='lime',
    background='black',
    font=('courier', 20),
    )
greeting.pack(fill=X)

button = ttk.Button(
    text='Click me!',
    command = change_msg,
)
button.pack()

window.mainloop()
