import tkinter as tk
from tkinter import ttk


class LoginInformation(tk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent, text="Login Information", pady=20)
        #self.configure(bg="gold")

        self.Username = tk.StringVar()
        username_label = ttk.Label(self, text="Enter Username")
        username_button = ttk.Entry(self, textvariable=self.Username)
        username_label.grid(row=0, column=0, sticky=(tk.W))
        username_button.grid(row=100, column=0, sticky=(tk.W))

        self.Password = tk.StringVar()
        password_label = ttk.Label(self, text="Enter Password")
        password_button = ttk.Entry(self, textvariable=self.Password)
        password_label.grid(row=0, column=100, sticky=(tk.W))
        password_button.grid(row=100, column=100, sticky=(tk.W))

        self.PizzaSize = tk.StringVar()
        grade_label = ttk.Label(self, text="Pizza Size")
        grade_button = ttk.Combobox(self, width=27, textvariable=self.PizzaSize)

        grade_values = ["Preschool", "Kindergarten"]
        for x in range(1, 19): grade_values.append(str(x))
        grade_button['values'] = tuple(grade_values)

        grade_label.grid(row=600, column=200, sticky=tk.W)
        grade_button.grid(row=800, column=200, sticky=(tk.W + tk.E))