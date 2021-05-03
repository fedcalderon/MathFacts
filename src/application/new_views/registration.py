# User registration
# Asher
# ask for name, last name, age, grade, parents names, username, password

import tkinter as tk
from tkinter import ttk

import src.application.models.modified_logger as logger
from src.application.models import database


class LoginInformation(tk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent, text="Login Information", pady=20)
        # self.configure(bg="gold")

        self.Username = tk.StringVar()
        self.username_label = ttk.Label(self, text="Enter Username")
        self.username_entry = ttk.Entry(self, textvariable=self.Username)
        self.username_label.grid(row=0, column=0, padx=10, sticky=tk.W)
        self.username_entry.grid(row=100, column=0, padx=10, sticky=tk.W)

        self.Password = tk.StringVar()
        self.password_label = ttk.Label(self, text="Enter Password")
        self.password_entry = ttk.Entry(self, textvariable=self.Password, show='*')
        self.password_label.grid(row=0, column=100, padx=10, sticky=tk.W)
        self.password_entry.grid(row=100, column=100, padx=10, sticky=tk.W)


class Guardian1Info(tk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent, text="Guardian 1:", pady=20)
        # self.configure(bg="gold")

        self.FirstName = tk.StringVar()
        self.first_name_label = ttk.Label(self, text="First Name")
        self.first_name_entry = ttk.Entry(self, textvariable=self.FirstName)
        self.first_name_label.grid(row=0, column=0, padx=10, sticky=tk.W)
        self.first_name_entry.grid(row=100, column=0, padx=10, sticky=tk.W)

        self.LastName = tk.StringVar()
        self.last_name_label = ttk.Label(self, text="Last Name")
        self.last_name_entry = ttk.Entry(self, textvariable=self.LastName)
        self.last_name_label.grid(row=0, column=100, padx=10, sticky=tk.W)
        self.last_name_entry.grid(row=100, column=100, padx=10, sticky=tk.W)


class Guardian2Info(tk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent, text="Guardian 2:", pady=20)
        # self.configure(bg="gold")

        self.FirstName = tk.StringVar()
        self.first_name_label = ttk.Label(self, text="First Name")
        self.first_name_entry = ttk.Entry(self, textvariable=self.FirstName)
        self.first_name_label.grid(row=0, column=0, padx=10, sticky=tk.W)
        self.first_name_entry.grid(row=100, column=0, padx=10, sticky=tk.W)

        self.LastName = tk.StringVar()
        self.last_name_label = ttk.Label(self, text="Last Name")
        self.last_name_entry = ttk.Entry(self, textvariable=self.LastName)
        self.last_name_label.grid(row=0, column=100, padx=10, sticky=tk.W)
        self.last_name_entry.grid(row=100, column=100, padx=10, sticky=tk.W)


class ChildInformation(tk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent, text="Child Information", pady=15)
        # self.configure(bg="gold")

        self.FirstName = tk.StringVar()
        self.first_name_label = ttk.Label(self, text="First Name")
        self.first_name_entry = ttk.Entry(self, textvariable=self.FirstName)
        self.first_name_label.grid(row=0, column=0, padx=10, sticky=tk.W)
        self.first_name_entry.grid(row=100, column=0, padx=10, sticky=tk.W)

        self.LastName = tk.StringVar()
        self.last_name_label = ttk.Label(self, text="Last Name")
        self.last_name_entry = ttk.Entry(self, textvariable=self.LastName)
        self.last_name_label.grid(row=0, column=100, padx=10, sticky=tk.W)
        self.last_name_entry.grid(row=100, column=100, padx=10, sticky=tk.W)

        self.Grade = tk.StringVar()
        self.grade_label = ttk.Label(self, text="Grade of Child")
        self.grade_entry = ttk.Combobox(self, width=10, textvariable=self.Grade)
        self.grade_values = []
        for x in range(1, 8): self.grade_values.append(str(x))
        self.grade_entry['values'] = tuple(self.grade_values)
        self.grade_label.grid(row=200, column=00, padx=10, sticky=tk.W)
        self.grade_entry.grid(row=300, column=00, padx=10, sticky=tk.W)

        self.Age = tk.StringVar()
        self.age_label = ttk.Label(self, text="Age of Child")
        self.age_entry = ttk.Combobox(self, width=10, textvariable=self.Age)
        # self.age_values = ["Under 5"]
        self.age_values = []
        for x in range(4, 19): self.age_values.append(str(x))
        self.age_entry['values'] = tuple(self.age_values)
        self.age_label.grid(row=200, column=100, padx=10, sticky=tk.W)
        self.age_entry.grid(row=300, column=100, padx=10, sticky=tk.W)


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

        self.logger = logger.Logger('registration_attempts.log')

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
                if all_information.get(key) == "":
                    self.field_text.set("Not all required fields have been answered")
                    self.logger.write_to_log(f"Registration for user '{all_information['username']}' has failed. "
                                             f"Cause: Not all required fields have been answered. "
                                             f"{self.logger.get_datetime_string()}")
                    break
            if key == "password":
                # Add the new user to the database
                message = database.add_user(all_information)
                if message == 'Success':
                    self.logger.write_to_log(f"User '{all_information['username']}' has successfully registered - "
                                             f"{self.logger.get_datetime_string()}")

                    self.field_text.set(f"User '{all_information['username']}' has been registered.")
                    self.reset_fields()
                else:
                    self.field_text.set(message)
                    self.logger.write_to_log(f"Registration for {all_information['username']} has failed. "
                                             f"Cause: {message}. - "
                                             f"{self.logger.get_datetime_string()}")
