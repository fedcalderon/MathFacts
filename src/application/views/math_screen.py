# Xade
import tkinter as tk
from tkinter import ttk
import re
import threading
import time
import random
import math
#from src.application.views import results

#
# DIFFERENT TYPES OF PROBLEMS AND IDS:
# 1-ADD: Single digit addition
# 2-ADD: Double digit addition
# 3-ADD: Addition up to 5 digits
# 1-SUB: Single digit subtraction
# 2-SUB: Double digit subtraction
# 3-SUB: Subtraction up to 5 digits
# 1-MUL: Single  digit multiplication
# 2-MUL: Double digit multiplication
# 1-DIV: Division with a single digit divisor.
# 2-DIV: Division with a double digit divisor.


class Questions:
    def __init__(self, ID):
        self.ID = ID
        self.all_questions_taken = []
        #self.all_questions_taken.append([f"What is {self.first_number} + {self.second_number}?",  f"{self.answer}"])
        print(self.all_questions_taken)

    def toggle_topics(self):
        # Addition
        if self.ID == '1-ADD':
            self.first_number = random.randint(0, 10)
            self.second_number = random.randint(0, 10)
            self.symbol = '+'
            self.answer = self.first_number + self.second_number
            return f"What is {self.first_number} + {self.second_number}?"

        elif self.ID == '2-ADD':
            self.first_number = random.randint(10, 99)
            self.second_number = random.randint(0, 99)
            self.symbol = '+'
            self.answer = self.first_number + self.second_number
            return f"What is {self.first_number} + {self.second_number}?"

        elif self.ID == '3-ADD':
            self.first_number = random.randint(12, 9999)
            self.second_number = random.randint(10, self.first_number)
            self.symbol = '+'
            self.answer = self.first_number + self.second_number
            return f"What is {self.first_number} + {self.second_number}?"

        # Subtraction
        elif self.ID == '1-SUB':
            self.first_number = random.randint(0, 10)
            self.second_number = random.randint(0, self.first_number)
            self.symbol = '-'
            self.answer = self.first_number - self.second_number
            return f"What is {self.first_number} - {self.second_number}?"

        elif self.ID == '2-SUB':
            self.first_number = random.randint(10, 99)
            self.second_number = random.randint(0, self.first_number - 1)
            self.symbol = '-'
            self.answer = self.first_number - self.second_number
            return f"What is {self.first_number} - {self.second_number}?"

        elif self.ID == '3_SUB':
            self.first_number = random.randint(12, 9999)
            self.second_number = random.randint(0, self.first_number)
            self.symbol = '-'
            self.answer = self.first_number - self.second_number
            return f"What is {self.first_number} - {self.second_number}?"

        # Multiplication
        elif self.ID == '1-MUL':
            self.first_number = random.randint(0, 10)
            self.second_number = random.randint(0, 10)
            self.symbol = 'x'
            self.answer = self.first_number * self.second_number
            return f"What is {self.first_number} x {self.second_number}?"

        elif self.ID == '2-MUL':
            self.first_number = random.randint(10, 99)
            self.second_number = random.randint(1, 99)
            self.symbol = 'x'
            self.answer = self.first_number * self.second_number
            return f"What is {self.first_number} x {self.second_number}?"

        # Division
        elif self.ID == '1-DIV':
            self.first_number = random.randint(1, 100)
            self.divisors = [x for x in range(1, 10) if self.first_number % x == 0]
            self.second_number = self.divisors[random.randint(0, len(self.divisors) - 1)]
            self.symbol = '/'
            self.answer = self.first_number / self.second_number
            return f"What is {self.first_number} / {self.second_number}?"

        elif self.ID == '2-DIV':
            self.first_number = random.randint(1, 9999)
            self.divisors = [x for x in range(10, 99) if self.first_number % x == 0]
            self.second_number = self.divisors[random.randint(1, len(self.divisors) - 1)]
            self.symbol = '/'
            self.answer = self.first_number / self.second_number
            return f"What is {self.first_number} / {self.second_number}?"


