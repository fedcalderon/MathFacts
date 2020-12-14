from tkinter import *
import os
import tkinter as tk


# Designing window for login
def login():
    global login_screen
    login_screen = Tk()

    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").grid()
    Label(login_screen, text="").grid()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username * ").grid()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.grid()
    Label(login_screen, text="").grid()
    Label(login_screen, text="Password * ").grid()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.grid()
    Label(login_screen, text="").grid()
    Button(login_screen, text="login", width=10, height=1, command=login_verify).grid()

# Implementing event on login button
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()

        else:
            password_not_recognised()

    else:
        user_not_found()


# Designing popup for login success

def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="login Success").grid()
    Button(login_success_screen, text="OK", command=login_success_screen.destroy).grid()


# Designing popup for login invalid password

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Tk()
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").grid()
    Button(password_not_recog_screen, text="OK", command=password_not_recog_screen.destroy).grid()


# Designing popup for user not found

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").grid()
    Button(user_not_found_screen, text="OK", command=user_not_found_screen.destroy).grid()

# Designing Main(first) window

# def main_account_screen():
#     global main_screen
#     main_screen = Tk()
#     main_screen.geometry("300x250")
#     main_screen.title("Account login")
#     Label(text="Select Your Choice", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
#     Label(text="").pack()
#     Button(text="login", height="2", width="30", command=login).pack()
#     Label(text="").pack()
#     main_screen.mainloop()


class MainAccountScreen(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.login_label = Label(self, text="Select Your Choice", bg="blue", font=("Calibri", 30))
        self.login_label.grid(sticky=(tk.E + tk.W + tk.N + tk.S))
        self.login_button = Button(self, text="Login", height="2", width="30", command=login)
        self.login_button.grid(sticky=(tk.E + tk.W + tk.N + tk.S))

        # Label(text="Select Your Choice", bg="blue", width="300", height="2", font=("Calibri", 13)).grid()
        # Label(text="").grid()
        # Button(text="Login", height="2", width="30", command=login).grid()
        # Label(text="").grid()


class LoginSelectionWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("305x250")
        self.title("Account Login")
        MainAccountScreen(self).grid()


if __name__ == '__main__':
    selection_window = LoginSelectionWindow()
    selection_window.mainloop()
