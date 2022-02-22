import tkinter as tk

SCREEN_FONT = ("Courier", 60)
BUTTON_FONT = ("Courier", 22)
BUTTON_WIDTH = 4
BUTTON_HEIGHT = 2


def convert(s):
    try:
        temp = int(s)
    except ValueError:
        try:
            temp = float(s)
        except ValueError:
            temp = s
    return temp


class Calculator:
    def __init__(self, root):
        root.title("PyCalc")
        self.root = root
        self.create_widgets()
        self.buffer = []
        self.operand1 = 0
        self.operand2 = 0
        self.operator = ''

    def create_widgets(self):
        self.screen = tk.Label(self.root, text="0",
                               font=SCREEN_FONT, bg="#ccc", anchor="e")
        self.screen.pack(fill=tk.BOTH, expand=True, ipady=5, ipadx=5)

        frame = tk.Frame(self.root, bg="#ccc")
        frame.pack(fill=tk.BOTH, expand=True)

        tk.Button(frame, text="AC", command=self.all_clear).grid(
            row=0, column=1)
        tk.Button(frame, text="C", command=self.clear).grid(row=0, column=2)
        tk.Button(frame, text="\u232B", command=self.delete_digit).grid(
            row=0, column=3)
        tk.Button(frame, text="\u00F7", command=lambda: self.choose_operation(
            'divide')).grid(row=0, column=4)

        tk.Button(frame, text="\u0037", command=lambda: self.enter_number(7)).grid(
            row=1, column=1)
        tk.Button(frame, text="\u0038", command=lambda: self.enter_number(8)).grid(
            row=1, column=2)
        tk.Button(frame, text="\u0039", command=lambda: self.enter_number(9)).grid(
            row=1, column=3)
        tk.Button(frame, text="\u00D7", command=lambda: self.choose_operation(
            'multiply')).grid(row=1, column=4)

        tk.Button(frame, text="\u0034", command=lambda: self.enter_number(4)).grid(
            row=2, column=1)
        tk.Button(frame, text="\u0035", command=lambda: self.enter_number(5)).grid(
            row=2, column=2)
        tk.Button(frame, text="\u0036", command=lambda: self.enter_number(6)).grid(
            row=2, column=3)
        tk.Button(frame, text="\u002D", command=lambda: self.choose_operation(
            'subtract')).grid(row=2, column=4)

        tk.Button(frame, text="\u0031", command=lambda: self.enter_number(1)).grid(
            row=3, column=1)
        tk.Button(frame, text="\u0032", command=lambda: self.enter_number(2)).grid(
            row=3, column=2)
        tk.Button(frame, text="\u0033", command=lambda: self.enter_number(3)).grid(
            row=3, column=3)
        tk.Button(frame, text="\u002B", command=lambda: self.choose_operation(
            'add')).grid(row=3, column=4)

        tk.Button(frame, text="\u00B1", command=self.flip_sign).grid(
            row=4, column=1)
        tk.Button(frame, text="\u0030", command=lambda: self.enter_number(0)).grid(
            row=4, column=2)
        tk.Button(frame, text="\u002E", command=lambda: self.enter_number(
            '.')).grid(row=4, column=3)
        tk.Button(frame, text="\u003D", command=self.calculate_result).grid(
            row=4, column=4)

        for child in frame.children.values():
            child.config(font=BUTTON_FONT, width=BUTTON_WIDTH,
                         height=BUTTON_HEIGHT, relief=tk.FLAT)

    def enter_number(self, number):
        self.buffer.append(str(number))
        self.update_screen()

    def update_screen(self, number=0):
        if self.buffer:
            number = ''.join(self.buffer)
        self.screen["text"] = number

    def choose_operation(self, operation):
        if self.buffer:
            self.operand1 = convert(''.join(self.buffer))
        else:
            if not isinstance(convert(self.screen["text"]), str):
                self.operand1 = convert(self.screen["text"])
            else:
                self.operand1 = 0
        self.operator = operation
        self.buffer = []

    def calculate_result(self):
        result = 0
        if self.buffer:
            self.operand2 = convert(''.join(self.buffer))
        else:
            self.operand2 = 0

        if self.operator == 'add':
            result = self.operand1 + self.operand2
        elif self.operator == 'subtract':
            result = self.operand1 - self.operand2
        elif self.operator == 'multiply':
            result = self.operand1 * self.operand2
        elif self.operator == 'divide':
            try:
                result = self.operand1 / self.operand2
            except:
                result = 'error'

        self.buffer = [str(result)]
        self.update_screen()
        self.buffer = []

    def delete_digit(self):
        if len(self.buffer) > 0:
            self.buffer.pop()
        self.update_screen()

    def all_clear(self):
        self.operand1 = 0
        self.operand2 = 0
        self.buffer = []
        self.operator = None
        self.screen["text"] = '0'

    def clear(self):
        self.buffer = []
        self.screen["text"] = '0'

    def flip_sign(self):
        if convert(''.join(self.buffer)) >= 0:
            self.buffer.insert(0, '-')
        else:
            self.buffer.remove('-')
        self.update_screen()


if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()