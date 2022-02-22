import tkinter as tk
import random

window = tk.Tk()
window.title('Making Choices')
window.geometry('300x200')

default_font=('Arial', 14)
colors = [
    ('Purple', '#eacfff'), 
    ('Green', '#b3ffc7'),
    ('Blue', '#b3efff')
]
radio_var = tk.IntVar()
check_var = tk.IntVar()

# add this last
radio_var.set(random.randrange(len(colors)))
bg_color = colors[radio_var.get()][1]

def switch_color():
    global bg_color
    bg_color = colors[radio_var.get()][1]

def toggle_bg():
    if check_var.get() == 1:
        window['bg'] = bg_color
        for child in window.children:
            window.children[child]['bg'] = bg_color
        check_button['text'] = 'Color on'
    else:
        window['bg'] = '#fff'
        for child in window.children:
            window.children[child]['bg'] = '#fff'
        check_button['text'] = 'Color off'

for (index, color) in enumerate(colors):
    tk.Radiobutton(
        text=color[0],
        font=default_font,
        value=index,
        variable=radio_var,
        command=switch_color
    ).pack()

check_button = tk.Checkbutton(
    text='Color off', 
    font=default_font,
    variable=check_var, 
    command=toggle_bg
)
check_button.pack(pady=10)

window.mainloop()
