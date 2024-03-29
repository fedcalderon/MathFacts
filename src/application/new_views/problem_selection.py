# Select which problem set to work on
# Andrew
# This is task #4 and it works

import tkinter as tk
from tkinter import ttk
from src.application.new_views import math_screen
from datetime import datetime
import src.application.models.modified_logger as logger
from src.application.new_views import results
from src.application.new_views import settings

# DIFFERENT TYPES OF PROBLEMS AND IDS:
# 1-ADD: Single digit addition
# 2-ADD: Double digit addition
# 3-ADD: Addition up to 5 digits
# 1-SUB: Single digit subtraction
# 2-SUB: Double digit subtraction
# 3-SUB: Subtraction up to 5 digits
# 1-MUL: Single digit multiplication
# 2-MUL: Double digit multiplication
# 1-DIV: Division with a single digit divisor.
# 2-DIV: Division with a double digit divisor.


class OptionFrame(tk.Frame):
    """A frame that contains one option for the user."""

    def __init__(self, parent, name, detail, ID, screen_to_destroy, master_screen, *args, **kwargs):
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
        self.label_frame.pack(expand=True,
                              fill='both')  # Source: https://stackoverflow.com/questions/28419763/expand-text-widget-to-fill-the-entire-parent-frame-in-tkinter
        self.start_is_clicked = False

        # Create and position the widgets in the LabelFrame
        detail_label = ttk.Label(self.label_frame, text=detail, padding=(0, 0, 50, 10))
        detail_label.grid(row=0, column=0, sticky='w')

        start_frame = tk.Frame(self.label_frame, height=20)
        start_frame.grid(row=1, column=0)
        self.start_button = ttk.Button(self.label_frame, text='Start', command=lambda: self.on_start(master_screen))
        # Source: https://stackoverflow.com/questions/18736465/how-to-center-a-tkinter-widget
        self.start_button.place(relx=1, rely=1, anchor='se')

        # self.m_s = math_screen.Math_Screen(master_screen, self.ID)

    def on_start(self, master_screen):
        """Handle the start button pressed event."""
        # Start the proper math exercise
        print(f"Starting {self.name} activity...")
        logger.Logger('activities_started.log').write_to_log(
            f"Starting {self.name} activity -- {datetime.now()}")
        self.start_is_clicked = True
        master_screen.math_problems_screen = math_screen.Math_Screen(master_screen, self.ID)
        master_screen.change_screen(master_screen.math_problems_screen)

        # if master_screen.math_problems_screen[0].Question_Count - 1 == master_screen.math_problems_screen[0].Total_Questions:
        #     tk.Button(master_screen, text="Show Grades",
        #               command=lambda: results.ResultsScreen(self, 'test').mainloop()).grid()


