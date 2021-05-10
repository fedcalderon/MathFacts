import tkinter as tk



# self.configure(bg="gold")

class Dashboard(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, pady=20)
        # self.configure(bg="gold")
        self.lbl=tk.Label(parent,text="Dashboard", font=("", 25))
        self.lbl.place(x=80,y=100)
        self.btn=tk.Button(parent, text="Exit", font=("", 15))
        self.btn.place(x=35,y=20)


