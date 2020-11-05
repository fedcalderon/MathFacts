"""
This is the entry to the Math Facts Application
"""
from src.application.views import registration

print("Welcome to the Math Facts Application")

if __name__ == '__main__':
    app = registration.MyApplication()
    app.mainloop()