class Math_Screen(tk.Frame):
    def __init__(self, parent, ID, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.answer_verification = tk.StringVar()
        self.ans_insert = tk.StringVar()
        self.insert_num = tk.StringVar()
        self.Question_Count = 1
        self.Total_Questions = 3
        self.all_questions_list = []

        self.Question_label = tk.StringVar()
        self.Question_label.set(f"Question # of {self.Total_Questions}")
        self.Time_label = tk.StringVar()
        self.time_left = 0

        self.ID = ID
        self.Question = Questions(self.ID)
        self.is_Question_Correct = False

        self.student_answer = 0

        # User entry, Submit button and Labels for layout
        self.UserInsert_entry = ttk.Entry(self, textvariable=self.ans_insert)
        self.submit_button = ttk.Button(self, text="Submit", command=self.submit_ans)
        self.clear_button = ttk.Button(self, text="Clear", command= lambda : self.UserInsert_entry.delete(0, 'end'))
        self.Question_Label = ttk.Label(self, textvariable=self.Question_label,
                                font=("TkDefaultFont", 10), wraplength=600)
        self.Question_is_correct = False
        self.incorrect_questions = 0

        Time_label = ttk.Label(self, textvariable=self.Time_label,
                                font=("TkDefaultFont", 10), wraplength=600)

        # Display Questions


        self.Display_Question = tk.StringVar()
        self.Display_Question.set(self.Question.toggle_topics())
        self.addition_question = ttk.Label(self, textvariable=self.Display_Question,
                                      font=("TkDefaultFont", 10), wraplength=600)

        self.addition_question.grid(row=1, column=0, sticky=tk.W)

        #Number buttons
        self.number_button0 = ttk.Button(self, text="0", command=lambda: self.UserInsert_entry.insert('end', "0"))
        self.number_button1 = ttk.Button(self, text="1", command=lambda: self.UserInsert_entry.insert('end', "1"))
        self.number_button2 = ttk.Button(self, text="2", command=lambda: self.UserInsert_entry.insert('end', "2"))
        self.number_button3 = ttk.Button(self, text="3", command=lambda: self.UserInsert_entry.insert('end', "3"))
        self.number_button4 = ttk.Button(self, text="4", command=lambda: self.UserInsert_entry.insert('end', "4"))
        self.number_button5 = ttk.Button(self, text="5", command=lambda: self.UserInsert_entry.insert('end', "5"))
        self.number_button6 = ttk.Button(self, text="6", command=lambda: self.UserInsert_entry.insert('end', "6"))
        self.number_button7 = ttk.Button(self, text="7", command=lambda: self.UserInsert_entry.insert('end', "7"))
        self.number_button8 = ttk.Button(self, text="8", command=lambda: self.UserInsert_entry.insert('end', "8"))
        self.number_button9 = ttk.Button(self, text="9", command=lambda: self.UserInsert_entry.insert('end', "9"))
        self.decimal_button = ttk.Button(self, text=".", command=lambda: self.UserInsert_entry.insert('end', "."))

        # Grid Layout
        self.UserInsert_entry.grid(row=5, column=2, sticky=(tk.E))
        self.submit_button.grid(row=5, column=3, sticky=tk.E)
        self.clear_button.grid(row=5, column=4, sticky=tk.E)
        self.Question_Label.grid(row=0, column=0, sticky=tk.E)
        Time_label.grid(row=0, column=12, sticky=tk.E)
        self.columnconfigure(1, weight=1)

        # number button grid
        self.number_button0.grid(row=11, column=2, sticky=(tk.E))
        self.number_button1.grid(row=10, column=2, sticky=(tk.E))
        self.number_button2.grid(row=10, column=3, sticky=(tk.E))
        self.number_button3.grid(row=10, column=4, sticky=(tk.W))
        self.number_button4.grid(row=9, column=2, sticky=(tk.E))
        self.number_button5.grid(row=9, column=3, sticky=(tk.E))
        self.number_button6.grid(row=9, column=4, sticky=(tk.W))
        self.number_button7.grid(row=8, column=2, sticky=(tk.E))
        self.number_button8.grid(row=8, column=3, sticky=(tk.E))
        self.number_button9.grid(row=8, column=4, sticky=(tk.W))
        self.decimal_button.grid(row=11, column=4, sticky=(tk.W))

    def update_time(self, start_time):
        self.time_left = start_time
        for x in range(start_time, -1, -1):
            self.time_left = x
            time.sleep(1)
            self.Time_label.set(f"Time Left: {self.time_left}")
            print(self.time_left)

    def submit_ans(self):
        if self.Question_Count - 1 < self.Total_Questions:
            if len(self.ans_insert.get()) > 0:
                if re.search('[a-zA-Z]', self.ans_insert.get()):
                    print("Your answer is incomprehensible.")
                    self.answer_verification.set("\nYour answer is incomprehensible")
                    ttk.Label(self, textvariable=self.answer_verification,
                              font=("TkDefaultFont", 10), wraplength=101).grid(row=2, column=0, sticky=tk.W)
                else:

                    self.all_questions_list.append([f"What is {self.Question.first_number} {self.Question.symbol} "
                                            f"{self.Question.second_number}?", f"{self.ans_insert.get()}"])
                    self.student_answer = self.ans_insert.get()
                    for x in range(0, len(self.all_questions_list)):
                        if len(self.all_questions_list) >= 2:

                            if len(self.all_questions_list) == 2:
                                if self.all_questions_list[x][0] == self.all_questions_list[x - 1][0]:
                                    self.all_questions_list[x].append("INCORRECT")
                                    self.all_questions_list.remove(self.all_questions_list[x - 1])
                                    self.incorrect_questions += 1

                            if len(self.all_questions_list) > 2:
                                if self.all_questions_list[x][0] == self.all_questions_list[x - 1][0]:
                                    self.all_questions_list[x - 1].append("INCORRECT")
                                    self.all_questions_list.remove(self.all_questions_list[x])
                                    self.incorrect_questions += 1

                    # If the student's answer is correct...
                    if int(self.ans_insert.get()) == (self.Question.answer):
                        self.Question_Count = self.Question_Count + 1
                        self.Question_label.set(f"Question #{self.Question_Count} of {self.Total_Questions}")
                        self.reset_fields()

                    else:
                        print(f"Your answer is wrong.")
                        print(self.all_questions_list)
                        self.answer_verification.set(f"\nYour answer is wrong.")
                        ttk.Label(self, textvariable=self.answer_verification,
                                  font=("TkDefaultFont", 10), wraplength=101).grid(row=2, column=0, sticky=tk.W)

                    # question_list updating should go here
                    print(self.all_questions_list)

            else:
                print("Your answer is blank.")
                self.answer_verification.set("\nYour answer is blank")
                ttk.Label(self, textvariable=self.answer_verification,
                          font=("TkDefaultFont", 10), wraplength=101).grid(row=2, column=0, sticky=tk.W)

        if self.Question_Count - 1 == self.Total_Questions:
            ttk.Label(self, text="You have completed all questions. Close the window to view your answers and grade.",
                      font=("TkDefaultFont", 10), wraplength=101).grid(row=2, column=0, sticky=tk.W)
            self.Display_Question.set('')
            self.Question_label.set('')


    def reset_fields(self):
        self.Display_Question.set(self.Question.toggle_topics())
        self.answer_verification.set('')
        self.ans_insert.set('')


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

    # def close_down_app(self):
    #     if self.math_screen.time_left > 0:
    #         print("The timer must stop before the app is closed. ")
    #
    #     else:
    #         self.destroy()

    def close_down_app(self):
        # if self.math_screen.Question_Count < self.math_screen.Total_Questions + 1:
        #     print(f"You must complete at least {self.math_screen.Total_Questions} questions. ")
        #     ttk.Label(self, text=f"You must complete at least {self.math_screen.Total_Questions} questions. ",
        #               font=("TkDefaultFont", 10), wraplength=101).grid(row=2, column=0, sticky=tk.W)
        #
        # else:
            self.destroy()




if __name__ == '__main__':
    test_ID = '1-ADD'
    app = Math_Screen_Settings(test_ID)
    # while len(app.math_screen.all_questions_list) < 3:
    app.mainloop()
    #results.ResultsScreen(app).mainloop()

