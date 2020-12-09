import tkinter as tk
from tkinter import ttk
import csv


class LoginInformation(tk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent, text="login Information", pady=20)
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


class ChildInformation(tk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent, text="Child Information", pady=15)
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
        self.resizable(width=True, height=True)
        self.view_1()

        self.columnconfigure(0, weight=1)

    def view_1(self):
        # View 1
        self.Main_Label = ttk.Label(self, text="Signup for MathFacts", font=("TkDefaultFont", 27), wraplength=600)
        self.Main_Label.grid(row=0, column=0, sticky=tk.W)
        self.c = ChildInformation(self)
        self.c.grid(sticky=(tk.E + tk.W + tk.N + tk.S))
        self.g1 = Guardian1Info(self)
        self.g1.grid(sticky=(tk.E + tk.W + tk.N + tk.S))
        self.view_1_items = [self.Main_Label, self.c, self.g1]

        # View 2
        self.g2 = Guardian2Info(self)
        self.l = LoginInformation(self)
        self.view_2_items = [self.g2, self.l]

        self.change_screen_button_1 = ttk.Button(self, text="Change view",
                                                 command=lambda : self.change_screen(self.view_1_items, self.view_2_items))
        self.change_screen_button_1.grid(row=1200, column=100, sticky=tk.E)
        self.view_1_items.append(self.change_screen_button_1)

        # Broken. Needs fixing.

        # self.change_screen_button_2 = ttk.Button(self, text="Back button",
        #                                          command=lambda: self.change_screen(self.view_2_items,
        #                                                                             self.view_1_items))
        # self.view_2_items.append(self.change_screen_button_2)
        #self.change_screen_button_2.grid(row=1200, column=100, sticky=tk.E)

    def change_screen(self, current_screen, new_screen):
        for item in current_screen:
            item.destroy()
        for item in new_screen:
            item.grid(sticky=(tk.E+tk.W+tk.N+tk.S))

if __name__ == '__main__':
    app = MyApplication()
    app.mainloop()