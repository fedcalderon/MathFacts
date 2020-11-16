"""This file contains DescriptionFrame which show the description of the program.
It is meant to be shown on the welcome screen."""
# Andrew
import tkinter as tk
from tkinter import ttk


class DescriptionFrame(tk.Frame):
    """Contains and displays the description of the Math Facts Practice application."""
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        description = "Welcome to Math Facts Practice! This app helps you or your child practice math facts using " \
                      "randomly generated problems. Math Facts includes exercises for addition, subtraction, " \
                      "multiplication, division, and more. After completing a test, you will have the ability to " \
                      "print the results or save them for future reference. You may view all completed tests as " \
                      "well as helpful tips on the reports screen.\n" \
                      "To get started, click 'Create an Account'."

        desc_label = ttk.Label(self, text=description, wraplength=400, font=("TkDefaultFont", 11))
        desc_label.pack()


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Math Facts Practice')
    root.resizable(width=False, height=False)
    root.geometry('500x300')
    DescriptionFrame(root).pack(expand=True, fill='both')
    root.mainloop()
