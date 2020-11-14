# Micah
from tkinter import *
import os

# Designing welcome screen

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("1000x800")
    main_screen.title("MathFacts")
    main_screen.configure(background='yellow')
    Label(text="Welcome to MathFacts!", bg="blue", width="300", height="2", font=("Calibri", 25)).pack()
    Label(text="").pack()


    main_screen.mainloop()


main_account_screen()
