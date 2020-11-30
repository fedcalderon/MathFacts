# Xade

import tkinter as tk
import tkinter as ttk
import  os
from src.application.views import login
from src.application.views import registration

class Page_Links(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.Time_label = tk.StringVar()
        self.Time_label.set("Time Left: #")

        Time_label = ttk.Label(self, textvariable=self.Time_label,
                               font=("TkDefaultFont", 10), wraplength=600)

        #Link buttons

        login_button = ttk.Button(self, text="Login", command= self.Login())
        register_button = ttk.Button(self, text="Register", command= self.Register())

        #Grid
        login_button.grid(row=3, column=2, sticky=(tk.E+tk.W))
        register_button.grid(row=4, column=2, sticky=(tk.E+tk.W))
        Time_label.grid(row=0, column=12, sticky=tk.E)

    def Login(self):
        if self.Login().get:
            os.system(login.py)
        else:
            exit()

    def Register(self):
        if self.register().get:
            os.system(registration.py)
        else:
            exit()

#if __name__ == '__main__':
#    root = tk.Tk()
#    root.title('Math Facts Practice')
#    root.resizable(width=False, height=False)
#    root.geometry('500x300')
#   Page_Links(root).pack(expand=True, fill='both')
#    root.mainloop()


    class test_screen_Settings(tk.Tk):
        """Screen settings"""

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.geometry("600x500")
            self.resizable(width=False, height=False)
            Page_Links(self).grid(sticky=(tk.E + tk.W + tk.N + tk.S))
            self.columnconfigure(0, weight=1)


    if __name__ == '__main__':
        app = test_screen_Settings()
        app.mainloop()