from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os

# Globals

filepath = None

window = Tk()
# window.geometry("600x400")
window.title("Get Help")
window.option_add('*tear_off', False)
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

menubar = Menu(window)
window['menu'] = menubar

# Menubar Menus
menu_file = Menu(menubar)
menubar.add_cascade(menu=menu_file, label="File")
menu_help = Menu(menubar)
menubar.add_cascade(menu=menu_help, label="Help")


# File Menu Functions

def update_title():
    filename = filepath.split('/')[-1]
    window.title(filename)

def new_file():
    global filepath
    content.delete('1.0', 'end')
    filepath = None
    window.title('Untitled.txt')

def open_file():
    global filepath
    filepath = filedialog.askopenfilename(
        initialdir=os.getcwd(),
        filetypes=(('Text files', '*.txt'),)
    )
    try:
        with open(filepath) as file:
            content.insert('1.0', file.read())
        update_title()
    except:
        pass

def save_file():
    global filepath
    if filepath == None:
        filepath = filedialog.asksaveasfilename(
            initialdir=os.getcwd(),
            filetypes=(('Text files', '*.txt'),)
        )
    try:
        with open(filepath, 'w') as file:
            file.write(content.get('1.0', 'end'))
        update_title()
    except:
        pass


# File Menu Commands

menu_file.add_command(label="New", command=new_file)
menu_file.add_command(label="Open", command=open_file)
menu_file.add_command(label="Save", command=save_file)
menu_file.add_command(label="Quit", command=quit)


# Help Menu Commands

def show_about():
    about_win = Toplevel(window)
    loc = f"{window.winfo_x() + 50}+{window.winfo_y() + 50}"
    about_win.geometry(f"200x100+{loc}")
    about_win.title("About")
    about_win.anchor(CENTER)

    ttk.Label(about_win, text="This is my app! ").grid(pady=10)
    ttk.Button(about_win, text="OK", command=about_win.destroy).grid()

menu_help.add_command(label="About This App", command=show_about)


# Text Widget Code

content = Text(window, width=60, height=15)
content.configure(
    font=('monospace', 10),
)
content.grid(row=0, column=0, sticky=N+S+E+W)
content.focus_set()


scroll = ttk.Scrollbar(window, orient=VERTICAL, command=content.yview)
scroll.grid(row=0, column=1, sticky=N+S)

content['yscrollcommand'] = scroll.set



mainloop()