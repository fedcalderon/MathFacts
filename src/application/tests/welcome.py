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
from src.application.views import login
from src.application.views import registration
import json
from pathlib import Path


class TermsOfUseWindow(tk.Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        # Used this from andrews code to display window
        description = "No copying this program or using it illegally. It is strictly for the use of Math Facts " \
                      "purposes only. \n"
        desc_label = ttk.Label(self, text=description, wraplength=200, font=("TkDefaultFont", 14))
        desc_label.pack()


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


class LinksFrame(tk.Frame):
    def __init__(self, parent, screen_to_destroy, registration_screen, **kwargs):
        super().__init__(parent, **kwargs)

        # Popup Windows
        self.screen_to_destroy = screen_to_destroy
        self.parent = parent

        # Frame with button links
        self.terms_of_use_link = ttk.Button(self, text="Terms Of Use", command=self.terms_of_use_open)
        self.terms_of_use_link.grid(row=100, column=0, sticky=tk.W)

        self.registration_button = ttk.Button(self, text="Registration",
            command=lambda: self.Registration_start(registration_screen))
        self.registration_button.grid(row=100, column=100, sticky=(tk.E))
        self.registration_pressed = False

        self.login_button = ttk.Button(self, text="Login", command=self.Login_start)
        self.login_button.grid(row=100, column=200, sticky=(tk.E))
        self.login_pressed = False

    def Registration_start(self, registration_screen):
        self.screen_to_destroy.change_screen(self.parent.welcome_screen, registration_screen)

    def terms_of_use_open(self):
        # Terms of use window
        self.root = tk.Tk()
        self.root.title('Terms Of Use')
        self.root.resizable(width=False, height=False)
        self.root.geometry('340x121')
        TermsOfUseWindow(self.root).pack(expand=True, fill='both')
        self.root.mainloop()

    def Login_start(self):
        # self.login_pressed = True
        # #login.login()
        # self.screen_to_destroy.destroy()
        # login_window = login.LoginScreen()
        # login_window.mainloop()
        x = 5
    # Open registration.py


class WelcomeView(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("MathFacts")
        self.geometry("1000x650")

        self.resizable(width=True, height=True)

        with open(f'{Path().absolute()}\student_data.json', 'w') as jsonfile:
                json.dump({}, jsonfile)

        # FRAMES
        self.icon_frame = IconFrame(self)
        self.description = DescriptionFrame(self)
        self.description.grid(sticky=(tk.E + tk.W + tk.N + tk.S))
        self.links = LinksFrame(self, self)
        self.links.grid(sticky=(tk.E + tk.W + tk.N + tk.S))

        self.columnconfigure(0, weight=1)

    def kill_everything(self):
        self.destroy()


if __name__ == '__main__':
    app = WelcomeView()
    app.mainloop()


    # if app.links.registration_pressed:
    #     registration_app = registration.MyApplication()
    #     registration_app.mainloop()
