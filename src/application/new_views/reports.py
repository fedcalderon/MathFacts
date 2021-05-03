import tkinter as tk
from tkinter import ttk
import json
from pathlib import Path
from src.application.new_views import stats_graph as stats_graph

"""This view is a work in progress. When it is completed, it will store all the lesson results in a graph. """


class ReportsFrame(tk.Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        self.report_graph = stats_graph.ReportsGraph()
        self.icon = IconFrame(parent)

        self.Main_Label = ttk.Label(self, text="User Reports Screen:", font=("TkDefaultFont", 27), wraplength=600)
        self.Main_Label.grid(row=0, column=0, sticky=tk.W)

        self.Save = ttk.Button(self, text="Click to show Reports Graph",
                               command=lambda: self.report_graph.display_graph(parent))

        self.Save = ttk.Button(self, text="Click to show Reports Graph",
                               command=lambda: self.show_icon(parent))

        self.Save.grid(row=1200, column=0)

    def show_icon(self, parent):
        if parent.current_screen == parent.reports_screen:
            # self.icon.grid()
            # self.icon.image_label.grid()
            parent.reports_screen.extend([self.icon, self.icon.image_label])
            for item in parent.reports_screen:
                item.grid()


class IconFrame(tk.Frame):
    """Contains and displays the description of the Math Facts Practice application."""
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.image = tk.PhotoImage(file="view_images/user_graph.png")
        self.image_label = tk.Label(self, image=self.image)
