from tkinter import *
top=Tk()
top.title("Dashboard")
top.geometry("1000x650")
lbl=Label(top,text="Dashboard", font=("", 25))
lbl.place(x=80,y=100)
btn=Button(top, text="Exit", font=("", 15))
btn.place(x=35,y=20)
top.mainloop()
