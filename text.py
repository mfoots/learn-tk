import tkinter as tk

window = tk.Tk()
window['background'] = 'black'
window.title('My Window')
window.geometry('600x800')

# def clear_text():
#     user_text.delete(1.0, tk.END)

user_text = tk.Text(
    font=('Arial', 12)
)
user_text.pack(padx=10, pady=10)

reset = tk.Button(
    text='Reset', 
    font=('Arial', 20),
    command=lambda : user_text.delete(1.0, tk.END)
)
reset.pack(padx=10, pady=10)

window.mainloop()


'''
Lambdas are short, anonymous functions

def fun_name(x):
    return x

lambda x: x
'''
