# Xade
import tkinter as tk
from tkinter import ttk
import re
import threading
import time


class Math_Screen(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.ans_insert = tk.StringVar()
        self.insert_num = tk.StringVar()
        self.Question_label = tk.StringVar()
        self.Question_label.set("Question # of 100")
        self.Time_label = tk.StringVar()
        self.time_left = 0

        # User entry, Submit button and Labels for layout

        self.UserInsert_entry = ttk.Entry(self, textvariable=self.ans_insert)
        self.submit_button = ttk.Button(self, text="Submit", command=self.submit_ans)
        self.clear_button = ttk.Button(self, text="Clear", command=self.clear_ans)
        Question_Label = ttk.Label(self, textvariable=self.Question_label,
                                font=("TkDefaultFont", 10), wraplength=600)

        Time_label = ttk.Label(self, textvariable=self.Time_label,
                                font=("TkDefaultFont", 10), wraplength=600)

        #Number buttons
        number_button0 = ttk.Button(self, text="0", command=self.insert_num_zero)
        number_button1 = ttk.Button(self, text="1", command=self.insert_num_one)
        number_button2 = ttk.Button(self, text="2", command=self.insert_num_two)
        number_button3 = ttk.Button(self, text="3", command=self.insert_num_three)
        number_button4 = ttk.Button(self, text="4", command=self.insert_num_four)
        number_button5 = ttk.Button(self, text="5", command=self.insert_num_five)
        number_button6 = ttk.Button(self, text="6", command=self.insert_num_six)
        number_button7 = ttk.Button(self, text="7", command=self.insert_num_seven)
        number_button8 = ttk.Button(self, text="8", command=self.insert_num_eight)
        number_button9 = ttk.Button(self, text="9", command=self.insert_num_nine)
        decimal_button0 = ttk.Button(self, text=".", command=self.insert_decimal)

        # Grid Layout
        self.UserInsert_entry.grid(row=5, column=2, sticky=(tk.E))
        self.submit_button.grid(row=5, column=3, sticky=tk.E)
        self.clear_button.grid(row=5, column=4, sticky=tk.E)
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


    # def update_answer_box(self):
    #     characters_entered = []

    def update_time(self, start_time):
        self.time_left = start_time
        for x in range(start_time, 0, -1):
            time.sleep(1)
            self.Time_label.set(f"Time Left: {x}")
            print(self.time_left)

    def submit_ans(self):
        if len(self.ans_insert.get()) > 0:
            if re.search('[a-zA-Z]', self.ans_insert.get()):
                print("Your answer is incomprehensible.")
            else:
                print(self.ans_insert.get())
        else:
            print("Your answer is blank.")

    def clear_ans(self):
        self.UserInsert_entry.delete(0, 'end')

    def insert_num_zero(self):
        #if self.insert_num.get():
        self.UserInsert_entry.insert('end', "0")

    def insert_num_one(self):
        #if self.ans_insert.get():
        self.UserInsert_entry.insert('end', "1")

    def insert_num_two(self):
        #if self.ans_insert.get():
        self.UserInsert_entry.insert('end', "2")

    def insert_num_three(self):
        #if self.ans_insert.get():
        self.UserInsert_entry.insert('end', "3")

    def insert_num_four(self):
        #if self.ans_insert.get():
        self.UserInsert_entry.insert('end', "4")

    def insert_num_five(self):
        #if self.ans_insert.get():
        self.UserInsert_entry.insert('end', "5")

    def insert_num_six(self):
        #if self.ans_insert.get():
        self.UserInsert_entry.insert('end', "6")

    def insert_num_seven(self):
        #if self.ans_insert.get():
        self.UserInsert_entry.insert('end', "7")

    def insert_num_eight(self):
        #if self.ans_insert.get():
        self.UserInsert_entry.insert('end', "8")

    def insert_num_nine(self):
        #if self.ans_insert.get():
        self.UserInsert_entry.insert('end', "9")

    def insert_decimal(self):
        #if self.ans_insert.get():
        self.UserInsert_entry.insert('end', '.')


class Math_Screen_Settings(tk.Tk):
    """Screen settings"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("600x500")
        self.resizable(width=False, height=False)
        self.math_screen = Math_Screen(self)

        #self.math_screen.grid(sticky=(tk.E + tk.W + tk.N + tk.S))
        #self.math_screen.update_time(10)

        self.t1 = threading.Thread(target=lambda : self.math_screen.grid(sticky=(tk.E + tk.W + tk.N + tk.S)), args=[])
        self.t2 = threading.Thread(target=lambda : self.math_screen.update_time(10), args=[])

        self.t1.start()
        self.t2.start()

        self.columnconfigure(0, weight=1)


if __name__ == '__main__':
    app = Math_Screen_Settings()
    app.mainloop()
