#!/usr/bin/env python3

# based on project by PythonGeeks

from tkinter import *

# Tk() helps display the window on the screen
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
Story1Button.place(x=140, y=90)
Story2Button = Button(
    screen,
    text="Story 2",
    font=("Century Gothic", 13),
    command=lambda: Story2(screen),
    bg="Blue",
)
Story2Button.place(x=150, y=150)

screen.update()
# running the event loop
screen.mainloop()


def Story1(win):
    def final(tl: Toplevel, number, city, timeofday, transport, point):
        text = f""" The day before an exam, {number} students decided to travel. They missed the exam, and decided to find a way to do the exam anyways.
        'Teacher, we went on a trip to {city}, and blew a tire. We could not fix it, and that is why we missed the exam.'
        The teacher was understanding and said they could take the exam that {timeofday}.
        And so, the students took the {transport} home, and studied as hard as they could.
        At the time of the test, the teacher placed each student in a different room and handed them the test.
        First question worth {point} points: 'Explain Ohm's Law'
        The {number} students were happy because they had studied for the exam, and thought it was going to be very easy.
        Second question worth all the points: 'Which tire was flat?'
        """

        tl.geometry(newGeometry="500x500")

        Label(tl, text="Story: ", wraplength=tl.winfo_width()).place(x=160, y=310)
        Label(tl, text=text, wraplength=tl.winfo_width()).place(x=0, y=330)

    NewScreen = Toplevel(win, bg="yellow")


def Story2(win):
    pass
