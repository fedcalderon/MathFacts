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

        self.welcome_screen.extend([self.registration_button, self.terms_of_use_button])

        # Append all frames to the welcome view
        for item in self.welcome_screen:
            item.grid(sticky=(tk.W + tk.E + tk.N + tk.S))

        # Registration screen
        self.registration_screen = [ttk.Label(self, text="Signup for MathFacts",
                                              font=("TkDefaultFont", 27), wraplength=600),
                                    r.ChildInformation(self), r.Guardian1Info(self), r.Guardian2Info(self),
                                    r.LoginInformation(self)]

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
