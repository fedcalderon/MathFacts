"""
This is the entry to the Math Facts Application
"""
from src.application.views import registration
from src.application.welcome import welcome_description
import tkinter as tk


if __name__ == '__main__':
    root = tk.Tk()
    root.title('MathFacts')
    root.resizable(width=False, height=False)
    root.geometry('500x300')
    welcome_description.DescriptionFrame(root).pack(expand=True, fill='both')
    root.mainloop()