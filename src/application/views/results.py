# Showing all problems worked on by user
# Milton
from tkinter import *
import time

window = Tk()

window.title("Math Problems")
menu = Menu(window)

canvas_width = 400
canvas_height = 400

w = Canvas(window, width=canvas_width, height=canvas_height, bg="#B7F9E3")
w.pack()

a = int(input("enter first number: "))
operation = input("enter the type of equation: ")
b = int(input("enter second number: "))


def add(a,b):
    c = a + b
    return str(c)

def subtract(a,b):
    c = a - b
    return str(c)

def division(a,b):
    c = a / b
    return str(c)

def multiply(a, b):
    c = a * b
    return str(c)

if operation == "+":
    d = add(a,b)

if operation == "-":
    d = subtract(a, b)

if operation == "/":
    d = division(a, b)

if operation == "*":
    d = multiply(a, b)

if operation == "+":
    w.create_text(100, 50, font=("times new roman", 16), text="Addition Results")
    w.create_text(200, 200, font=("times new roman", 16), text=d)

if operation == "-":
    w.create_text(100, 50, font=("times new roman", 16), text="Subtraction Results")
    w.create_text(200, 200, font=("times new roman", 16), text=d)

if operation == "*":
    w.create_text(100, 50, font=("times new roman", 16), text="Multiplication Results")
    w.create_text(200, 200, font=("times new roman", 16), text=d)

if operation == "/":
    w.create_text(100, 50, font=("times new roman", 16), text="Division Results")
    w.create_text(200, 200, font=("times new roman", 16), text=d)

window.config(menu=menu)
window.mainloop()
