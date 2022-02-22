import tkinter as tk


window = tk.Tk()
window.geometry('600x200')
# window.wm_attributes('-alpha', 0.8)
# window.wm_attributes('-transparentcolor', 'red')

frameA = tk.Frame(window, bg='red', width=300)
frameA.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frameB = tk.Frame(window, bg='green', width=200)
frameB.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frameC = tk.Frame(window, bg='blue', width=100)
frameC.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)



label1 = tk.Label(
    frameA,
    text="I'm in frameA"
)
label1.place(relx=.5, rely=.5, anchor=tk.CENTER)

def set_label(opt):
    label1['text'] = 'You picked: ' + opt

option_list = ['option1', 'option2', 'option3', 'option4']
option = tk.StringVar()
options = tk.OptionMenu(frameA, option, *option_list, command=set_label)
option.set(option_list[0])
options.place(relx=.5, rely=.7, anchor=tk.CENTER)


img = tk.PhotoImage(file="Atari-2600.png")
label2 = tk.Label(
    frameB,
    text="I'm in frameB",
    image=img
)
label2.place(relx=.5, rely=.5, anchor=tk.CENTER)





label3 = tk.Label(
    frameC,
    text="I'm in frameC",
)
label3.place(relx=.5, rely=.5, anchor=tk.CENTER)

count = 0
def inc_count():
    global count
    count += 1
    label3['text'] = count

button1 = tk.Button(frameC, text="Click Me", command=inc_count)
button1.place(relx=.5, rely=.9, anchor=tk.CENTER)

window.mainloop()
