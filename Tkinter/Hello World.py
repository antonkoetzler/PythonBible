from tkinter import *

# Main window
root = Tk()

# Title of the window
root.title("Hello World")

# Width and height of the window
root.geometry("200x300")

# Creating a Label (text on the screen)
text = Label(root, text="Hello World")
# Makes the text visible, pack() also just organizes widgets in general
text.pack()

# Initializing the main loop
root.mainloop()
