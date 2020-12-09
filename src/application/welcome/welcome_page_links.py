# Xade

import tkinter as tk
import tkinter as ttk
#from src.application.views.registration import
from src.application.views.login import login
import os
import time
from src.application.welcome.terms_of_use import TermsOfUseWindow

class LinksFrame(tk.Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        # Frame with button links(right now only terms of use)
        self.terms_of_use_link = ttk.Button(self, text="Terms Of Use", command=self.terms_of_use_open)

        login_button = ttk.Button(self, text="login", command=self.Login_start)
        #register_button = ttk.Button(self, text="Register", command=self.Register_start)
        self.terms_of_use_link.grid(row=100, column=0, sticky=tk.W)
        login_button.grid(row=99, column=100, sticky=(tk.E + tk.W + tk.S + tk.N))
        #register_button.grid(row=100, column=100, sticky=(tk.E + tk.W + tk.S + tk.N))

    def terms_of_use_open(self):
        # Terms of use window
        root = tk.Tk()
        root.title('Terms Of Use')
        root.resizable(width=False, height=False)
        root.geometry('340x120')
        TermsOfUseWindow(root).pack(expand=True, fill='both')
        root.mainloop()

    def Login_start(self):
        login()
        exit()

   # def Register_start(self):
    #    registration()
    #    exit()


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Math Facts Practice')
    root.resizable(width=False, height=False)
    root.geometry('500x300')
    LinksFrame(root).pack(expand=True, fill='both')
    root.mainloop()
