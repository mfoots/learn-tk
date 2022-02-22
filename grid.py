import tkinter as tk

window = tk.Tk()

font = ('Arial', 18)

# frames in a 2 x 2 grid
frameA = tk.Frame(window, width=200, height=200)
frameA.grid(row=1, column=1, ipadx=20, ipady=20)

frameB = tk.Frame(window, width=200, height=200)
frameB.grid(row=1, column=2, ipadx=20, ipady=20)

frameC = tk.Frame(window, width=200, height=200)
frameC.grid(row=2, column=1, ipadx=20, ipady=20)

frameD = tk.Frame(window, width=200, height=200)
frameD.grid(row=2, column=2, ipadx=20, ipady=20)

# other widgets packed in different frames

# in FrameA
check1_var = tk.IntVar()
check1 = tk.Checkbutton(frameA, font=font, text="Dine In", anchor='w', variable=check1_var)
check1.pack(anchor='w', pady=10, fill='both')

check2_var = tk.IntVar()
check2 = tk.Checkbutton(frameA, font=font, text="Drink Included", anchor='w', variable=check2_var)
check2.pack(anchor='w', pady=10, fill='both')

# in FrameB
choice = tk.IntVar()
for (index, item) in enumerate(['burger', 'pizza', 'chicken strips']):
    tk.Radiobutton(
        frameB,
        font=font,
        text=item,
        value=index,
        anchor='w',
        variable=choice
    ).pack(anchor='w', pady=10, fill='both')


# in FrameC
amount_label = tk.Label(frameC, text='$2.00', font=font)
amount_label.pack(pady=20, fill='both')


# in FrameD
button_submit = tk.Button(frameD, text='Submit', font=font)
button_submit.pack(pady=20, fill='both')


window.mainloop()