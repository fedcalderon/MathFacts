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
        self.clear_button = ttk.Button(self, text="Clear", command= lambda : self.UserInsert_entry.delete(0, 'end'))
        Question_Label = ttk.Label(self, textvariable=self.Question_label,
                                font=("TkDefaultFont", 10), wraplength=600)

        Time_label = ttk.Label(self, textvariable=self.Time_label,
                                font=("TkDefaultFont", 10), wraplength=600)

        #Number buttons
        number_button0 = ttk.Button(self, text="0", command=lambda: self.UserInsert_entry.insert('end', "0"))
        number_button1 = ttk.Button(self, text="1", command=lambda: self.UserInsert_entry.insert('end', "1"))
        number_button2 = ttk.Button(self, text="2", command=lambda: self.UserInsert_entry.insert('end', "2"))
        number_button3 = ttk.Button(self, text="3", command=lambda: self.UserInsert_entry.insert('end', "3"))
        number_button4 = ttk.Button(self, text="4", command=lambda: self.UserInsert_entry.insert('end', "4"))
        number_button5 = ttk.Button(self, text="5", command=lambda: self.UserInsert_entry.insert('end', "5"))
        number_button6 = ttk.Button(self, text="6", command=lambda: self.UserInsert_entry.insert('end', "6"))
        number_button7 = ttk.Button(self, text="7", command=lambda: self.UserInsert_entry.insert('end', "7"))
        number_button8 = ttk.Button(self, text="8", command=lambda: self.UserInsert_entry.insert('end', "8"))
        number_button9 = ttk.Button(self, text="9", command=lambda: self.UserInsert_entry.insert('end', "9"))
        decimal_button = ttk.Button(self, text=".", command=lambda: self.UserInsert_entry.insert('end', "."))

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
        decimal_button.grid(row=11, column=4, sticky=(tk.W))

    def update_time(self, start_time):
        self.time_left = start_time
        for x in range(start_time, -1, -1):
            self.time_left = x
            time.sleep(1)
            self.Time_label.set(f"Time Left: {self.time_left}")
            print(self.time_left)

    def submit_ans(self):
        if len(self.ans_insert.get()) > 0:
            if re.search('[a-zA-Z]', self.ans_insert.get()):
                print("Your answer is incomprehensible.")
            else:
                print(self.ans_insert.get())
        else:
            print("Your answer is blank.")


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
        self.protocol("WM_DELETE_WINDOW", self.close_down_app)

        self.columnconfigure(0, weight=1)

    def close_down_app(self):
        if self.math_screen.time_left > 0:
            print("The timer must stop before the app is closed. ")
        else:
            app.destroy()


if __name__ == '__main__':
    app = Math_Screen_Settings()
    app.mainloop()
