"""
This is the entry to the Math Facts Application
"""
from src.application.views import registration
from src.application.welcome import welcome_description
from src.application.views.welcome import WelcomeView
import tkinter as tk
#

if __name__ == '__main__':
    app = WelcomeView()
    app.mainloop()