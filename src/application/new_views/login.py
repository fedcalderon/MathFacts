import tkinter as tk
from tkinter import *
from tkinter import ttk

from src.application.models import database
from src.application.models import modified_logger as logger


# class problem_set:
#     def __init__(self, parent):
#         self.login_manager = Login(parent)
#         self.selection_view = self.login_manager.generate_problem_set()


class Login(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.main_app = parent
        self.username_verify = tk.StringVar()
        self.password_verify = tk.StringVar()
        self.username_login_entry = ttk.Entry(self, textvariable=self.username_verify)
        self.password_login_entry = ttk.Entry(self, textvariable=self.password_verify, show='*')
        self.remember_me = tk.BooleanVar()
        self.remember_checkbox = ttk.Checkbutton(self, text="Remember Me", variable=self.remember_me)
        self.result_message = ""
        self.student = {}
        self.student_id = None

        self.username1 = self.username_verify.get()
        self.password1 = self.password_verify.get()

        self.logged_in = False
        self.program_logger = logger.Logger('login_attempts.log')

        ttk.Label(self, text='Please enter details below to login').grid()
        ttk.Label(self, text='').grid()
        ttk.Label(self, text="Username").grid()
        self.username_login_entry.grid()
        ttk.Label(self, text="").grid()
        ttk.Label(self, text="Password").grid()
        self.password_login_entry.grid()
        ttk.Label(self, text="").grid()
        self.remember_checkbox.grid()
        ttk.Label(self, text="").grid()
        ttk.Button(self, text="Login", command=lambda: self.login_verify(parent)).grid()
        ttk.Label(self, text="").grid()
        ttk.Label(self, text="").grid()
        tk.Button(self, text="Back to Welcome Screen", command=lambda: parent.change_screen(
            parent.welcome_screen)).grid()

        self.username_login_entry.focus()

    # def generate_problem_set(self, parent):
    #     with open(f'{Path(__file__).parent.parent}\\student_data.json') as jsonfile:
    #         self.users_data = json.load(jsonfile)
    #         for key in self.users_data:
    #             if self.username1 == self.users_data[key]['username']:
    #                  if self.password1 == self.users_data[key]['password']:
    #                       self.student = self.users_data[key]
    #                       self.student_id = key
    #                       self.selection_view = ps.SelectionView(parent, self,
    #                                              {'child_grade': int(self.users_data[f'user 0']['child_grade']),
    #                                               'username': self.users_data[f'user 0']['username']}, self)
    #                       return self.selection_view

    def login_verify(self, parent):
        # TODO: FOR LOGIN VERIFY
        self.username1 = self.username_verify.get()
        self.password1 = self.password_verify.get()

        self.username_login_entry.delete(0, END)
        self.password_login_entry.delete(0, END)

        # Use the database to login
        student, message = database.login(self.username1, self.password1)
        if message == 'Success':
            self.student = student
            self.student_id = student['username']
            self.result_message = "Successfully logged in"
            self.program_logger.write_to_log(f"{self.username1}: Login Successful"
                                             f" - {self.program_logger.get_datetime_string()}")
            self.logged_in = True
            # Forget any user who might have been remembered
            database.forget_remembered_user()

            # If the user selected Remember Me, save them as the remembered user
            if self.remember_me.get():
                database.set_remembered_user(student['username'], self.password1)

            # Let the main app know about the user
            self.main_app.set_user(self.student)
        else:
            self.result_message = message
            self.program_logger.write_to_log(f"{self.username1}: Login Failed. "
                                             f"Cause: {message}. - {self.program_logger.get_datetime_string()}")

        self.result_of_verification(self.result_message, parent)

    def kill_everything(self, parent):
        self.login_success_screen.destroy()
        parent.change_screen(parent.problem_selection_screen)

    # Popup for login success/failure
    def result_of_verification(self, result_message, parent):
        self.result_message = result_message
        self.login_success_screen = Toplevel(self)
        self.login_success_screen.title("Login Result")
        self.login_success_screen.geometry("140x140")
        Label(self.login_success_screen, text=result_message).grid()

        # ok_button = Button(self.login_success_screen, text="OK", height="1", width="15",
        #                    command=self.login_success_screen.destroy)
        # ok_button.grid(sticky=(tk.E + tk.W + tk.N + tk.S))

        if result_message == "User not found":
            Label(self.login_success_screen, text="Do you want to register?").grid()
            Label(self.login_success_screen, text="").grid()
            ok = Button(self.login_success_screen, text="Register", height="1", width="15",
                        command=lambda: parent.change_screen(parent.registration_screen))
            ok.grid(sticky=(tk.E + tk.W + tk.N + tk.S))

        elif result_message == "Successfully logged in":
            ok_button = Button(self.login_success_screen, text="OK", height="1", width="15",
                               command=lambda: self.kill_everything(parent))
            ok_button.grid(sticky=(tk.E + tk.W + tk.N + tk.S))

        else:
            ok_button = Button(self.login_success_screen, text="No, go back.", height="1", width="15",
                               command=self.login_success_screen.destroy)
            ok_button.grid(sticky=(tk.E + tk.W + tk.N + tk.S))
