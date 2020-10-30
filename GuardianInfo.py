import tkinter as tk
from tkinter import ttk


class Guardian1Info(tk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent, text="Guardian 1:", pady=20)
        #self.configure(bg="gold")

        self.FirstName = tk.StringVar()
        first_name_label = ttk.Label(self, text="First Name")
        first_name_button = ttk.Entry(self, textvariable=self.FirstName)
        first_name_label.grid(row=0, column=0, sticky=(tk.W))
        first_name_button.grid(row=100, column=0, sticky=(tk.W))

        self.LastName = tk.StringVar()
        last_name_label = ttk.Label(self, text="Last Name")
        last_name_button = ttk.Entry(self, textvariable=self.LastName)
        last_name_label.grid(row=0, column=100, sticky=(tk.W))
        last_name_button.grid(row=100, column=100, sticky=(tk.W))


class Guardian2Info(tk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent, text="Guardian 2:", pady=20)
        #self.configure(bg="gold")

        self.FirstName = tk.StringVar()
        first_name_label = ttk.Label(self, text="First Name")
        first_name_button = ttk.Entry(self, textvariable=self.FirstName)
        first_name_label.grid(row=0, column=0, sticky=(tk.W))
        first_name_button.grid(row=100, column=0, sticky=(tk.W))

        self.LastName = tk.StringVar()
        last_name_label = ttk.Label(self, text="Last Name")
        last_name_button = ttk.Entry(self, textvariable=self.LastName)
        last_name_label.grid(row=0, column=100, sticky=(tk.W))
        last_name_button.grid(row=100, column=100, sticky=(tk.W))