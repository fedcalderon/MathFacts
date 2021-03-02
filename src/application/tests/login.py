from tkinter import *
import os
import tkinter as tk
from src.application.views import registration
import src.application
import json
from pathlib import Path
from src.application.views import problem_selection


# Designing window for login

############################################################################################################
# REWORKED VERSION


class LoginScreen(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Login")
        self.geometry("230x250")
        Label(self, text='Please enter details below to login').grid()
        Label(self, text='').grid()

        self.username_verify = StringVar()
        self.password_verify = StringVar()

        Label(self, text="Username * ").grid(sticky=(tk.E + tk.W + tk.N + tk.S))
        self.username_login_entry = Entry(self, textvariable=self.username_verify)
        self.username_login_entry.grid(sticky=(tk.E + tk.W + tk.N + tk.S))
        Label(self, text="").grid(sticky=(tk.E + tk.W + tk.N + tk.S))
        Label(self, text="Password * ").grid(sticky=(tk.E + tk.W + tk.N + tk.S))
        self.password_login_entry = Entry(self, textvariable=self.password_verify, show='*')
        self.password_login_entry.grid(sticky=(tk.E + tk.W + tk.N + tk.S))
        Label(self, text="").grid(sticky=(tk.E + tk.W + tk.N + tk.S))
        Button(self, text="Login", width=10, height=1, command=self.login_verify).grid(
            sticky=(tk.E + tk.W + tk.N + tk.S))

        self.result_message = ""
        self.student = {}
        self.student_id = ''
        self.username1 = self.username_verify.get()
        self.password1 = self.password_verify.get()
        self.login_success_screen = Toplevel(self)

    def login_verify(self):
        # TODO: FOR LOGIN VERIFY
        # print(self.username1)
        # print(self.password1)

        self.username_login_entry.delete(0, END)
        self.password_login_entry.delete(0, END)

        # Replace Path call with os
        with open(f'{Path().absolute()}\student_data.json') as jsonfile:
            users_data = json.load(jsonfile)
            for key in users_data:
                # print(users_data[key]['username'])
                # print(users_data[key]['password'])
                # print(f"Username: {self.username1}")
                # print(f"Password: {self.password1}")
                if self.username1 == users_data[key]['username']:
                    if self.password1 == users_data[key]['password']:
                        self.student = users_data[key]
                        self.student_id = key
                        self.result_message = "Successfully logged in."
                        break

                    else:
                        self.result_message = "Password not recognized."
                        break

                else:
                    self.result_message = "User not found."

        self.result_of_verification(self.result_message)

    def open_registration(self, screen_to_destroy, screen_to_destroy_2):
        screen_to_destroy.destroy()
        screen_to_destroy_2.destroy()
        registration.MyApplication().mainloop()

    # Popup for login success/failure
    def result_of_verification(self, result_message):
        self.result_message = result_message

        self.login_success_screen.title("Login Result")
        self.login_success_screen.geometry("140x140")
        Label(self.login_success_screen, text=result_message).grid()

        # ok_button = Button(self.login_success_screen, text="OK", height="1", width="15",
        #                    command=self.login_success_screen.destroy)
        # ok_button.grid(sticky=(tk.E + tk.W + tk.N + tk.S))

        if result_message == "User not found.":
            Label(self.login_success_screen, text="Do you want to register?").grid()
            Label(self.login_success_screen, text="").grid()
            Button(self.login_success_screen, text="Register", height="1", width="15",
                   command=lambda: self.open_registration(self.login_success_screen, self)).grid(
                sticky=(tk.E + tk.W + tk.N + tk.S))

        if result_message == "Successfully logged in.":
            ok_button = Button(self.login_success_screen, text="OK", height="1", width="15",
                               command=self.kill_everything)
            ok_button.grid(sticky=(tk.E + tk.W + tk.N + tk.S))

        else:
            ok_button = Button(self.login_success_screen, text="No, go back.", height="1", width="15",
                               command=self.login_success_screen.destroy)
            ok_button.grid(sticky=(tk.E + tk.W + tk.N + tk.S))

    def kill_everything(self):
        self.login_success_screen.destroy()
        self.destroy()
        problem_selection.run_problem_selection(self.student_id, self.student)



############################################################################################


def login_verify(self):
    # TODO: FOR LOGIN VERIFY
    self.username1 = self.username_verify.get()
    self.password1 = self.password_verify.get()

    # print(self.username1)
    # print(self.password1)

    self.username_login_entry.delete(0, END)
    self.password_login_entry.delete(0, END)

    # Replace Path call with os
    with open(f'{Path().absolute()}\student_data.json') as jsonfile:
        users_data = json.load(jsonfile)
        for key in users_data:
            # print(users_data[key]['username'])
            # print(users_data[key]['password'])
            # print(f"Username: {self.username1}")
            # print(f"Password: {self.password1}")
            if self.username1 == users_data[key]['username']:
                if self.password1 == users_data[key]['password']:
                    self.student = users_data[key]
                    self.student_id = key
                    self.result_message = "Successfully logged in."
                    break

                else:
                    self.result_message = "Password not recognized."
                    break

            else:
                self.result_message = "User not found."

    result_of_verification(self, self.result_message)


def open_registration(self, screen_to_destroy, screen_to_destroy_2):
    screen_to_destroy.destroy()
    screen_to_destroy_2.destroy()
    registration.MyApplication().mainloop()


# Popup for login success/failure

def kill_everything(self):
    self.login_success_screen.destroy()
    self.destroy()
    problem_selection.run_problem_selection(self.student_id, self.student)


def result_of_verification(self, result_message):
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
        Button(self.login_success_screen, text="Register", height="1", width="15",
               command=lambda: self.open_registration(self.login_success_screen, self)).grid(
            sticky=(tk.E + tk.W + tk.N + tk.S))

    if result_message == "Successfully logged in.":
        ok_button = Button(self.login_success_screen, text="OK", height="1", width="15",
                           command=self.kill_everything)
        ok_button.grid(sticky=(tk.E + tk.W + tk.N + tk.S))

    else:
        ok_button = Button(self.login_success_screen, text="No, go back.", height="1", width="15",
                           command=self.login_success_screen.destroy)
        ok_button.grid(sticky=(tk.E + tk.W + tk.N + tk.S))
if __name__ == '__main__':
    login_window = LoginScreen()
    login_window.mainloop()

