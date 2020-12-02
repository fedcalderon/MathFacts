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
from tkinter import *
from tkinter import ttk


class TermsOfUseWindow(tk.Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        # Used this from andrews code to display window
        description = "No copying this program or using it illegally. It is strictly for the use of Math Facts purposes only. \n"
        desc_label = ttk.Label(self, text=description, wraplength=200, font=("TkDefaultFont", 14))
        desc_label.pack()


class IconFrame(tk.Frame):
    """Contains and displays the description of the Math Facts Practice application."""
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.image = tk.PhotoImage(file="icon.ico")
        self.image_label = tk.Label(self, image=self.image)


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


class LinksFrame(tk.Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        # Frame with button links(right now only terms of use)
        self.terms_of_use_link = ttk.Button(self, text="Terms Of Use", command=self.terms_of_use_open)
        self.terms_of_use_link.grid(row=100, column=0, sticky=tk.W)

    def terms_of_use_open(self):
        # Terms of use window
        root = tk.Tk()
        root.title('Terms Of Use')
        root.resizable(width=False, height=False)
        root.geometry('340x120')
        TermsOfUseWindow(root).pack(expand=True, fill='both')
        root.mainloop()


class WelcomeView(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("MathFacts")
        self.geometry("1000x650")

        self.resizable(width=True, height=True)

        # FRAMES
        self.icon_frame = IconFrame(self)
        self.icon_frame.grid()
        self.icon_frame.image_label.grid()

        self.description = DescriptionFrame(self)
        self.description.grid(sticky=(tk.E + tk.W + tk.N + tk.S))

        self.links = LinksFrame(self)
        self.links.grid(sticky=(tk.E + tk.W + tk.N + tk.S))

        self.columnconfigure(0, weight=1)
