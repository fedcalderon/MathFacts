# Xade
import random
import time
import tkinter as tk
from tkinter import ttk
from src.application.models.question import Question
from src.application.new_views import results


# DIFFERENT TYPES OF PROBLEMS AND IDS:
# 1-ADD: Single digit addition
# 2-ADD: Double digit addition
# 3-ADD: Addition up to 5 digits
# 1-SUB: Single digit subtraction
# 2-SUB: Double digit subtraction
# 3-SUB: Subtraction up to 5 digits
# 1-MUL: Single digit multiplication
# 2-MUL: Double digit multiplication
# 1-DIV: Division with a single digit divisor.
# 2-DIV: Division with a double digit divisor.


class Questions:
    def __init__(self, ID):
        self.ID = ID
        self.all_questions_taken = []
        # self.all_questions_taken.append([f"What is {self.first_number} + {self.second_number}?",  f"{self.answer}"])
        # print(self.all_questions_taken)

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
            divisors = [x for x in range(1, self.first_number + 1) if self.first_number % x == 0]
            self.second_number = divisors[random.randint(0, len(divisors) - 1)]
            self.symbol = '÷'
            self.answer = int(self.first_number / self.second_number)
            return f"What is {self.first_number} ÷ {self.second_number}?"

        elif self.ID == '2-DIV':
            self.first_number = random.randint(50, 999)
            # hard_divisors excludes 1 and the first number
            hard_divisors = [x for x in range(2, self.first_number) if self.first_number % x == 0]
            if len(hard_divisors) == 0:
                # Use 1 and the first number as possible divisors if there are no hard_divisors
                divisors = [1, self.first_number]
            else:
                # Use hard_divisors as possible divisors
                divisors = hard_divisors
            self.second_number = divisors[random.randint(0, len(divisors) - 1)]
            self.symbol = '÷'
            self.answer = int(self.first_number / self.second_number)
            return f"What is {self.first_number} ÷ {self.second_number}?"


