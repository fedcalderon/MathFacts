# This is a work in progress. This keeps all the screens in a single window.
# The major difference between this and the current program is that all the screens are contained in lists rather than
#   tk windows.

import tkinter as tk
from tkinter import ttk

import src.application.new_views.login as new_login
import src.application.new_views.problem_selection as ps
import src.application.new_views.registration as registration
import src.application.new_views.math_screen as ms
import src.application.new_views.user_settings as user_settings
import src.application.new_views.welcome as welcome
import src.application.new_views.reports as reports
import src.application.new_views.dashboard as dashboard
import src.application.tests.modified_logger as logger
from src.application.models import database


class MyApplication(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("MathFacts")
        self.geometry("1000x650")
        self.resizable(width=True, height=True)

        self.welcome_screen = [welcome.IconFrame(self), welcome.DescriptionFrame(self)]
        self.current_screen = self.welcome_screen

        self.student_data = {}
        self.student_id = ''
        self.logged_in = False

        self.display_welcome_screen()
        self.columnconfigure(0, weight=1)

    def display_welcome_screen(self):
        # Under the new system, there is only one window.
        # Each view is a list of frames.
        # For now, buttons are stored separately from other frames and have to be appended to the list.

        # Bridge buttons(buttons that connect the welcome view to other archived)
        self.registration_button = ttk.Button(self, text="Register",
                                              command=lambda: self.change_screen(self.registration_screen))

        self.terms_of_use_button = ttk.Button(self, text="Terms Of Use", command=lambda: self.change_screen(
            self.terms_of_use_screen))

        self.login_button = ttk.Button(self, text="Login", command=lambda: self.change_screen(self.login_screen))

        self.problem_selection_button = ttk.Button(self, text="Problem Selection", state='disabled',
                                                   command=lambda: self.change_screen(self.problem_selection_screen))

        self.dashboard_button = ttk.Button(self, text="Go to Dashboard", command=lambda: self.change_screen(
            self.dashboard_screen))

        # self.math_problems_button = ttk.Button(self, text="Sample Math Lesson", command=lambda: self.change_screen(
        #     self.math_problems_screen))

        self.welcome_screen.extend([self.terms_of_use_button, self.registration_button,
                                    self.login_button, self.problem_selection_button, self.dashboard_button])

        for item in self.welcome_screen:
             item.grid()

        # Dashboard Screen
        self.dashboard_screen = [tk.Label(self, text="Dashboard", font=("", 25)), dashboard.Dashboard(self), tk.Button(self, text="Exit", command=lambda: self.change_screen(self.welcome_screen))]

        # Settings screen
        self.settings_screen = [user_settings.SettingsFrame(self),
                                tk.Button(self, text="To Topics List", command=lambda: self.change_screen(
                                    self.problem_selection_screen)),
                                tk.Button(self, text="Back", command=lambda: self.change_screen(
                                    self.welcome_screen))]

        # Reports screen
        self.reports_screen = [reports.ReportsFrame(self),
                               tk.Button(self, text="Back", command=lambda: self.change_screen(self.welcome_screen))]

        # Terms of use screen
        self.terms_of_use_description = "No copying this program or using it illegally. " \
                                        "It is strictly for the use of Math Facts purposes only. \n"

        self.desc_label = ttk.Label(
            self, text=self.terms_of_use_description, wraplength=400, font=("TkDefaultFont", 11))

        self.terms_of_use_screen = [ttk.Label(self, text="Terms Of Use",
                                              font=("TkDefaultFont", 27), wraplength=600), self.desc_label]

        self.terms_of_use_back = tk.Button(self, text="Back",
                                           command=lambda: self.change_screen(self.welcome_screen))
        self.terms_of_use_screen.append(self.terms_of_use_back)

        # Registration screen
        self.registration_view = registration.RegistrationView(self)
        self.registration_screen = [self.registration_view,
                                    tk.Button(self, text="Go to Login", command=lambda: self.change_screen(
                                        self.login_screen)),
                                    tk.Button(self, text="Back to Welcome Screen", command=lambda: self.change_screen(
                                        self.welcome_screen))
                                    ]

        # Login screen
        ####################################################################################
        self.Login_Manager = new_login.Login(self)
        self.login_screen = [self.Login_Manager]

        # Try to find a remembered user in the database. Otherwise, run the program in signed out mode
        username, password, message = database.get_remembered_user()
        user_dict, message = database.login(username, password)
        if message == 'Success':
            self.student_data = user_dict
            self.student_id = self.student_data['username']
            self.logged_in = True
        ####################################################################################
        self._update_selection_screen()

        # The math screen.
        self.m_s = ms.Math_Screen(self, '1-ADD')
        self.math_problems_screen = [self.m_s]

    def change_screen(self, new_screen):
        # This method runs when a bridging button (buttons that connect two views) is clicked.
        # It deletes all frames in the current view, and replaces them with all the frames in the new view.
        for item in self.current_screen:
            item.grid_forget()
        for item in new_screen:
            item.grid()
        self.current_screen = new_screen

    def set_user(self, student):
        self.student_data = student
        self.student_id = student['username']
        self.logged_in = True
        self._update_selection_screen()

    def _update_selection_screen(self):
        if self.logged_in:
            # Problem selection screen
            self.selection_view = ps.SelectionView(self, self, {'child_grade': int(self.student_data['child_grade']),
                                                                'username': self.student_data['username']}, self)
            # self.selection_view = self.Login_Manager.generate_problem_set(self)

            self.problem_selection_screen = [self.selection_view,
                                             tk.Button(self, text="Back to Home", command=lambda: self.change_screen(
                                                 self.welcome_screen))]
            # Enable the problem selection button
            self.problem_selection_button['state'] = 'normal'

            # Reports screen
            # Reset the reports screen when switching users
            self.reports_screen = [reports.ReportsFrame(self),
                                   tk.Button(self, text="Back", command=lambda:
                                   self.change_screen(self.welcome_screen))]
        else:
            # Disable the problem selection button
            self.problem_selection_button['state'] = 'disabled'

            # Remove the menu toolbar
            self.config(menu="")
            try:
                del self.selection_view
            except AttributeError:
                pass

    def log_out(self):
        database.forget_remembered_user()
        self.change_screen(self.welcome_screen)
        self.student_data = {}
        self.student_id = ''
        self.logged_in = False
        self._update_selection_screen()


if __name__ == '__main__':
    app = MyApplication()
    app.mainloop()
