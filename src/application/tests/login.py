from tkinter import *
import os
import tkinter as tk
from src.application.views import registration
import src.application
import json
from pathlib import Path
from src.application.views import problem_selection as ps


# Designing window for login

def set_student_id(self):
    with open(f'{Path(__file__).parent.parent}\\student_data.json') as jsonfile:
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
                    print(self.student_id)
                    return self.student_id


def login_verify(self):
    # TODO: FOR LOGIN VERIFY
    self.username1 = self.username_verify.get()
    self.password1 = self.password_verify.get()

    self.username_login_entry.delete(0, END)
    self.password_login_entry.delete(0, END)

    # Replace Path call with os
    with open(f'{Path(__file__).parent.parent}\\student_data.json') as jsonfile:
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
                    #print(self.student_id)
                    self.result_message = "Successfully logged in."

                    # problem selection screen
                    break

                else:
                    self.result_message = "Password not recognized."
                    break

            else:
                self.result_message = "User not found."

    result_of_verification(self, self.result_message)

#def selection_view():


def open_registration(self, screen_to_destroy, screen_to_destroy_2):
    screen_to_destroy.destroy()
    screen_to_destroy_2.destroy()
    registration.MyApplication().mainloop()


# Popup for login success/failure
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
        ok = Button(self.login_success_screen, text="Register", height="1", width="15",
            command=lambda: self.change_screen(self.login_screen, self.registration_screen))
        ok.grid(sticky=(tk.E + tk.W + tk.N + tk.S))

    elif result_message == "Successfully logged in.":
        ok_button = Button(self.login_success_screen, text="OK", height="1", width="15",
                           command=lambda: kill_everything(self))
        ok_button.grid(sticky=(tk.E + tk.W + tk.N + tk.S))

    else:
        ok_button = Button(self.login_success_screen, text="No, go back.", height="1", width="15",
                           command=self.login_success_screen.destroy)
        ok_button.grid(sticky=(tk.E + tk.W + tk.N + tk.S))


def kill_everything(self):
    self.login_success_screen.destroy()
    self.change_screen(self.login_screen, self.problem_selection_screen)
