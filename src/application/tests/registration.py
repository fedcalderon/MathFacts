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
        self.Main_Label.grid(row=0, column=0, sticky=(tk.W))

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

        self.is_saved = False

        self.columnconfigure(0, weight=1)

        # self.users_data_file = registration'views_data\users.json'
        # self.users_data_file = f'{Path().absolute()}\student_data.json'
        self.users_data_file = f'{Path(__file__).parent.parent}\\student_data.json'
        # self.users_data_file = f'{os.path.normpath(os.path.join(os.path.dirname( __file__ ), os.pardir))}\student_data.json'

        # Read current users from file and set the correct index
        self.users_dict = self.get_users()
        if self.users_dict.items() == 0:
            self.user_index = 0
        else:
            self.user_index = self.find_next_user_index()

    def get_users(self):
        try:
            # Load user data from the json file
            with open(self.users_data_file) as jsonfile:
                users_data = json.load(jsonfile)
            print(users_data)
            return users_data
        except FileNotFoundError:
            # No users have been saved yet, so return an empty dictionary
            return {}

    def find_next_user_index(self):
        # Keep track of the highest user index so far
        highest_index = -1
        for key in self.users_dict.keys():
            user_index = int(key[5:])  # Substring just the number from "user ##"
            if user_index > highest_index:
                highest_index = user_index

        # The next user index will be 1 more than the previous highest index
        return highest_index + 1

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

        for key in self.all_information:
            if key == "guardian_2_first_name" or key == "guardian_2_last_name":
                pass

            else:
                if self.all_information.get(key) == "":
                    self.field = ttk.Label(self, text="Not all required fields have been answered"
                                           , font=("TkDefaultFont", 10), wraplength=600)
                    self.field.grid(row=1400, column=0, sticky=tk.W)
                    break

            if key == "password":

                # print(self.user_count)
                self.field = ttk.Label(self, text="          "
                                                  "                   "
                                                  "                   "
                                                  "                   "
                                                  "                   ", font=("TkDefaultFont", 10), wraplength=600)
                self.field.grid(row=1400, column=0, sticky=tk.W)

                # with open(registration'users.json', 'w') as jsonfile:
                #     json.dump({f"user {self.user_count}": all_information}, jsonfile)

                # Add new data to the users dictionary and save it all to the file
                self.users_dict[f'user {self.user_index}'] = self.all_information
                with open(self.users_data_file, 'w') as jsonfile:
                    json.dump(self.users_dict, jsonfile)

                #with open(self.users_data_file) as jsonfile:
                #    users_data = json.load(jsonfile)

                self.user_index += 1
                #self.users_list.append(users_data)

                #self.all_users = {}
                #for user in self.users_list:
                #    for key in user:
                #        self.all_users.update({key : user[key]})

                # print({list(self.all_users)[-1]: list(self.all_users.keys())[-1]})

                # with open(self.users_data_file, 'a') as jsonfile:
                #     json.dump(list(self.all_users)[-1], jsonfile)

                self.destroy()
                self.is_saved = True


if __name__ == "__main__":
    app = MyApplication()
    app.mainloop()
