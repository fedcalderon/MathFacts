# Milton
import tkinter as tk
from tkinter import ttk


class TermsOfUseWindow(tk.Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        #Used this from andrews code to display window
        description = "No copying this program or using it illegally. It is strictly for the use of Math Facts purposes only. \n"
        desc_label = ttk.Label(self, text=description, wraplength=200, font=("TkDefaultFont", 14))
        desc_label.pack()


#This portion of code displays the window
if __name__ == '__main__':
    root = tk.Tk()
    root.title('Terms Of Use')
    root.resizable(width=False, height=False)
    root.geometry('340x120')
    TermsOfUseWindow(root).pack(expand=True, fill='both')
    root.mainloop()