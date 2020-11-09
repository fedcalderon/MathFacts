# Xade
import tkinter as tk
from tkinter import ttk


class Math_Screen(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.ans_insert = tk.StringVar()
        self.insert_num = tk.StringVar()
        self.Question_label = tk.StringVar()
        self.Question_label.set("Question # of 100")
        self.Time_label = tk.StringVar()
        self.Time_label.set("Time Left: #")

        # User entry, Submit button and Labels for layout

        UserInsert_entry = ttk.Entry(self, textvariable=self.ans_insert)
        submit_button = ttk.Button(self, text="Submit", command=self.submit_ans())
        Question_Label = ttk.Label(self, textvariable=self.Question_label,
                                font=("TkDefaultFont", 10), wraplength=600)
        Time_label = ttk.Label(self, textvariable=self.Time_label,
                                font=("TkDefaultFont", 10), wraplength=600)

        #Number buttons
        number_button0 = ttk.Button(self, text="0", command=self.insert_num_zero())
        number_button1 = ttk.Button(self, text="1", command=self.insert_num_one())
        number_button2 = ttk.Button(self, text="2", command=self.insert_num_two())
        number_button3 = ttk.Button(self, text="3", command=self.insert_num_three())
        number_button4 = ttk.Button(self, text="4", command=self.insert_num_four())
        number_button5 = ttk.Button(self, text="5", command=self.insert_num_five())
        number_button6 = ttk.Button(self, text="6", command=self.insert_num_six())
        number_button7 = ttk.Button(self, text="7", command=self.insert_num_seven())
        number_button8 = ttk.Button(self, text="8", command=self.insert_num_eight())
        number_button9 = ttk.Button(self, text="9", command=self.insert_num_nine())
        decimal_button0 = ttk.Button(self, text=".", command=self.insert_decimal())

        # Grid Layout

        UserInsert_entry.grid(row=5, column=2, sticky=(tk.E))
        submit_button.grid(row=5, column=4, sticky=tk.E)
        Question_Label.grid(row=0, column=0, sticky=tk.E)
        Time_label.grid(row=0, column=12, sticky=tk.E)
        self.columnconfigure(1, weight=1)

        # number button grid
        number_button0.grid(row=11, column=2, sticky=(tk.E))
        number_button1.grid(row=10, column=2, sticky=(tk.E))
        number_button2.grid(row=10, column=3, sticky=(tk.E))
        number_button3.grid(row=10, column=4, sticky=(tk.W))
        number_button4.grid(row=9, column=2, sticky=(tk.E))
        number_button5.grid(row=9, column=3, sticky=(tk.E))
        number_button6.grid(row=9, column=4, sticky=(tk.W))
        number_button7.grid(row=8, column=2, sticky=(tk.E))
        number_button8.grid(row=8, column=3, sticky=(tk.E))
        number_button9.grid(row=8, column=4, sticky=(tk.W))
        decimal_button0.grid(row=11, column=4, sticky=(tk.W))

    def submit_ans(self):
        if self.ans_insert.get():
            print("Answer submitted")

    def insert_num_zero(self):
        if self.insert_num.get():
            print("Number get")

    def insert_num_one(self):
        if self.ans_insert.get():
            print("Answer submitted")

    def insert_num_two(self):
        if self.ans_insert.get():
            print("Answer submitted")

    def insert_num_three(self):
        if self.ans_insert.get():
            print("Answer submitted")

    def insert_num_four(self):
        if self.ans_insert.get():
            print("Answer submitted")

    def insert_num_five(self):
        if self.ans_insert.get():
            print("Answer submitted")
    def insert_num_six(self):
        if self.ans_insert.get():
            print("Answer submitted")
    def insert_num_seven(self):
        if self.ans_insert.get():
            print("Answer submitted")

    def insert_num_eight(self):
        if self.ans_insert.get():
            print("Answer submitted")

    def insert_num_nine(self):
        if self.ans_insert.get():
            print("Answer submitted")

    def insert_decimal(self):
        if self.ans_insert.get():
            print("Answer submitted")

class Math_Screen_Settings(tk.Tk):
    """Screen settings"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("600x500")
        self.resizable(width=False, height=False)
        Math_Screen(self).grid(sticky=(tk.E + tk.W + tk.N + tk.S))
        self.columnconfigure(0, weight=1)


if __name__ == '__main__':
    app = Math_Screen_Settings()
    app.mainloop()
