import tkinter as tk
from tkinter import ttk


class ContactInformation(tk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent, text="Contact Information", pady=30)

        self.FirstName = tk.StringVar()
        first_name_label = ttk.Label(self, text="First Name")
        first_name_button = ttk.Entry(self, textvariable=self.FirstName)
        first_name_label.grid(row=600, column=0, sticky=tk.W)
        first_name_button.grid(row=800, column=0, sticky=(tk.W + tk.E))

        self.Phone = tk.StringVar()
        phone_label = ttk.Label(self, text="Phone Number")
        phone_button = ttk.Entry(self, textvariable=self.Phone)
        phone_label.grid(row=600, column=100, sticky=tk.W)
        phone_button.grid(row=800, column=100, sticky=(tk.W + tk.E))