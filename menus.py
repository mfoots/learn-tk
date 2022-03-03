from tkinter import *
from tkinter import ttk

window = Tk()
# window.geometry("600x400")
window.title("Get Help")
window.option_add('*tear_off', False)
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

menubar = Menu(window)
window['menu'] = menubar

menu_file = Menu(menubar)
menubar.add_cascade(menu=menu_file, label="File")

menu_help = Menu(menubar)
menubar.add_cascade(menu=menu_help, label="Help")

def show_about():
    about_win = Toplevel(window)
    loc = f"{window.winfo_x() + 50}+{window.winfo_y() + 50}"
    about_win.geometry(f"200x100+{loc}")
    about_win.title("About")
    about_win.anchor(CENTER)

    ttk.Label(about_win, text="This is my app! ").grid(pady=10)
    ttk.Button(about_win, text="OK", command=about_win.destroy).grid()

menu_file.add_command(label="Close Program", command=quit)
menu_help.add_command(label="About This App", command=show_about)

content = Text(window, width=60, height=20)
content.configure(
    font=('monospace', 14),
)
content.grid(row=0, column=0, sticky=N+S+E+W)
content.focus_set()


scroll = ttk.Scrollbar(window, orient=VERTICAL, command=content.yview)
scroll.grid(row=0, column=1, sticky=N+S)

content['yscrollcommand'] = scroll.set

with open("sample-text.txt") as file:
    content.insert('1.0', file.read())

mainloop()