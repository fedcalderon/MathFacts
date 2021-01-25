# Showing all problems worked on by user
# Milton
from tkinter import *
import time
from src.application.views import math_screen


# Frame
class LinksFrame(Frame):
    def __init__(self, parent, problems, **kwargs):
        super().__init__(parent, **kwargs)

        # List and print all problem set grades.
        if len(problems.math_screen.all_questions_list) > 0:
            for x in range(0, len(problems.math_screen.all_questions_list)):
                if len(problems.math_screen.all_questions_list[x]) >= problems.math_screen.Total_Questions:
                    Label(self, text=f"Question {x + 1}: {problems.math_screen.all_questions_list[x][0]} --- "
                                     f"Student Answer: {problems.math_screen.all_questions_list[x][1]}. "
                                     f"{problems.math_screen.all_questions_list[x][2]}.",
                          wraplength=400, font=("TkDefaultFont", 11)).grid(sticky=W)
                else:
                    Label(self, text=f"Question {x + 1}: {problems.math_screen.all_questions_list[x][0]} --- "
                                     f"Student Answer: {problems.math_screen.all_questions_list[x][1]}. "
                                     f"CORRECT.",
                          wraplength=400, font=("TkDefaultFont", 11)).grid(sticky=W)

            Label(self, text=f"Asssignment grade is: "
                             f"{int(round(((len(problems.math_screen.all_questions_list) - problems.math_screen.incorrect_questions) / len(problems.math_screen.all_questions_list)) * 100, 2))}%",
                  wraplength=400, font=("TkDefaultFont", 11)).grid(sticky=W)

        else:
            Label(self, text=f"You did no questions. Grade: 0%"
                             ,
                  wraplength=400, font=("TkDefaultFont", 11)).grid(sticky=W)

        # desc_label.grid()


# Results screen
class ResultsScreen(Tk):
    def __init__(self, ms, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.geometry("600x800")

        self.LinksFrame = LinksFrame(self, ms)
        #if len(ms_window.math_screen.all_questions_list) > 3:
        self.LinksFrame.grid()


if __name__ == "__main__":
    ms_window_id = '1-SUB'
    ms_window = math_screen.Math_Screen_Settings(ms_window_id)
    # ms_window.geometry("600x500")
    ms_window.resizable(width=False, height=False)

    ms_window.mainloop()
    Results = ResultsScreen(ms_window)
    Results.mainloop()
