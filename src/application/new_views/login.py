from tkinter import *
import os
import tkinter as tk
from src.application.new_views import registration
import src.application
import json
from pathlib import Path
from src.application.new_views import problem_selection as ps


# Designing window for login
class problem_set:
    def __init__(self, parent):
        self.login_manager = Login(parent)
        self.selection_view = self.login_manager.generate_problem_set()


class Login(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.username_verify = tk.StringVar()
        self.password_verify = tk.StringVar()
        self.username_login_entry = tk.Entry(self, textvariable=self.username_verify)
        self.password_login_entry = tk.Entry(self, textvariable=self.password_verify, show='*')
        self.result_message = ""
        self.student = {}

        self.username1 = self.username_verify.get()
        self.password1 = self.password_verify.get()

        self.selection_view = self.generate_problem_set()

        tk.Label(self, text='Please enter details below to login').grid()
        tk.Label(self, text='').grid()
        tk.Label(self, text="Username * ").grid()
        self.username_login_entry.grid()
        tk.Label(self, text="").grid()
        tk.Label(self, text="Password * ").grid()
        self.password_login_entry.grid()
        tk.Label(self, text="").grid()
        tk.Button(self, text="Login", width=10, height=1, command=
        lambda: self.login_verify(parent)).grid()
        tk.Label(self, text="").grid()
        tk.Label(self, text="").grid()
        tk.Button(self, text="Back to Welcome Screen", command=lambda: parent.change_screen(
            parent.login_screen, parent.welcome_screen)).grid()

    def generate_problem_set(self):
        with open(f'{Path(__file__).parent.parent}\\student_data.json') as jsonfile:
            self.users_data = json.load(jsonfile)
            for key in self.users_data:
                if self.username1 == self.users_data[key]['username']:
                    if self.password1 == self.users_data[key]['password']:
                        self.student = self.users_data[key]
                        self.student_id = key
                        selection_view = ps.SelectionView(self, self,
                                               {'child_grade': int(self.users_data[f'user 0']['child_grade']),
                                                'username': self.users_data[f'user 0']['username']}, self)

                        return selection_view

    def login_verify(self, parent):
        # TODO: FOR LOGIN VERIFY
        self.username1 = self.username_verify.get()
        self.password1 = self.password_verify.get()

        self.username_login_entry.delete(0, END)
        self.password_login_entry.delete(0, END)

        # Replace Path call with os
        with open(f'{Path(__file__).parent.parent}\\student_data.json') as jsonfile:
            self.users_data = json.load(jsonfile)
            for key in self.users_data:
                # print(users_data[key]['username'])
                # print(users_data[key]['password'])
                # print(f"Username: {self.username1}")
                # print(f"Password: {self.password1}")
                if self.username1 == self.users_data[key]['username']:
                    if self.password1 == self.users_data[key]['password']:
                        self.student = self.users_data[key]
                        self.student_id = key
                        # print(self.student_id)
                        self.result_message = "Successfully logged in."

                        # problem selection screen
                        break

                    else:
                        self.result_message = "Password not recognized."
                        break

                else:
                    self.result_message = "User not found."

        self.result_of_verification(self.result_message, parent)

    def kill_everything(self, parent):
        self.login_success_screen.destroy()
        parent.change_screen(parent.login_screen, parent.problem_selection_screen)

    def open_registration(self, screen_to_destroy, screen_to_destroy_2):
        screen_to_destroy.destroy()
        screen_to_destroy_2.destroy()
        registration.MyApplication().mainloop()

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

        if result_message == "User not found.":
            Label(self.login_success_screen, text="Do you want to register?").grid()
            Label(self.login_success_screen, text="").grid()
            ok = Button(self.login_success_screen, text="Register", height="1", width="15",
                        command=lambda: parent.change_screen(parent.login_screen, parent.registration_screen))
            ok.grid(sticky=(tk.E + tk.W + tk.N + tk.S))

        elif result_message == "Successfully logged in.":
            ok_button = Button(self.login_success_screen, text="OK", height="1", width="15",
                               command=lambda: self.kill_everything(parent))
            ok_button.grid(sticky=(tk.E + tk.W + tk.N + tk.S))

        else:
            ok_button = Button(self.login_success_screen, text="No, go back.", height="1", width="15",
                               command=self.login_success_screen.destroy)
            ok_button.grid(sticky=(tk.E + tk.W + tk.N + tk.S))