class SelectionView(tk.Frame):
    """The frame where the user selects which type of problems to practice."""

    def __init__(self, parent, screen_to_destroy, student, master_screen, *args, **kwargs):
        super().__init__(parent, padx=20, pady=15, *args, *kwargs)

        # Get grade and username
        self.grade = int(student['child_grade'])
        self.username = student['username']

        # Create users_list toolbar with menus
        # Source: http://zetcode.com/tkinter/menustoolbars/
        toolbar = tk.Menu(self.master)
        self.master.config(menu=toolbar)

        user_menu = tk.Menu(toolbar)
        user_menu.add_command(label='Log Out', command=parent.log_out)
        toolbar.add_cascade(label=self.username, menu=user_menu)

        settings_menu = tk.Menu(toolbar)
        toolbar.add_cascade(label='Settings', menu=settings_menu)

        settings_menu.add_command(label='Settings', command=lambda: parent.change_screen(
            parent.settings_screen))

        # num_questions_menu = tk.Menu(settings_menu)
        # settings_menu.add_cascade(label='Number of Questions', menu=num_questions_menu)
        # num_questions = settings.get_num_questions(self.username)
        # # Setting initial value of menu radio buttons:
        # # https://stackoverflow.com/questions/61578186/python-tkinter-how-to-set-initial-selection-for-radiobutton-menu
        # self.num_questions = tk.IntVar()
        # self.num_questions.set(num_questions)
        # num_questions_menu.add_radiobutton(label='10', value=10, variable=self.num_questions,
        #                                    command=self.set_num_questions)
        # num_questions_menu.add_radiobutton(label='20', value=20, variable=self.num_questions,
        #                                    command=self.set_num_questions)
        # num_questions_menu.add_radiobutton(label='50', value=50, variable=self.num_questions,
        #                                    command=self.set_num_questions)
        # num_questions_menu.add_radiobutton(label='100', value=100, variable=self.num_questions,
        #                                    command=self.set_num_questions)


        reports_menu = tk.Menu(toolbar)
        toolbar.add_cascade(label='Reports', menu=reports_menu)
        reports_menu.add_command(label='Reports', command=lambda: parent.change_screen(parent.reports_screen))

        # Make a list to hold all the options
        self.options = []
        self.frame = tk.Frame(self)
        self.frame.grid()

        # Use the grade to determine which tests to show
        if self.grade == 1:
            self.options.append(OptionFrame(self.frame, 'Addition', 'Single digit addition.', '1-ADD', screen_to_destroy, master_screen))
            self.options.append(OptionFrame(self.frame, 'Subtraction', 'Single digit subtraction', '1-SUB', screen_to_destroy, master_screen))

        elif self.grade == 2:
            self.options.append(OptionFrame(self.frame, 'Addition', 'Double digit addition.', '2-ADD', screen_to_destroy, master_screen))
            self.options.append(OptionFrame(self.frame, 'Subtraction', 'Double digit subtraction.', '2-SUB', screen_to_destroy, master_screen))

        elif self.grade == 3:
            self.options.append(OptionFrame(self.frame, 'Addition', 'Double digit addition.', '2-ADD', screen_to_destroy, master_screen))
            self.options.append(OptionFrame(self.frame, 'Subtraction', 'Double digit subtraction.', '2-SUB', screen_to_destroy, master_screen))
            self.options.append(OptionFrame(self.frame, 'Multiplication', '0 to 12 multiplication.', '1-MUL', screen_to_destroy, master_screen))

        elif self.grade == 4:
            self.options.append(OptionFrame(self.frame, 'Addition', 'Multi-digit addition.', '3-ADD', screen_to_destroy, master_screen))
            self.options.append(OptionFrame(self.frame, 'Subtraction', 'Multi-digit subtraction.', '3-SUB', screen_to_destroy, master_screen))
            self.options.append(OptionFrame(self.frame, 'Multiplication', '0 to 12 multiplication.', '1-MUL', screen_to_destroy, master_screen))
            self.options.append(OptionFrame(self.frame, 'Division', 'Whole number division', '1-DIV', screen_to_destroy, master_screen))

        elif self.grade == 5:
            self.options.append(OptionFrame(self.frame, 'Addition', 'Multi-digit addition.', '3-ADD', screen_to_destroy, master_screen))
            self.options.append(OptionFrame(self.frame, 'Subtraction', 'Multi-digit subtraction.', '3-SUB', screen_to_destroy, master_screen))
            self.options.append(OptionFrame(self.frame, 'Multiplication', 'Double digit multiplication.', '2-MUL', screen_to_destroy, master_screen))
            self.options.append(OptionFrame(self.frame, 'Division', 'Multi-digit division', '2-DIV', screen_to_destroy, master_screen))

        elif self.grade >= 6:
            self.options.append(OptionFrame(self.frame, 'Addition', 'Multi-digit addition.', '3-ADD', screen_to_destroy, master_screen))
            self.options.append(OptionFrame(self.frame, 'Subtraction', 'Multi-digit subtraction.', '3-SUB', screen_to_destroy, master_screen))
            self.options.append(OptionFrame(self.frame, 'Multiplication', 'Double digit multiplication.', '2-MUL', screen_to_destroy, master_screen))
            self.options.append(OptionFrame(self.frame, 'Division', 'Multi-digit division', '2-DIV', screen_to_destroy, master_screen))

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

        tk.Button(self, text="Back to Home", command=lambda: parent.change_screen(parent.welcome_screen)).grid()

    # def set_num_questions(self):
    #     settings.set_num_questions(self.username, self.num_questions.get())
