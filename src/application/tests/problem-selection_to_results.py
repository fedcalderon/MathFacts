import tkinter as tk
from tkinter import ttk
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

        # problem_selection screen
        self.welcome_screen = [ps.SelectionView(self, self, student = {'child_grade': 1, 'username': 'TestUser'})]

        # Bridge buttons(buttons that connect the welcome view to other views)
        self.registration_button = ttk.Button(self, text="Registration",
                                              command=lambda: self.change_screen(
                                                  self.welcome_screen, self.registration_screen))

        self.terms_of_use_button = ttk.Button(self, text="Terms Of Use", command=lambda: self.change_screen(
            self.welcome_screen, self.terms_of_use_screen))

        self.welcome_screen.extend([self.registration_button, self.terms_of_use_button])


    def change_screen(self, current_screen, new_screen):
        # This method runs when a bridging button(buttons that connect two views) is clicked.
        # It deletes all frames in the current view, and replaces them with all the frames in the new view.
        for item in current_screen:
            item.destroy()
        for item in new_screen:
            item.grid(sticky=(tk.W + tk.E + tk.N + tk.S))


if __name__ == '__main__':
    app = MyApplication()
    app.mainloop()