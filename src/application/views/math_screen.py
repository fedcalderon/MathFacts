# Xade
import tkinter as tk
from tkinter import ttk


class Math_Screen(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.ans_insert = tk.StringVar()
        self.insert_num = tk.StringVar()

        UserInsert_entry = ttk.Entry(self, textvariable=self.ans_insert)
        submit_button = ttk.Button(self, text="Submit", command=self.submit_ans())
        number_button0 = ttk.Button(self, text="0", command=self.insert_num())
        number_button1 = ttk.Button(self, text="1", command=self.insert_num())
        number_button2 = ttk.Button(self, text="2", command=self.insert_num())
        number_button3 = ttk.Button(self, text="3", command=self.insert_num())
        number_button4 = ttk.Button(self, text="4", command=self.insert_num())
        number_button5 = ttk.Button(self, text="5", command=self.insert_num())
        number_button6 = ttk.Button(self, text="6", command=self.insert_num())
        number_button7 = ttk.Button(self, text="7", command=self.insert_num())
        number_button8 = ttk.Button(self, text="8", command=self.insert_num())
        number_button9 = ttk.Button(self, text="9", command=self.insert_num())
        decimal_button0 = ttk.Button(self, text=".", command=self.insert_num())

        # Grid Layout

        UserInsert_entry.grid(row=5, column=3, sticky=(tk.W + tk.E))
        submit_button.grid(row=5, column=5, sticky=tk.E)
        self.columnconfigure(1, weight=1)

        # number button grid
        number_button0.grid(row=11, column=3, sticky=(tk.W))
        number_button1.grid(row=10, column=3, sticky=(tk.W))
        number_button2.grid(row=10, column=4, sticky=(tk.W + tk.E))
        number_button3.grid(row=10, column=5, sticky=(tk.E))
        number_button4.grid(row=9, column=3, sticky=(tk.W))
        number_button5.grid(row=9, column=4, sticky=(tk.W + tk.E))
        number_button6.grid(row=9, column=5, sticky=(tk.E))
        number_button7.grid(row=8, column=3, sticky=(tk.W))
        number_button8.grid(row=8, column=4, sticky=(tk.W + tk.E))
        number_button9.grid(row=8, column=5, sticky=(tk.E))
        decimal_button0.grid(row=11, column=5, sticky=(tk.E))

    def submit_ans(self):
        if self.ans_insert.get():
            print("Answer submitted")

    def insert_num(self):
        if self.insert_num.get():
            print("Number get")


class Math_Screen_Settings(tk.Tk):
    """Screen settings"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("700x600")
        self.resizable(width=False, height=False)
        Math_Screen(self).grid(sticky=(tk.E + tk.W + tk.N + tk.S))
        self.columnconfigure(0, weight=1)


if __name__ == '__main__':
    app = Math_Screen_Settings()
    app.mainloop()
