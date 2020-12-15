# Xade
import tkinter as tk
from tkinter import ttk
import re
import threading
import time
import random
import math


class Questions:
    def __init__(self, ID):
        self.ID = ID

    def toggle_topics(self):
        # Addition
        if self.ID == '1-ADD':
            return self.one_digit_addition()

        elif self.ID == '2-ADD':
            return self.two_digit_addition()

        elif self.ID == '3-ADD':
            return self.multi_digit_addition()

        # Subtraction
        elif self.ID == '1-SUB':
            return self.one_digit_subtraction()

        elif self.ID == '2-SUB':
            return self.one_digit_subtraction()

        elif self.ID == '3_SUB':
            return self.multi_digit_subtraction()

        # Multiplication
        elif self.ID == '1-MUL':
            return self.one_digit_multiplication()

        elif self.ID == '2-MUL':
            return self.two_digit_multiplication()

        # Division
        elif self.ID == '1-DIV':
            return self.one_digit_division()

        elif self.ID == '2-DIV':
            return self.two_digit_division()

    def one_digit_addition(self):
        #return [self.first_number, self.second_number]
        self.first_number = random.randint(0, 10)
        self.second_number = random.randint(0, 10)
        self.answer = self.first_number + self.second_number
        return f"What is {self.first_number} + {self.second_number}?"

    def two_digit_addition(self):
        self.first_number = random.randint(10, 99)
        self.second_number = random.randint(0, 99)

        self.answer = self.first_number + self.second_number
        return f"What is {self.first_number} + {self.second_number}?"

    def multi_digit_addition(self):
        self.first_number = random.randint(12, 9999)
        self.second_number = random.randint(10, self.first_number)

        self.answer = self.first_number + self.second_number
        return f"What is {self.first_number} + {self.second_number}?"

    def one_digit_subtraction(self):
        self.first_number = random.randint(0, 10)
        self.second_number = random.randint(0, self.first_number)
        self.answer = self.first_number - self.second_number
        return f"What is {self.first_number} - {self.second_number}?"

    def two_digit_subtraction(self):
        self.first_number = random.randint(10, 99)
        self.second_number = random.randint(0, self.first_number - 1)
        self.answer = self.first_number - self.second_number
        return f"What is {self.first_number} - {self.second_number}?"

    def multi_digit_subtraction(self):
        self.first_number = random.randint(12, 9999)
        self.second_number = random.randint(0, self.first_number)

        self.answer = self.first_number - self.second_number
        return f"What is {self.first_number} - {self.second_number}?"

    def one_digit_multiplication(self):
        self.first_number = random.randint(0, 10)
        self.second_number = random.randint(0, 10)
        self.answer = self.first_number * self.second_number
        return f"What is {self.first_number} x {self.second_number}?"

    def two_digit_multiplication(self):
        self.first_number = random.randint(10, 99)
        self.second_number = random.randint(1, 99)
        self.answer = self.first_number * self.second_number
        return f"What is {self.first_number} x {self.second_number}?"

    def one_digit_division(self):
        self.first_number = random.randint(1, 100)
        self.divisors = [x for x in range(1, 10) if self.first_number % x == 0]
        self.second_number = self.divisors[random.randint(0, len(self.divisors) - 1)]
        self.answer = self.first_number / self.second_number
        return f"What is {self.first_number} / {self.second_number}?"

    def two_digit_division(self):
        self.first_number = random.randint(1, 9999)
        self.divisors = [x for x in range(10, 99) if self.first_number % x == 0]
        self.second_number = self.divisors[random.randint(1, len(self.divisors) - 1)]
        self.answer = self.first_number / self.second_number
        return f"What is {self.first_number} / {self.second_number}?"


class Math_Screen(tk.Frame):
    def __init__(self, parent, ID, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.answer_verification = tk.StringVar()
        self.ans_insert = tk.StringVar()
        self.insert_num = tk.StringVar()
        self.Question_label = tk.StringVar()
        self.Question_label.set("Question # of 100")
        self.Time_label = tk.StringVar()
        self.time_left = 0
        self.ID = ID
        self.Question = Questions(self.ID)

        # User entry, Submit button and Labels for layout
        self.UserInsert_entry = ttk.Entry(self, textvariable=self.ans_insert)
        self.submit_button = ttk.Button(self, text="Submit", command=self.submit_ans)
        self.clear_button = ttk.Button(self, text="Clear", command= lambda : self.UserInsert_entry.delete(0, 'end'))
        self.Question_Label = ttk.Label(self, textvariable=self.Question_label,
                                font=("TkDefaultFont", 10), wraplength=600)

        Time_label = ttk.Label(self, textvariable=self.Time_label,
                                font=("TkDefaultFont", 10), wraplength=600)

        # Display Questions


        self.Display_Question = tk.StringVar()
        self.Display_Question.set(self.Question.toggle_topics())
        addition_question = ttk.Label(self, textvariable=self.Display_Question,
                                      font=("TkDefaultFont", 10), wraplength=600)

        addition_question.grid(row=1, column=0, sticky=tk.W)

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
        self.Question_Label.grid(row=0, column=0, sticky=tk.E)
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
                self.answer_verification.set("\nYour answer is incomprehensible")
                ttk.Label(self, textvariable=self.answer_verification,
                          font=("TkDefaultFont", 10), wraplength=101).grid(row=2, column=0, sticky=tk.W)
            else:
                # For
                if int(self.ans_insert.get()) == (self.Question.answer):
                    self.reset_fields()
                else:
                    print("Your answer is wrong.")
                    self.answer_verification.set("\nYour answer is wrong")
                    ttk.Label(self, textvariable=self.answer_verification,
                              font=("TkDefaultFont", 10), wraplength=101).grid(row=2, column=0, sticky=tk.W)
        else:
            print("Your answer is blank.")
            self.answer_verification.set("\nYour answer is blank")
            ttk.Label(self, textvariable=self.answer_verification,
                      font=("TkDefaultFont", 10), wraplength=101).grid(row=2, column=0, sticky=tk.W)

    def reset_fields(self):
        self.Display_Question.set(self.Question.toggle_topics())
        self.answer_verification.set('')


class Math_Screen_Settings(tk.Tk):
    """Screen settings"""

    def __init__(self, ID, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("600x500")
        self.resizable(width=False, height=False)
        self.ID = ID
        self.math_screen = Math_Screen(self, ID)

        self.math_screen.grid(sticky=(tk.E + tk.W + tk.N + tk.S))
        #self.math_screen.update_time(10)

        # self.t1 = threading.Thread(target=lambda : self.math_screen.grid(sticky=(tk.E + tk.W + tk.N + tk.S)), args=[])
        # self.t2 = threading.Thread(target=lambda : self.math_screen.update_time(10), args=[])
        #
        # self.t1.start()
        # self.t2.start()
        self.protocol("WM_DELETE_WINDOW", self.close_down_app)
        self.columnconfigure(0, weight=1)

    def close_down_app(self):
        if self.math_screen.time_left > 0:
            print("The timer must stop before the app is closed. ")

        else:
            self.destroy()


if __name__ == '__main__':
    ID = '2-DIV'
    app = Math_Screen_Settings(ID)
    app.mainloop()
