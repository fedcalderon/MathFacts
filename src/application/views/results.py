# Showing all problems worked on by user
# Milton
from tkinter import *
import time
from src.application.views import math_screen


# window = Tk()
#
# window.title("Math Problems")
# menu = Menu(window)
#
# canvas_width = 400
# canvas_height = 400
#
# w = Canvas(window, width=canvas_width, height=canvas_height, bg="#B7F9E3")
# w.pack()
#
# a = int(input("enter first number: "))
# operation = input("enter the type of equation: ")
# b = int(input("enter second number: "))
#
#
# def add(a,b):
#     c = a + b
#     return str(c)
#
# def subtract(a,b):
#     c = a - b
#     return str(c)
#
# def division(a,b):
#     c = a / b
#     return str(c)
#
# def multiply(a, b):
#     c = a * b
#     return str(c)
#
# if operation == "+":
#     d = add(a,b)
#
# if operation == "-":
#     d = subtract(a, b)
#
# if operation == "/":
#     d = division(a, b)
#
# if operation == "*":
#     d = multiply(a, b)
#
# if operation == "+":
#     w.create_text(100, 50, font=("times new roman", 16), text="Addition Results")
#     w.create_text(200, 200, font=("times new roman", 16), text=d)
#
# if operation == "-":
#     w.create_text(100, 50, font=("times new roman", 16), text="Subtraction Results")
#     w.create_text(200, 200, font=("times new roman", 16), text=d)
#
# if operation == "*":
#     w.create_text(100, 50, font=("times new roman", 16), text="Multiplication Results")
#     w.create_text(200, 200, font=("times new roman", 16), text=d)
#
# if operation == "/":
#     w.create_text(100, 50, font=("times new roman", 16), text="Division Results")
#     w.create_text(200, 200, font=("times new roman", 16), text=d)
#
# window.config(menu=menu)
# window.mainloop()


math_screen_window = math_screen.Math_Screen_Settings('1-ADD')
math_screen_window.geometry("600x500")
math_screen_window.resizable(width=False, height=False)
math_screen_window.mainloop()

# Frame
class LinksFrame(Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        # Frame with button links

        # desc_label = Label(self, text=description, wraplength=400, font=("TkDefaultFont", 11))
        for x in range(0, len(math_screen_window.math_screen.all_questions_list)):
            if(len(math_screen_window.math_screen.all_questions_list[x]) >= 3):
                Label(self, text=f"Question {x + 1}: {math_screen_window.math_screen.all_questions_list[x][0]} --- "
                                 f"Student Answer: {math_screen_window.math_screen.all_questions_list[x][1]}. "
                                 f"{math_screen_window.math_screen.all_questions_list[x][2]}.",
                      wraplength=400, font=("TkDefaultFont", 11)).grid(sticky=W)
            else:
                Label(self, text=f"Question {x + 1}: {math_screen_window.math_screen.all_questions_list[x][0]} --- "
                                 f"Student Answer: {math_screen_window.math_screen.all_questions_list[x][1]}. "
                                 f"CORRECT.",
                      wraplength=400, font=("TkDefaultFont", 11)).grid(sticky=W)

        # desc_label.grid()

# Results screen
class ResultsScreen(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.LinksFrame = LinksFrame(self)
        self.LinksFrame.grid()

Results = ResultsScreen()
Results.mainloop()