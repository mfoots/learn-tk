import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os

window = tk.Tk()


path = ''
filename = 'Untitled'
window.title(filename)
changes_made = 0
content = tk.StringVar()
content.set('')

def save_warning():
    answer = messagebox.askyesno(
        title='Save Changes',
        message='You have unsaved changes. Do you want to save these changes?'
    )
    if answer == True:
        save_file()

def new_file(*args):
    global filename, path
    if changes_made == 1:
        save_warning()
    text.delete(0.0, tk.END)
    filename = 'Untitled'
    path = ''
    window.title(filename)

def update(*args):
    global changes_made
    if content.get() != text.get(0.0, tk.END):
        content.set(text.get(0.0, tk.END))
        changes_made = 1
        window.title(filename + '*')

def exit_program(*args):
    if changes_made == 1:
        save_warning()
    window.quit()

def open_file(*args):
    global path, filename
    try:
        filein = filedialog.askopenfile(mode='r')
        text.insert(0.0, filein.read())
        path, filename = os.path.split(filein.name)
        window.title(filename)
    except Exception as e:
        print(e)    

def save_file(*args):
    global path, filename, changes_made
    try:
        if path != '':
            fileout = open(os.path.join(path, filename), mode='w')
        else:
            fileout = filedialog.asksaveasfile(mode='w')
            
        path, filename = os.path.split(fileout.name)
        fileout.write(text.get(0.0, tk.END))
        window.title(filename)
        changes_made = 0
    except Exception as e:
        print(e)

def save_as_file(*args):
    global path, filename, changes_made
    try:
        fileout = filedialog.asksaveasfile(mode='w') 
        path, filename = os.path.split(fileout.name)
        fileout.write(text.get(0.0, tk.END))
        window.title(filename)
        changes_made = 0
    except Exception as e:
        print(e)

def display_about():
    content = 'Code written by MRF\nCopyright 2021'
    about = tk.Toplevel(window)
    about.title('About this program')
    label = tk.Label(about, text=content)
    label.pack(padx=10, pady=10)
    button = tk.Button(about, text="OK", command=about.destroy)
    button.pack(padx=10, pady=10)

menubar = tk.Menu(window)

filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label='New \tCtrl+N', command=new_file)
filemenu.add_command(label='Open \tCtrl+O', command=open_file)
filemenu.add_command(label='Save \tCtrl+S', command=save_file)
filemenu.add_command(label='Save As \tShift+Ctrl+S', command=save_as_file)
filemenu.add_separator()
filemenu.add_command(label='Exit  \tCtrl+Q', command=exit_program)
menubar.add_cascade(label='File', menu=filemenu)

helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label='About', command= display_about)
menubar.add_cascade(label='Help', menu=helpmenu)

window['menu'] = menubar

text = tk.Text(window, font=('courier', 20))
text.pack()


window.bind('<Control-n>', new_file)
window.bind('<Control-o>', open_file)
window.bind('<Control-s>', save_file)
window.bind('<Shift-Control-S>', save_as_file)
window.bind('<Control-q>', exit_program)
text.bind('<KeyRelease>', update)


window.mainloop()
