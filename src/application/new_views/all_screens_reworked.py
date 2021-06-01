# This is a work in progress. This keeps all the screens in a single window.
# The major difference between this and the current program is that all the screens are contained in lists rather than
#   tk windows.

import tkinter as tk
from tkinter import ttk

from src.application.new_views import login
import src.application.new_views.problem_selection as ps
from src.application.new_views import registration
import src.application.new_views.math_screen as ms
from src.application.new_views import settings
from src.application.new_views import welcome
from src.application.new_views import reports
from src.application.new_views import dashboard
from src.application.models import database
from src.application.new_views import results
from datetime import datetime
import src.application.models.modified_logger as logger


class MyApplication(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("MathFacts")
        self.geometry("1000x700")
        self.resizable(width=True, height=True)

        self.welcome_screen = welcome.WelcomeFrame(self)
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
        # Andrew: Moved buttons to their respective screens so that each screen is just a frame, not a list

        # self.welcome_screen.extend([self.terms_of_use_button, self.registration_button,
        #                             self.login_button, self.problem_selection_button, self.dashboard_button])

        # for item in self.welcome_screen:
        #     item.grid()
        self.welcome_screen.pack()

        # Dashboard Screen
        self.dashboard_screen = dashboard.Dashboard(self)

        # Reports screen
        self.reports_screen = reports.ReportsFrame(self)

        # Terms of use screen
        self.terms_of_use_screen = welcome.TermsOfUse(self)

        # Registration screen
        self.registration_screen = registration.RegistrationView(self)

        # Login screen
        ####################################################################################
        self.login_screen = login.Login(self)

        # Try to find a remembered user in the database. Otherwise, run the program in signed out mode
        username, password, message = database.get_remembered_user()
        user_dict, message = database.login(username, password)
        if message == 'Success':
            self.student_data = user_dict
            self.student_id = self.student_data['username']
            self.logged_in = True
        ####################################################################################
        self._update_user_screens()

        # The math screen.
        self.math_problems_screen = ms.Math_Screen(self, '1-ADD')

    def change_screen(self, new_screen):
        # This method runs when a bridging button (buttons that connect two views) is clicked.
        # It deletes all frames in the current view, and replaces them with all the frames in the new view.
        # for item in self.current_screen:
        #     item.grid_forget()
        # for item in new_screen:
        #     item.grid()
        self.current_screen.pack_forget()
        if type(new_screen) == results.LinksFrame:
            new_screen.pack(fill='both', expand=True)
        else:
            new_screen.pack(fill='y', expand=True)
        self.current_screen = new_screen

    def set_user(self, student):
        self.student_data = student
        self.student_id = student['username']
        self.logged_in = True
        self._update_user_screens()

    def _update_user_screens(self):
        if self.logged_in:
            # Problem selection screen
            self.selection_view = ps.SelectionView(self, self, {'child_grade': int(self.student_data['child_grade']),
                                                                'username': self.student_data['username']}, self)
            # self.selection_view = self.Login_Manager.generate_problem_set(self)

            self.problem_selection_screen = self.selection_view
            # Enable the problem selection button
            self.welcome_screen.problem_selection_button['state'] = 'normal'

            # Reports screen
            # Reset the reports screen when switching users
            self.reports_screen = reports.ReportsFrame(self)

            # Settings screen
            self.settings_screen = settings.SettingsFrame(self)
        else:
            # Disable the problem selection button
            self.welcome_screen.problem_selection_button['state'] = 'disabled'

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
        self._update_user_screens()


if __name__ == '__main__':
    app = MyApplication()
    app.mainloop()
