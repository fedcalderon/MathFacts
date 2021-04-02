"""
This is the entry to the Math Facts Application
"""

from src.application.archived.welcome import WelcomeView


if __name__ == '__main__':
    app = WelcomeView()
    app.mainloop()
