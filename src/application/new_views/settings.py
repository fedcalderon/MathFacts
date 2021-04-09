import tkinter as tk
from tkinter import ttk
import json
from pathlib import Path
from src.application.new_views import registration as r


class SettingsFrame(tk.Frame):
    """Contains and displays the description of the Math Facts Practice application."""
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        self.users_data_file = f'{Path(__file__).parent.parent}\\student_data.json'
        with open(self.users_data_file) as jsonfile:
            users_data = json.load(jsonfile)

        self.users_data = users_data

        self.Main_Label = ttk.Label(self, text="User Settings", font=("TkDefaultFont", 27), wraplength=600)
        self.Main_Label.grid(row=0, column=0, sticky=tk.W)

        self.c = r.ChildInformation(self)
        self.c.grid(sticky=(tk.E + tk.W + tk.N + tk.S))
        self.c.first_name_button.insert(0, self.users_data['user 0']['child_first_name'])
        self.c.last_name_button.insert(0, self.users_data['user 0']['child_last_name'])
        self.c.grade_button.insert(0, self.users_data['user 0']['child_grade'])
        self.c.age_button.insert(0, self.users_data['user 0']['child_age'])

        self.g1 = r.Guardian1Info(self)
        self.g1.grid(sticky=(tk.E + tk.W + tk.N + tk.S))
        self.g1.first_name_button.insert(0, self.users_data['user 0']['guardian_1_first_name'])
        self.g1.last_name_button.insert(0, self.users_data['user 0']['guardian_1_last_name'])

        self.g2 = r.Guardian1Info(self)
        self.g2.grid(sticky=(tk.E + tk.W + tk.N + tk.S))
        self.g2.first_name_button.insert(0, self.users_data['user 0']['guardian_2_first_name'])
        self.g2.last_name_button.insert(0, self.users_data['user 0']['guardian_2_last_name'])

        self.Save = ttk.Button(self, text="Save", command=self.save)
        self.Save.grid(row=1200, column=0, sticky=tk.W)

    def save(self):

        self.all_information = {
            "child_first_name": self.c.FirstName.get(),
            "child_last_name": self.c.LastName.get(),
            "child_grade": self.c.Grade.get(),
            "child_age": self.c.Age.get(),

            "guardian_1_first_name": self.g1.FirstName.get(),
            "guardian_1_last_name": self.g1.LastName.get(),

            "guardian_2_first_name": self.g2.FirstName.get(),
            "guardian_2_last_name": self.g2.LastName.get(),

            "username": self.users_data['user 0']['username'],
            "password": self.users_data['user 0']['password']
        }

        self.users_data['user 0'] = self.all_information
        print(self.users_data)

        with open(self.users_data_file, 'w') as jsonfile:
            json.dump(self.users_data, jsonfile)
