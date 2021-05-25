import tkinter as tk
from tkinter import ttk
from src.application.new_views import stats_graph as stats_graph
import os


class ReportsFrame(tk.Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        self.report_graph = stats_graph.ReportsGraph()
        self.graph = None

        self.Main_Label = ttk.Label(self, text="User Reports", font=("TkDefaultFont", 27))
        self.Main_Label.grid(row=0, column=0)

        self.Save = ttk.Button(self, text="Update Reports Graph", command=lambda: self.show_icon(parent))
        self.Save.grid(row=1, column=0)

        tk.Button(self, text="Back to Home", command=lambda:
                  parent.change_screen(parent.welcome_screen)).grid(row=3, column=0)

    def show_icon(self, parent):
        if parent.current_screen == parent.reports_screen:
            self.report_graph.generate_graph(parent)
            self.graph = GraphFrame(self)
            self.graph.grid(row=2, column=0)
            # self.graph.image_label.grid()
            # parent.reports_screen.extend([self.graph, self.graph.image_label])
            # for item in parent.reports_screen:
            #     item.grid()


class GraphFrame(tk.Frame):
    """Contains and displays a graph of the student's quiz grades."""
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        if os.path.exists(stats_graph.graph_path):
            self.image = tk.PhotoImage(file=stats_graph.graph_path)
            self.image_label = ttk.Label(self, image=self.image)
            self.image_label.pack()
        else:
            self.label = ttk.Label(self, text="You have not completed any quizzes yet.", font=("TkDefaultFont", 16))
            self.label.pack(pady=10)
