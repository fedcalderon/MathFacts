# Showing all problems worked on by user
# Milton
from tkinter import *
import time
from src.application.views import math_screen


ms_window = math_screen.Math_Screen_Settings('1-ADD')
#ms_window.geometry("600x500")
ms_window.resizable(width=False, height=False)


# Frame
class LinksFrame(Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        # Frame with button links

        # desc_label = Label(self, text=description, wraplength=400, font=("TkDefaultFont", 11))
        for x in range(0, len(ms_window.math_screen.all_questions_list)):
            if(len(ms_window.math_screen.all_questions_list[x]) >= ms_window.math_screen.Total_Questions):
                Label(self, text=f"Question {x + 1}: {ms_window.math_screen.all_questions_list[x][0]} --- "
                                 f"Student Answer: {ms_window.math_screen.all_questions_list[x][1]}. "
                                 f"{ms_window.math_screen.all_questions_list[x][2]}.",
                      wraplength=400, font=("TkDefaultFont", 11)).grid(sticky=W)
            else:
                Label(self, text=f"Question {x + 1}: {ms_window.math_screen.all_questions_list[x][0]} --- "
                                 f"Student Answer: {ms_window.math_screen.all_questions_list[x][1]}. "
                                 f"CORRECT.",
                      wraplength=400, font=("TkDefaultFont", 11)).grid(sticky=W)

        Label(self, text=f"Asssignment grade is: "
                         f"{int(round(((len(ms_window.math_screen.all_questions_list) - ms_window.math_screen.incorrect_questions) / len(ms_window.math_screen.all_questions_list)) * 100, 2))}%",
              wraplength=400, font=("TkDefaultFont", 11)).grid(sticky=W)
        # desc_label.grid()


# Results screen
class ResultsScreen(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.geometry("600x800")

        self.LinksFrame = LinksFrame(self)
        #if len(ms_window.math_screen.all_questions_list) > 3:
        self.LinksFrame.grid()


if __name__ == "__main__":
    ms_window.mainloop()
    Results = ResultsScreen()
    Results.mainloop()