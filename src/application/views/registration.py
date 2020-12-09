# User registration
# Asher
# ask for name, last name, age, grade, parents names, username, password

import tkinter as tk
from tkinter import ttk
import json
import src.application
import os
from pathlib import Path


class LoginInformation(tk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent, text="login Information", pady=20)
        # self.configure(bg="gold")

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


class Guardian1Info(tk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent, text="Guardian 1:", pady=20)
        # self.configure(bg="gold")

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
        # self.configure(bg="gold")

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


class ChildInformation(tk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent, text="Child Information", pady=15)
        # self.configure(bg="gold")

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

        self.Grade = tk.StringVar()
        grade_label = ttk.Label(self, text="Grade of Child")
        grade_button = ttk.Combobox(self, width=27, textvariable=self.Grade)
        grade_values = ["Preschool", "Kindergarten"]
        for x in range(1, 19): grade_values.append(str(x))
        grade_button['values'] = tuple(grade_values)
        grade_label.grid(row=200, column=00, sticky=tk.W)
        grade_button.grid(row=300, column=00, sticky=(tk.W))

        self.Age = tk.StringVar()
        age_label = ttk.Label(self, text="Age of Child")
        age_button = ttk.Combobox(self, width=27, textvariable=self.Age)
        age_values = ["Under 5"]
        for x in range(5, 19): age_values.append(str(x))
        age_button['values'] = tuple(age_values)
        age_label.grid(row=200, column=100, sticky=tk.W)
        age_button.grid(row=300, column=100, sticky=(tk.W))


class MyApplication(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("MathFacts")
        self.geometry("800x650")
        # self.configure(bg="gold")

        # background_image = tk.PhotoImage('Pizza.png')
        # background_label = tk.Label(self, image=background_image)
        # background_label.image = background_image
        # background_label.place(x=0, y=0, relwidth=2, relheight=2)

        self.resizable(width=True, height=True)
        self.Main_Label = ttk.Label(self, text="Signup for MathFacts", font=("TkDefaultFont", 27), wraplength=600)
        self.Main_Label.grid(row=0, column=0, sticky=tk.W)

        self.c = ChildInformation(self)
        self.c.grid(sticky=(tk.E + tk.W + tk.N + tk.S))

        self.g1 = Guardian1Info(self)
        self.g1.grid(sticky=(tk.E + tk.W + tk.N + tk.S))

        self.g2 = Guardian2Info(self)
        self.g2.grid(sticky=(tk.E + tk.W + tk.N + tk.S))

        self.l = LoginInformation(self)
        self.l.grid(sticky=(tk.E + tk.W + tk.N + tk.S))

        self.Save = ttk.Button(self, text="Save", command=self.save)
        self.Save.grid(row=1200, column=0, sticky=tk.W)

        self.columnconfigure(0, weight=1)

        self.user_count = 0
        self.users_list = []

        #
        #self.users_data_file = r'views_data\users.json'
        self.users_data_file = f'{Path().absolute().parent}\student_data.json'

    def save(self):
        self.user_count = self.user_count
        all_information = {
            "child_first_name": self.c.FirstName.get(),
            "child_last_name": self.c.LastName.get(),
            "child_grade": self.c.Grade.get(),
            "child_age": self.c.Age.get(),

            "guardian_1_first_name": self.g1.FirstName.get(),
            "guardian_1_last_name": self.g1.LastName.get(),

            "guardian_2_first_name": self.g2.FirstName.get(),
            "guardian_2_last_name": self.g2.LastName.get(),

            "username": self.l.Username.get(),
            "password": self.l.Password.get(),
        }

        for key in all_information:
            if key == "guardian_2_first_name" or key == "guardian_2_last_name":
                pass

            else:
                if (all_information.get(key) == ""):
                    self.field = ttk.Label(self, text="Not all required fields have been answered"
                                           , font=("TkDefaultFont", 10), wraplength=600)
                    self.field.grid(row=1400, column=0, sticky=tk.W)
                    break

            if key == "password":

                print(self.user_count)
                self.field = ttk.Label(self, text="          "
                                                  "                   "
                                                  "                   "
                                                  "                   "
                                                  "                   ", font=("TkDefaultFont", 10), wraplength=600)
                self.field.grid(row=1400, column=0, sticky=tk.W)

                # with open(r'users.json', 'w') as jsonfile:
                #     json.dump({f"user {self.user_count}": all_information}, jsonfile)

                with open(self.users_data_file, 'w') as jsonfile:
                    json.dump({f"user {self.user_count}": all_information}, jsonfile)

                with open(self.users_data_file) as jsonfile:
                    users_data = json.load(jsonfile)

                self.user_count = self.user_count + 1
                self.users_list.append(users_data)

                all_users = {}
                for user in self.users_list:
                    for key in user:
                        all_users.update({key : user[key]})

                with open(self.users_data_file, 'w') as jsonfile:
                    json.dump(all_users, jsonfile)
    #def write_to_users_file(self):


if __name__ == "__main__":
    app = MyApplication()
    app.mainloop()