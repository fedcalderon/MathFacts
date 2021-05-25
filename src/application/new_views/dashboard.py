import tkinter as tk


class Dashboard(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, pady=20)
        # self.configure(bg="gold")
        tk.Label(self, text="Dashboard", font=("", 25)).grid()
        tk.Button(self, text="Back", font=("", 15), command=lambda: parent.change_screen(parent.welcome_screen)).grid()