# TODO: Prevent same question from appearing multiple times
class Math_Screen(tk.Frame):
    def __init__(self, parent, ID, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.parent = parent
        self.answer_verification = tk.StringVar()
        self.ans_insert = tk.StringVar()
        self.insert_num = tk.StringVar()
        self.Question_Count = 1
        self.Total_Questions = 20
        self.questions_list = []
        self.finished = False

        self.Correct_Answers = 0

        self.Question_label = tk.StringVar()
        self.Question_label.set(f"Question # of {self.Total_Questions}")
        self.Time_label = tk.StringVar()
        self.time_left = 0

        self.ID = ID
        self.questions = Questions(self.ID)
        self.is_Question_Correct = False

        self.student_answer = 0

        # User entry, Submit button and Labels for layout
        self.UserInsert_entry = ttk.Entry(self, textvariable=self.ans_insert)
        self.UserInsert_entry.bind("<Key>", self.entry_key)
        self.submit_button_text = tk.StringVar()
        self.submit_button_text.set('Submit')
        self.submit_button = ttk.Button(self, textvariable=self.submit_button_text, command=self.submit_ans)
        self.clear_button = ttk.Button(self, text="Clear", command=lambda: self.UserInsert_entry.delete(0, 'end'))
        self.Question_Label = ttk.Label(self, textvariable=self.Question_label,
                                        font=("TkDefaultFont", 10), wraplength=600)
        self.Question_is_correct = False
        self.form_enabled = True
        time_label = ttk.Label(self, textvariable=self.Time_label,
                               font=("TkDefaultFont", 10), wraplength=600)

        # Display Questions
        self.Display_Question = tk.StringVar()
        self.addition_question = ttk.Label(self, textvariable=self.Display_Question,
                                           font=("TkDefaultFont", 10), wraplength=600)

        self.addition_question.grid(row=1, column=0, sticky=tk.W)

        # Number buttons
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
        time_label.grid(row=0, column=12, sticky=tk.E)
        self.columnconfigure(1, weight=1)

        # Number button grid
        self.number_button0.grid(row=11, column=2, sticky=tk.E)
        self.number_button1.grid(row=10, column=2, sticky=tk.E)
        self.number_button2.grid(row=10, column=3, sticky=tk.E)
        self.number_button3.grid(row=10, column=4, sticky=tk.W)
        self.number_button4.grid(row=9, column=2, sticky=tk.E)
        self.number_button5.grid(row=9, column=3, sticky=tk.E)
        self.number_button6.grid(row=9, column=4, sticky=tk.W)
        self.number_button7.grid(row=8, column=2, sticky=tk.E)
        self.number_button8.grid(row=8, column=3, sticky=tk.E)
        self.number_button9.grid(row=8, column=4, sticky=tk.W)
        self.decimal_button.grid(row=11, column=4, sticky=tk.W)

        self.results_screen = results.LinksFrame(parent, self, 'test')

        self.reset_fields()
        # Set focus on text box
        self.UserInsert_entry.focus()

        self.results_screen = tk.Button(self, text="Show Grades", command=lambda: parent.change_screen(
            parent.math_problems_screen, [results.LinksFrame(parent, self, 'test')]))

    def enable_buttons(self, enable=True):
        if enable:
            set_state = 'normal'
            self.submit_button_text.set('Submit')
            self.form_enabled = True
        else:
            set_state = 'disabled'
            self.submit_button_text.set('Next')
            self.form_enabled = False
        self.clear_button['state'] = set_state
        self.decimal_button['state'] = set_state
        self.number_button0['state'] = set_state
        self.number_button1['state'] = set_state
        self.number_button2['state'] = set_state
        self.number_button2['state'] = set_state
        self.number_button3['state'] = set_state
        self.number_button4['state'] = set_state
        self.number_button5['state'] = set_state
        self.number_button6['state'] = set_state
        self.number_button7['state'] = set_state
        self.number_button8['state'] = set_state
        self.number_button9['state'] = set_state
        self.UserInsert_entry['state'] = set_state

    def update_time(self, start_time):
        self.time_left = start_time
        for x in range(start_time, -1, -1):
            self.time_left = x
            time.sleep(1)
            self.Time_label.set(f"Time Left: {self.time_left}")
            print(self.time_left)

    def entry_key(self, key):
        # If the user presses the enter key, submit their answer
        if key.char == '\r':
            self.submit_ans()

    def submit_ans(self):
        if self.finished:
            # Don't do anything
            return
        if self.form_enabled is not True:
            self.enable_buttons(True)
            self.answer_verification.set('')
            self.reset_fields()
            return
        if self.Question_Count - 1 < self.Total_Questions:
            if len(self.ans_insert.get()) > 0:
                # Make sure the user's input can be represented as an int
                try:
                    student_answer = int(self.ans_insert.get())
                except ValueError:
                    print("Your answer is incomprehensible.")
                    self.answer_verification.set("\nYour answer is incomprehensible")
                    ttk.Label(self, textvariable=self.answer_verification,
                              font=("TkDefaultFont", 10), wraplength=101).grid(row=2, column=0, sticky=tk.W)
                    return

                text = f"What is {self.questions.first_number} {self.questions.symbol} {self.questions.second_number}?"
                question = Question(question_type=self.ID,
                                    first_num=self.questions.first_number,
                                    second_num=self.questions.second_number,
                                    symbol=self.questions.symbol,
                                    correct_ans=self.questions.answer,
                                    student_ans=student_answer,
                                    text=text)
                self.questions_list.append(question)

                # Check if the student's answer is correct
                if student_answer == self.questions.answer:
                    self.Question_Count += 1
                    self.Correct_Answers += 1
                    self.reset_fields()
                else:
                    print(f"Your answer is wrong.")
                    self.Question_Count += 1
                    self.answer_verification.set(f"\nYour answer is wrong.")
                    ttk.Label(self, textvariable=self.answer_verification,
                              font=("TkDefaultFont", 10), wraplength=101).grid(row=2, column=0, sticky=tk.W)
                    self.enable_buttons(False)
            else:
                print("Your answer is blank.")
                self.answer_verification.set("\nYour answer is blank")
                ttk.Label(self, textvariable=self.answer_verification,
                          font=("TkDefaultFont", 10), wraplength=101).grid(row=2, column=0, sticky=tk.W)

        if self.Question_Count - 1 == self.Total_Questions:
            self.results_screen.grid()
            self.reset_exercise(self.parent)

        # Set the focus back to the entry
        self.UserInsert_entry.focus()

    def reset_exercise(self, parent_screen):
        self.finished = True
        self.reset_fields()
        self.enable_buttons(False)
        self.submit_button['state'] = 'disabled'
        ttk.Label(self, text="You have completed this task.",
                  font=("TkDefaultFont", 10), wraplength=101).grid(row=2, column=0, sticky=tk.W)
        self.Display_Question.set('')
        self.Question_label.set('')

    def reset_fields(self):
        self.Display_Question.set(self.questions.toggle_topics())
        self.answer_verification.set('')
        self.ans_insert.set('')
        self.Question_label.set(f"Question #{self.Question_Count} of {self.Total_Questions}")
