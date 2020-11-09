# User login
# Micah

from tkinter import *

def main_account_screen():
    main_screen = Tk()  # create a GUI window
    main_screen.geometry("300x250")  # set the configuration of GUI window
    main_screen.title("Account Login")  # set the title of GUI window

main_account_screen()
global main_screen
main_screen.mainloop()  # start

Label(text="Choose Login or Register", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
Label(text="").pack()

# Login Button
Button(text="Login", height="2", width="30").pack()
Label(text="").pack()


def login_verify():
    # get username and password

    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)


    list_of_files = os.listdir()

    if username1 in list_of_files:
        file1 = open(username1, "r")  # open the file in read mode


        verify = file1.read().splitlines()
        login_sucess()

    else:
        password_not_recognised()

        else:
            user_not_found()



def login_sucess():
    global login_success_screen  # make login_success_screen global
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()

    # create OK button
    Button(login_success_screen, text="OK", command=delete_login_success).pack()

def delete_login_success():
    login_success_screen.destroy()

#password
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")a
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()

def delete_password_not_recognised():
    password_not_recog_screen.destroy()

#username
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()

def delete_user_not_found_screen():
    user_not_found_screen.destroy()