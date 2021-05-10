import tkinter as tk


class Dashboard(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, pady=20)
        # self.configure(bg="gold")
        tk.Label(parent, text="Dashboard", font=("", 25))
        # self.lbl.grid()
        self.btn=tk.Button(parent, text="Exit", font=("", 15))