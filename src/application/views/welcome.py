#*******************
#Nov 7, 2020
#*******************
# This is the welcome screen for all developers to collaborate
# Need to decide on users_list common screen dimension for the program
# Investigate if you have users_list master frame or screen, that changes content for each page
# Program should have the ability to resize at will (stop at users_list minimum size), and full screen

# 1: Micah: Design, users_list nice picture, colors, users_list logo
# 2: Xade: Place the login and registration links, nice animation
# 3: Andrew: Description of the program, graphics
# 4: Milton: Link to terms of use (needs users_list new page)
# 5: Asher: Test the connection between the login and registration pages, testing all the code
# Team lead: Asher

#*******************
#Nov 16, 2020
#*******************
# 1: Micah: Design, users_list nice picture, colors, users_list logo
# 2: Xade: Place the login and registration links, nice animation. Collaborate with Asher in integrating all the code
#          into welcome.py.
# 3: Andrew: Description of the program, graphics. Collaborate with Asher in integrating all the code
#            into welcome.py.
# 4: Milton: Link to terms of use (needs users_list new page). Make it users_list pop up screen with generic terms
#            of use (google it). Give it an OK button to exit. Collaborate with Asher in integrating all the code
#            into welcome.py.
# 5: Asher: In charge of integrating everyone else's code into welcome.py.
#           Test the connection between the login and registration pages, testing all the code.
# Team lead: Asher

#Asher
"""This file contains DescriptionFrame which show the description of the program.
It is meant to be shown on the welcome screen."""
# Andrew

import tkinter as tk
from tkinter import ttk


class IconFrame(tk.Frame):
    """Contains and displays the description of the Math Facts Practice application."""
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.image = tk.PhotoImage(file="icon.ico")
        self.image_label = tk.Label(self, image=self.image)
        self.grid()
        self.image_label.grid()


class DescriptionFrame(tk.Frame):
    """Contains and displays the description of the Math Facts Practice application."""
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        description = "Welcome to Math Facts Practice! This app helps you or your child practice math facts using " \
                      "randomly generated problems. Math Facts includes exercises for addition, subtraction, " \
                      "multiplication, division, and more, based on the user's age and grade level. 100 problems are " \
                      "shown one at a time, and the user may enter a response using either a keyboard or mouse. After" \
                      " completing a test, the program shows all the problems and displays which ones the user " \
                      "answered correctly or incorrectly. You will have the ability to print the results or save them" \
                      " for future reference. You may view all completed tests as well as helpful tips on the reports" \
                      " screen.\n" \
                      "To get started, click 'Register'."

        desc_label = ttk.Label(self, text=description, wraplength=400, font=("TkDefaultFont", 11))
        desc_label.pack()