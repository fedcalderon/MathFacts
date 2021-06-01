import tkinter as tk
from tkinter import ttk
from src.application.new_views import registration as r
from src.application.models import database
import src.application.models.modified_logger as logger

"""This frame allows the user to change various user settings such as their name, grade, age, and guardian
information. They cannot(for now) change their username or password."""


class SettingsFrame(tk.Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        self.user_data = parent.student_data
        self.username = parent.student_id
        self.parent = parent

        self.Main_Label = ttk.Label(self, text="User Settings", font=("TkDefaultFont", 27), wraplength=600)
        self.Main_Label.grid(row=0, column=0, sticky=tk.W)

        self.c = r.ChildInformation(self)
        self.c.grid(sticky=(tk.E + tk.W + tk.N + tk.S))

        self.g1 = r.Guardian1Info(self)
        self.g1.grid(sticky=(tk.E + tk.W + tk.N + tk.S))

        self.g2 = r.Guardian2Info(self)
        self.g2.grid(sticky=(tk.E + tk.W + tk.N + tk.S))

        self.l = LoginInformation(self)
        self.l.grid(sticky=(tk.E + tk.W + tk.N + tk.S))

        self.q = NumberOfQuestions(self)
        self.q.grid(sticky=(tk.E + tk.W + tk.N + tk.S))

        self.reset_fields()

        self.field_text = tk.StringVar()
        self.field = ttk.Label(self, textvariable=self.field_text,
                               font=("TkDefaultFont", 11), wraplength=600)
        self.field.grid(sticky=tk.W)

        self.bottom_frame = tk.Frame(self)
        self.bottom_frame.grid()

        self.Save = ttk.Button(self.bottom_frame, text="Save", command=self.save)
        self.Save.grid(sticky=tk.W, row=0, column=0, padx=5)

        ttk.Button(self.bottom_frame, text="To Topics List", command=lambda: parent.change_screen(
            parent.problem_selection_screen)).grid(row=0, column=1, padx=5)
        ttk.Button(self.bottom_frame, text="Back to Home", command=lambda: parent.change_screen(
            parent.welcome_screen)).grid(row=0, column=2, padx=5)

    def save(self):
        new_username = self.l.Username.get().strip()
        password = self.l.Password.get()
        new_password = self.l.NewPassword.get()
        confirm_new_password = self.l.ConfirmPassword.get()

        try:
            logger.Logger('change_settings_attempts.log').write_to_log(f"Change settings successful")
            child_grade = int(self.c.Grade.get())
            child_age = int(self.c.Age.get())
            if child_grade > 999 or child_grade < 0:
                self.field_text.set("Child grade out of range")
                logger.Logger('change_settings_attempts.log').write_to_log(f"Change settings failed - GRADE TOO HIGH")
                return
            if child_age > 999 or child_age < 0:
                self.field_text.set("Child age out of range")
                logger.Logger('change_settings_attempts.log').write_to_log(f"Change settings failed - AGE TOO HIGH")
                return
        except ValueError:
            self.field_text.set("Invalid grade or age")
            logger.Logger('change_settings_attempts.log').write_to_log(f"Change settings failed - INVALID INPUT")
            return

        if password.strip() == "":
            self.field_text.set("You must enter your password to update user data")
            logger.Logger('change_settings_attempts.log').write_to_log(f"Change settings failed - PASSWORD VERIFICATION FAILED")
            return

        new_info = {
            "child_first_name": self.c.FirstName.get().strip(),
            "child_last_name": self.c.LastName.get().strip(),
            "child_grade": child_grade,
            "child_age": child_age,

            "guardian_1_first_name": self.g1.FirstName.get().strip(),
            "guardian_1_last_name": self.g1.LastName.get().strip(),

            "guardian_2_first_name": self.g2.FirstName.get().strip(),
            "guardian_2_last_name": self.g2.LastName.get().strip(),

            "username": new_username,
        }

        # Keep track of any changes the user has made
        no_changes = True
        for key, value in self.user_data.items():
            if value != new_info[key]:
                no_changes = False
                break

        old_num_questions = get_num_questions(self.username)
        new_num_questions = self.q.QuestionCount.get()
        if old_num_questions != new_num_questions:
            no_changes = False

        if self.l.ChangePassword.get():
            if new_password != confirm_new_password:
                self.field_text.set("New Passwords do not match")
                return
            new_info['password'] = new_password

            if password != new_password:
                no_changes = False

        # If there were no changes, don't bother saving it
        if no_changes:
            self.field_text.set("You have not made any changes")
            return

        for item in new_info:
            if item != "guardian_2_first_name" and item != "guardian_2_last_name":
                if new_info[item] == "":
                    self.field_text.set("Not all required fields have been answered")
                    return

        # Update database and app
        message = database.update_user_data(self.username, password, new_info)
        if message == 'Success':
            self.field_text.set('Changes saved')
            self.user_data = new_info
            self.username = new_info['username']
            self.reset_fields()
            self.parent.set_user(self.user_data)
        else:
            self.field_text.set(message)

        # Update user settings
        settings_dict = {'num_problems': new_num_questions}
        message = database.save_user_settings(new_username, settings_dict)
        print(message)

    def reset_fields(self):
        self.l.Password.set("")
        self.l.NewPassword.set("")
        self.l.ConfirmPassword.set("")
        self.l.ChangePassword.set(False)
        self.l.Username.set(self.username)

        self.c.FirstName.set(self.user_data['child_first_name'])
        self.c.LastName.set(self.user_data['child_last_name'])
        self.c.Grade.set(self.user_data['child_grade'])
        self.c.Age.set(self.user_data['child_age'])

        self.g1.FirstName.set(self.user_data['guardian_1_first_name'])
        self.g1.LastName.set(self.user_data['guardian_1_last_name'])

        self.g2.FirstName.set(self.user_data['guardian_2_first_name'])
        self.g2.LastName.set(self.user_data['guardian_2_last_name'])

        self.q.QuestionCount.set(get_num_questions(self.username))


# LoginInformation frame copied from registration, with changes
class LoginInformation(tk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent, text="Login Information", pady=20)
        # self.configure(bg="gold")

        # Tkinter validation: https://stackoverflow.com/questions/8959815/restricting-the-value-in-tkinter-entry-widget
        vcmd = (self.register(self.validate_length), '%d', '%P')

        self.Username = tk.StringVar()
        self.username_label = ttk.Label(self, text="Username")
        self.username_entry = ttk.Entry(self, textvariable=self.Username, validate='key', validatecommand=vcmd)
        self.username_label.grid(row=0, column=0, padx=10, sticky=tk.W)
        self.username_entry.grid(row=1, column=0, padx=10, sticky=tk.W)

        self.Password = tk.StringVar()
        self.password_label = ttk.Label(self, text="Password")
        self.password_entry = ttk.Entry(self, textvariable=self.Password, show='*',
                                        validate='key', validatecommand=vcmd)
        self.password_label.grid(row=0, column=1, padx=10, sticky=tk.W)
        self.password_entry.grid(row=1, column=1, padx=10, sticky=tk.W)

        self.ChangePassword = tk.BooleanVar()
        self.change_password_checkbox = ttk.Checkbutton(self, text="Change Password", variable=self.ChangePassword,
                                                        command=self.update_change_password)
        self.change_password_checkbox.grid(row=2, padx=10, sticky=tk.W)

        self.NewPassword = tk.StringVar()
        self.new_password_label = ttk.Label(self, text="New Password")
        self.new_password_entry = ttk.Entry(self, textvariable=self.NewPassword, show='*',
                                            validate='key', validatecommand=vcmd, state='disabled')
        self.new_password_label.grid(row=3, column=0, padx=10, sticky=tk.W)
        self.new_password_entry.grid(row=4, column=0, padx=10, sticky=tk.W)

        self.ConfirmPassword = tk.StringVar()
        self.confirm_password_label = ttk.Label(self, text="Confirm New Password")
        self.confirm_password_entry = ttk.Entry(self, textvariable=self.ConfirmPassword, show='*',
                                                validate='key', validatecommand=vcmd, state='disabled')
        self.confirm_password_label.grid(row=3, column=1, padx=10, sticky=tk.W)
        self.confirm_password_entry.grid(row=4, column=1, padx=10, sticky=tk.W)

    def update_change_password(self):
        if self.ChangePassword.get():
            self.new_password_entry['state'] = 'normal'
            self.confirm_password_entry['state'] = 'normal'
        else:
            self.NewPassword.set('')
            self.new_password_entry['state'] = 'disabled'
            self.ConfirmPassword.set('')
            self.confirm_password_entry['state'] = 'disabled'

    def validate_length(self, action, value_if_allowed):
        # action '1' means text is being inserted
        if action == '1':
            if len(value_if_allowed) > 24:
                return False
            else:
                return True
        else:
            return True


class NumberOfQuestions(tk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent, text="Number Of Questions", pady=15)
        self.QuestionCount = tk.IntVar()
        self.question_count_label = ttk.Label(self, text="Number of Questions")
        self.question_count_entry = ttk.Combobox(self, width=10, textvariable=self.QuestionCount)

        self.question_count_entry['values'] = tuple([10, 20, 50, 100])
        self.question_count_label.grid(row=200, column=100, padx=10, sticky=tk.W)
        self.question_count_entry.grid(row=300, column=100, padx=10, sticky=tk.W)


# Static functions for settings
def get_num_questions(username):
    settings, message = database.get_user_settings(username)
    if message == 'Success':
        logger.Logger('num_questions.log').write_to_log(f"Number of questions is {settings['num_problems']}")
        return settings['num_problems']

    else:
        logger.Logger('num_questions.log').write_to_log(f"Attempt to change number of questions failed")
        return 20
