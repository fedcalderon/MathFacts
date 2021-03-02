# This is a work in progress. This keeps all the screens in a single window.
# The major difference between this and the current program is that all the screens are contained in lists rather than
#   tk windows.
#
#
#
#
#
#
import tkinter as tk
from tkinter import ttk
import csv
import src.application.tests.welcome as welcome
import src.application.tests.registration as r
import src.application.tests.login as login
import src.application.tests.problem_selection as ps

class MyApplication(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("MathFacts")
        self.geometry("1000x650")
        self.resizable(width=True, height=True)
        self.display_welcome_screen()
        self.columnconfigure(0, weight=1)

    def display_welcome_screen(self):
        # Under the new system, there is only one window.
        # Each view is a list of frames.
        # For now, buttons are stored separately from other frames and have to be appended to the list.

        # Welcome_screen
        self.welcome_screen = [welcome.IconFrame(self), welcome.DescriptionFrame(self)]

        # Bridge buttons(buttons that connect the welcome view to other views)
        self.registration_button = ttk.Button(self, text="Registration",
                                              command=lambda: self.change_screen(
                                                  self.welcome_screen, self.registration_screen))

        self.terms_of_use_button = ttk.Button(self, text="Terms Of Use", command=lambda: self.change_screen(
            self.welcome_screen, self.terms_of_use_screen))

        self.login_button = ttk.Button(self, text="Login", command=lambda: self.change_screen(
            self.welcome_screen, self.login_screen))

        self.problem_selection_button = ttk.Button(self, text="Problem Selection", command=lambda: self.change_screen(
            self.welcome_screen, self.problem_selection_screen))

        self.welcome_screen.extend([self.terms_of_use_button, self.registration_button,
                                    self.login_button, self.problem_selection_button])

        # Append all frames to the welcome view
        for item in self.welcome_screen:
            item.grid(sticky=(tk.W + tk.E + tk.N + tk.S))

        # Terms of use screen
        self.terms_of_use_description = "No copying this program or using it illegally. " \
                                        "It is strictly for the use of Math Facts purposes only. \n"
        self.desc_label = ttk.Label(
            self, text=self.terms_of_use_description, wraplength=400, font=("TkDefaultFont", 11))

        self.terms_of_use_screen = [ttk.Label(self, text="Terms Of Use",
                                              font=("TkDefaultFont", 27), wraplength=600), self.desc_label]

        self.terms_of_use_back = tk.Button(self, text="Back",
                                           command=lambda: self.change_screen(
                                               self.terms_of_use_screen, self.welcome_screen))
        self.terms_of_use_screen.append(self.terms_of_use_back)

        # Registration screen
        self.registration_screen = [ttk.Label(self, text="Signup for MathFacts",
                                              font=("TkDefaultFont", 27), wraplength=600),
                                    r.ChildInformation(self), r.Guardian1Info(self), r.Guardian2Info(self),
                                    r.LoginInformation(self)]

        # Login screen
        self.username_verify = tk.StringVar()
        self.password_verify = tk.StringVar()
        self.username_login_entry = tk.Entry(self, textvariable=self.username_verify)
        self.password_login_entry = tk.Entry(self, textvariable=self.password_verify, show='*')
        self.result_message = ""
        self.student = {}
        self.student_id = ''
        self.username1 = self.username_verify.get()
        self.password1 = self.password_verify.get()
        self.login_success_screen = tk.Toplevel(self)
        self.login_screen = [tk.Label(self, text='Please enter details below to login'),
                             tk.Label(self, text=''),
                             tk.Label(self, text="Username * "),
                             self.username_login_entry,
                             tk.Label(self, text=""),
                             tk.Label(self, text="Password * "),
                             self.password_login_entry,
                             tk.Label(self, text=""),
                             tk.Button(self, text="Login", width=10, height=1, command=
                                lambda: login.login_verify(self))
                             ]

        # Problem selection screen
        self.problem_selection_screen = [ps.SelectionView(self, self, student = {'child_grade': 1,
               'username': 'TestUser'})]


    def change_screen(self, current_screen, new_screen):
        # This method runs when a bridging button(buttons that connect two views) is clicked.
        # It deletes all frames in the current view, and replaces them with all the frames in the new view.
        for item in current_screen:
            item.grid_forget()
        for item in new_screen:
            item.grid(sticky=(tk.W + tk.E + tk.N + tk.S))


if __name__ == '__main__':
    app = MyApplication()
    app.mainloop()
