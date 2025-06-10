from tkinter import *


def create_root():
    root = Tk()  # This is to create the APP
    root.geometry("700x600")  # This is how to make the window
    root.title('GUI Shop')  # This is the title of the program
    root.resizable(False, False)  # Stops the program from expanding
    return root


def create_frame():
    frame = Canvas(root, width=700, height=700)  # This creates the frame to work on
    frame.grid(row=0, column=0)  # This is the starting point of the frame
    return frame


root = create_root()
frame = create_frame()
