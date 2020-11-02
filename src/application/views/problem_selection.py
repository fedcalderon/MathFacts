# Select which problem set to work on
# Andrew

import tkinter as tk
from tkinter import ttk


class OptionFrame(tk.Frame):
    """A frame that contains one option for the user."""
    def __init__(self, parent, name, detail='', *args, **kwargs):
        """Initializes an OptionFrame widget.
        :param parent: the parent widget
        :param name: the name of the option
        :param detail: optional additional detail about the option"""
        # Set the text of the LabelFrame to this option's name
        super().__init__(parent, padx=10, pady=5, width=500, *args, **kwargs)
        self.name = name

        # Create a LabelFrame inside the Frame
        self.label_frame = tk.LabelFrame(self, text=name, font=("TkDefaultFont", 16), padx=5, pady=5)
        self.label_frame.pack(expand=True, fill='both')  # Source: https://stackoverflow.com/questions/28419763/expand-text-widget-to-fill-the-entire-parent-frame-in-tkinter

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


class SelectionView(tk.Frame):
    """The frame where the user selects which type of problems to practice."""
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, padx=20, pady=15, *args, *kwargs)

        # Create a toolbar with menus
        # Source: http://zetcode.com/tkinter/menustoolbars/
        toolbar = tk.Menu(self)
        self.master.config(menu=toolbar)

        user_menu = tk.Menu(toolbar)
        user_menu.add_command(label='Log Out')
        toolbar.add_cascade(label='Username', menu=user_menu)

        settings_menu = tk.Menu(toolbar)
        toolbar.add_cascade(label='Settings', menu=settings_menu)

        reports_menu = tk.Menu(toolbar)
        toolbar.add_cascade(label='Reports', menu=reports_menu)

        # Create some OptionFrames as examples
        # In the future, these will be generated as needed
        addition_frame = OptionFrame(self, 'Addition', 'Two digit addition.')
        subtraction_frame = OptionFrame(self, 'Subtraction', 'Two digit subtraction.')
        multiplication_frame = OptionFrame(self, 'Multiplication', 'Single digit multiplication.')

        # Make a list to hold all the options
        options = [addition_frame, subtraction_frame, multiplication_frame]

        # Place the options in the grid automatically
        max_columns = 2
        row = 0
        column = 0
        for option in options:
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
    SelectionView(root).pack(expand=True, fill='both')
    root.mainloop()
