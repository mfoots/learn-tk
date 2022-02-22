import tkinter as tk

window = tk.Tk()

def display_result():
    txt = 'You typed: ' + user_input.get()
    result['text'] = txt

def reset_text():
    user_input.delete(0, tk.END)
    result['text'] = ''

user_input = tk.Entry(
    width=50,
    font=('Arial', 20)
    )
user_input.pack(padx=10, pady=10)

# user_input.insert(0, 'Tkinter is awesome!')

submit_button = tk.Button(
    text='Submit',
    font=('Times New Roman', 20),
    command=display_result
    )
submit_button.pack(padx=10, pady=10)

result = tk.Label(
    width=50,
    fg='red',
    text='',
    font=('Arial Narrow', 20)
)
result.pack(padx=10, pady=10)

clear_button = tk.Button(
    text='Clear',
    font=('Times New Roman', 20),
    command=reset_text
)
clear_button.pack(padx=10, pady=10)

window.mainloop()
