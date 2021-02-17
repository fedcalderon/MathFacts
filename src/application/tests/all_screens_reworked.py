# This is a work in progress. This keeps all the screens in a single window.
# The major difference between this and the current program is that all the screens are contained in lists rather than
#   tk windows.
#
#
#
#
#
#
import tkinter as tk
from tkinter import ttk
import csv
import src.application.tests.welcome as welcome
import src.application.tests.registration as r


class MyApplication(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("MathFacts")
        self.geometry("1000x650")
        self.resizable(width=True, height=True)
        self.display_welcome_screen()
        self.columnconfigure(0, weight=1)




    def display_welcome_screen(self):
        self.welcome_screen = [welcome.IconFrame(self), welcome.DescriptionFrame(self),]
                               #welcome.LinksFrame(self, self, self.registration_screen)]

        for item in self.welcome_screen:
            item.grid()

    # def display_registration(self):
    # self.registration_screen = [r.ChildInformation(self), r.Guardian1Info(self), r.Guardian2Info(self),
        #                        r.LoginInformation(self)]
    #     self.change_screen(self.welcome_screen, self.registration_screen)
    #     for item in self.registration_screen:
    #         item.grid()

        # self.change_screen_button_1 = ttk.Button(self, text="Go to screen 2",
        #                                          command=lambda: self.change_screen(self.welcome_screen,
        #                                                                             self.view_2_items))
        # self.change_screen_button_1.grid(row=1200, column=100, sticky=tk.E)
        # self.welcome_screen.append(self.change_screen_button_1)
        #
        # # View 2
        # self.g2 = Guardian2Info(self)
        # self.l = LoginInformation(self)
        # # self.view_2_items = [self.g2, self.l]
        # self.view_2_items = [Guardian2Info(self), LoginInformation(self)]
        #
        # self.change_screen_button_2 = ttk.Button(self, text="Go to screen 3",
        #                                          command=lambda: self.change_screen(self.view_2_items,
        #                                                                             self.view_3_items))
        # self.view_2_items.append(self.change_screen_button_2)
        #
        # # View 3
        # self.ch = ChilInformation(self)
        # self.view_3_items = [self.ch]
        #
        # self.change_screen_button_3 = ttk.Button(self, text="Go back to screen 2",
        #                                          command=lambda: self.change_screen(self.view_3_items,
        #                                                                             [Guardian2Info(self),
        #                                                                              LoginInformation(self)]))
        # self.view_3_items.append(self.change_screen_button_3)

    def change_screen(self, current_screen, new_screen):
        for item in current_screen:
            item.destroy()
        for item in new_screen:
            print(new_screen)
            item.grid(sticky=(tk.E + tk.W + tk.N + tk.S))


if __name__ == '__main__':
    app = MyApplication()
    app.mainloop()
