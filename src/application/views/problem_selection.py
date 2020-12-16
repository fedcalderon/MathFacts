# Select which problem set to work on
# Andrew

import tkinter as tk
from tkinter import ttk
from src.application.views import math_screen


class OptionFrame(tk.Frame):
    """A frame that contains one option for the user."""
    def __init__(self, parent, name, detail, ID, *args, **kwargs):
        """Initializes an OptionFrame widget.
        :param parent: the parent widget
        :param name: the name of the option
        :param detail: optional additional detail about the option"""
        # Set the text of the LabelFrame to this option's name
        super().__init__(parent, padx=20, pady=20, width=500, *args, **kwargs)
        self.name = name
        self.ID = ID

        # Create users_list LabelFrame inside the Frame
        self.label_frame = tk.LabelFrame(self, text=name, font=("TkDefaultFont", 16), padx=5, pady=5)
        self.label_frame.pack(expand=True, fill='both')  # Source: https://stackoverflow.com/questions/28419763/expand-text-widget-to-fill-the-entire-parent-frame-in-tkinter
        self.start_is_clicked = False

        # Create and position the widgets in the LabelFrame
        detail_label = ttk.Label(self.label_frame, text=detail, padding=(0, 0, 50, 10))
        detail_label.grid(row=0, column=0, sticky='w')

        start_frame = tk.Frame(self.label_frame, height=20)
        start_frame.grid(row=1, column=0)
        start_button = ttk.Button(self.label_frame, text='Start', command=self.on_start)
        start_button.place(relx=1, rely=1, anchor='se')  # Source: https://stackoverflow.com/questions/18736465/how-to-center-a-tkinter-widget

    def on_start(self):
        """Handle the start button pressed event."""
        # Start the proper math exercise
        print(f"Starting {self.name} activity...")
        self.app = math_screen.Math_Screen_Settings('1-ADD')
        self.start_is_clicked  = True
        # self.app.update()
        self.app.mainloop()

class SelectionView(tk.Frame):
    """The frame where the user selects which type of problems to practice."""
    def __init__(self, parent, grade, username='Username', *args, **kwargs):
        super().__init__(parent, padx=20, pady=15, *args, *kwargs)

        # Create users_list toolbar with menus
        # Source: http://zetcode.com/tkinter/menustoolbars/
        toolbar = tk.Menu(self)
        self.master.config(menu=toolbar)

        user_menu = tk.Menu(toolbar)
        user_menu.add_command(label='Log Out')
        toolbar.add_cascade(label=username, menu=user_menu)

        settings_menu = tk.Menu(toolbar)
        toolbar.add_cascade(label='Settings', menu=settings_menu)

        reports_menu = tk.Menu(toolbar)
        toolbar.add_cascade(label='Reports', menu=reports_menu)

        # Make a list to hold all the options
        self.options = []

        # Use the grade to determine which tests to show
        if grade == 1:
            self.options.append(OptionFrame(self, 'Addition', 'Single digit addition.', '1-ADD'))
            self.options.append(OptionFrame(self, 'Subtraction', 'Single digit subtraction', '1-SUB'))
        # elif grade == 2:
        #     options.append(OptionFrame(self, 'Addition', 'Double digit addition.'))
        #     options.append(OptionFrame(self, 'Subtraction', 'Double digit subtraction.'))
        # elif grade == 3:
        #     options.append(OptionFrame(self, 'Addition', 'Double digit addition.'))
        #     options.append(OptionFrame(self, 'Subtraction', 'Double digit subtraction.'))
        #     options.append(OptionFrame(self, 'Multiplication', 'Single digit multiplication.'))
        # elif grade == 4:
        #     options.append(OptionFrame(self, 'Addition', 'Triple digit addition.'))
        #     options.append(OptionFrame(self, 'Subtraction', 'Triple digit subtraction.'))
        #     options.append(OptionFrame(self, 'Multiplication', '0 to 12 multiplication.'))
        #     options.append(OptionFrame(self, 'Division', 'Whole number division'))
        # elif grade == 5:
        #     options.append(OptionFrame(self, 'Addition', 'Triple digit addition.'))
        #     options.append(OptionFrame(self, 'Subtraction', 'Triple digit subtraction.'))
        #     options.append(OptionFrame(self, 'Multiplication', 'Double digit multiplication.'))
        #     options.append(OptionFrame(self, 'Division', 'Double digit division'))
        # elif grade >= 6:
        #     options.append(OptionFrame(self, 'Addition', 'Triple digit addition.'))
        #     options.append(OptionFrame(self, 'Subtraction', 'Triple digit subtraction.'))
        #     options.append(OptionFrame(self, 'Multiplication', 'Double digit multiplication.'))
        #     options.append(OptionFrame(self, 'Division', 'Double digit division'))
        #     options.append(OptionFrame(self, 'Algebra', 'Simple linear equations.'))

        # Place the options in the grid automatically
        max_columns = 2
        row = 0
        column = 0
        for option in self.options:
            # Add the option to the grid
            option.grid(row=row, column=column, sticky=(tk.E + tk.W))

            # Increment the variables
            column += 1
            if column >= max_columns:
                # Move to the next row if the row is filled
                column = 0
                row += 1


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Math Facts Practice')
    root.resizable(width=False, height=False)
    sv = SelectionView(root, grade=1)
    sv.pack(expand=True, fill='both')
    root.mainloop()
        # ID = '1-ADD'
        # app = math_screen.Math_Screen_Settings(ID)
        # app.mainloop()
