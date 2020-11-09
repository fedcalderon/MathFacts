import tkinter as tk
from tkinter import ttk
import ChildInformation
import GuardianInfo
import LoginInformation


class MyApplication(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("MathFacts")
        self.geometry("800x650")
        #self.configure(bg="gold")


        # background_image = tk.PhotoImage('Pizza.png')
        # background_label = tk.Label(self, image=background_image)
        # background_label.image = background_image
        # background_label.place(x=0, y=0, relwidth=2, relheight=2)

        self.resizable(width=True, height=True)
        self.Main_Label = ttk.Label(self, text="Signup for MathFacts", font=("TkDefaultFont", 27), wraplength=600)
        self.Main_Label.grid(row=0, column=0, sticky=tk.W)

        self.c = ChildInformation.ChildInformation(self)
        self.c.grid(sticky=(tk.E + tk.W + tk.N + tk.S))

        self.g1 = GuardianInfo.Guardian1Info(self)
        self.g1.grid(sticky=(tk.E + tk.W + tk.N + tk.S))

        self.g2 = GuardianInfo.Guardian2Info(self)
        self.g2.grid(sticky=(tk.E + tk.W + tk.N + tk.S))

        self.l = LoginInformation.LoginInformation(self)
        self.l.grid(sticky=(tk.E + tk.W + tk.N + tk.S))

        self.Save = ttk.Button(self, text="Save", command=self.save)
        self.Save.grid(row=1200, column=0, sticky=tk.W)

        self.columnconfigure(0, weight=1)

    def save(self):
        ################################################################################################################
        # This code is from https://stackoverflow.com/questions/2846947/get-screenshot-on-windows-with-python
        all_information = {
            "child_first_name": self.c.FirstName.get(),
            "child_last_name": self.c.LastName.get(),
            "child_grade": self.c.Grade.get(),
            "child_age": self.c.Age.get(),

            "guardian_1_first_name": self.g1.FirstName.get(),
            "guardian_1_last_name": self.g1.LastName.get(),

            "guardian_2_first_name": self.g2.FirstName.get(),
            "guardian_2_last_name": self.g2.LastName.get(),

            "username":self.l.Username.get(),
            "password":self.l.Password.get(),
        }

        print(all_information)
        ################################################################################################################


if __name__ == '__main__':
    app = MyApplication()
    app.mainloop()