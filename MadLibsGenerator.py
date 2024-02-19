#!/usr/bin/env python3

# based on project by PythonGeeks

from tkinter import *

screen = Tk()
screen.title("Mini-Games Mad Libs Generator")
screen.geometry("400x400")
screen.config(bg="purple")
Label(screen, text="Mini-Games Mad Libs Generator").place(x=100, y=20)
# creating buttons
Story1Button = Button(
    screen,
    text="Story 1",
    font=("Century Gothic", 13),
    command=lambda: Story1(screen),
    bg="Blue",
)


def Story1(win):
    pass
