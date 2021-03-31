# User registration
# Asher
# ask for name, last name, age, grade, parents names, username, password

import tkinter as tk
from tkinter import ttk
import json
from pathlib import Path


class LoginInformation(tk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent, text="Login Information", pady=20)
        # self.configure(bg="gold")

        self.Username = tk.StringVar()
        self.username_label = ttk.Label(self, text="Enter Username")
        self.username_button = ttk.Entry(self, textvariable=self.Username)
        self.username_label.grid(row=0, column=0, sticky=(tk.W))
        self.username_button.grid(row=100, column=0, sticky=(tk.W))

        self.Password = tk.StringVar()
        self.password_label = ttk.Label(self, text="Enter Password")
        self.password_button = ttk.Entry(self, textvariable=self.Password, show='*')
        self.password_label.grid(row=0, column=100, sticky=(tk.W))
        self.password_button.grid(row=100, column=100, sticky=(tk.W))


class Guardian1Info(tk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent, text="Guardian 1:", pady=20)
        # self.configure(bg="gold")

        self.FirstName = tk.StringVar()
        self.first_name_label = ttk.Label(self, text="First Name")
        self.first_name_button = ttk.Entry(self, textvariable=self.FirstName)
        self.first_name_label.grid(row=0, column=0, sticky=(tk.W))
        self.first_name_button.grid(row=100, column=0, sticky=(tk.W))

        self.LastName = tk.StringVar()
        self.last_name_label = ttk.Label(self, text="Last Name")
        self.last_name_button = ttk.Entry(self, textvariable=self.LastName)
        self.last_name_label.grid(row=0, column=100, sticky=(tk.W))
        self.last_name_button.grid(row=100, column=100, sticky=(tk.W))


class Guardian2Info(tk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent, text="Guardian 2:", pady=20)
        # self.configure(bg="gold")

        self.FirstName = tk.StringVar()
        self.first_name_label = ttk.Label(self, text="First Name")
        self.first_name_button = ttk.Entry(self, textvariable=self.FirstName)
        self.first_name_label.grid(row=0, column=0, sticky=(tk.W))
        self.first_name_button.grid(row=100, column=0, sticky=(tk.W))

        self.LastName = tk.StringVar()
        self.last_name_label = ttk.Label(self, text="Last Name")
        self.last_name_button = ttk.Entry(self, textvariable=self.LastName)
        self.last_name_label.grid(row=0, column=100, sticky=(tk.W))
        self.last_name_button.grid(row=100, column=100, sticky=(tk.W))


class ChildInformation(tk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent, text="Child Information", pady=15)
        # self.configure(bg="gold")

        self.FirstName = tk.StringVar()
        self.first_name_label = ttk.Label(self, text="First Name")
        self.first_name_button = ttk.Entry(self, textvariable=self.FirstName)
        self.first_name_label.grid(row=0, column=0, sticky=(tk.W))
        self.first_name_button.grid(row=100, column=0, sticky=(tk.W))

        self.LastName = tk.StringVar()
        self.last_name_label = ttk.Label(self, text="Last Name")
        self.last_name_button = ttk.Entry(self, textvariable=self.LastName)
        self.last_name_label.grid(row=0, column=100, sticky=(tk.W))
        self.last_name_button.grid(row=100, column=100, sticky=(tk.W))

        self.Grade = tk.StringVar()
        self.grade_label = ttk.Label(self, text="Grade of Child")
        self.grade_button = ttk.Combobox(self, width=27, textvariable=self.Grade)
        self.grade_values = []
        for x in range(1, 8): self.grade_values.append(str(x))
        self.grade_button['values'] = tuple(self.grade_values)
        self.grade_label.grid(row=200, column=00, sticky=tk.W)
        self.grade_button.grid(row=300, column=00, sticky=(tk.W))

        self.Age = tk.StringVar()
        self.age_label = ttk.Label(self, text="Age of Child")
        self.age_button = ttk.Combobox(self, width=27, textvariable=self.Age)
        self.age_values = ["Under 5"]
        for x in range(5, 19): self.age_values.append(str(x))
        self.age_button['values'] = tuple(self.age_values)
        self.age_label.grid(row=200, column=100, sticky=tk.W)
        self.age_button.grid(row=300, column=100, sticky=(tk.W))


class RegistrationView(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, *kwargs)

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

        self.field_text = tk.StringVar()
        self.field = ttk.Label(self, textvariable=self.field_text,
                               font=("TkDefaultFont", 11), wraplength=600)
        self.field.grid(row=1400, column=0, sticky=tk.W)

        self.users_data_file = f'{Path(__file__).parent.parent}\\student_data.json'
        self.users_dict = self.get_users()

        # Read current users from file and set the correct index
        if self.users_dict.items() == 0:
            self.user_index = 0
        else:
            self.user_index = self.find_next_user_index()

    def get_users(self):
        try:
            # Load user data from the json file
            with open(self.users_data_file) as jsonfile:
                users_data = json.load(jsonfile)
            # print(users_data)
            return users_data
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            # No users have been saved yet, so return an empty dictionary
            return {}

    def find_next_user_index(self):
        # Find the highest user index so far
        highest_index = -1
        for key in self.users_dict.keys():
            user_index = int(key[5:])  # Substring just the number from "user ##"
            if user_index > highest_index:
                highest_index = user_index

        # The next user index will be 1 more than the previous highest index
        return highest_index + 1

    def reset_fields(self):
        # Clear the fields that likely wouldn't be the same for multiple users

        self.c.FirstName.set('')
        # Last name is not cleared
        self.c.Grade.set('')
        self.c.Age.set('')
        # Guardian details are not cleared
        self.l.Username.set('')
        self.l.Password.set('')

    def save(self):
        # self.user_count = self.user_count
        self.all_information = {
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

        # Make sure the username is unique
        for user in self.users_dict.values():
            if self.all_information['username'] == user['username']:
                self.field_text.set(f"Username '{user['username']}' is already taken")
                return

        for key in self.all_information:
            if key == "guardian_2_first_name" or key == "guardian_2_last_name":
                pass
            else:
                if self.all_information.get(key) == "":
                    self.field_text.set("Not all required fields have been answered")
                    break
            if key == "password":
                # Add new data to the users dictionary and save it all to the file
                self.users_dict[f'user {self.user_index}'] = self.all_information
                with open(self.users_data_file, 'w') as jsonfile:
                    json.dump(self.users_dict, jsonfile)

                self.user_index += 1

                self.field_text.set(f"User '{self.all_information['username']}' has been registered.")
                self.reset_fields()
