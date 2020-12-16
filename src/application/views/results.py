# Showing all problems worked on by user
# Milton
from tkinter import *
import time
from src.application.views import math_screen

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