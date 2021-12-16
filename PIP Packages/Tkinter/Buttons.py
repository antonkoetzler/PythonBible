from tkinter import *

# Main window initialization #
root = Tk()
root.title("Using buttons in tkinter")
root.geometry("200x100")
root.configure(bg="#101010")



# Functions #
def displayAbout():
  aboutWindow = Toplevel(root)
  aboutWindow.title("About this program")
  aboutWindow.geometry("350x50")

  aboutText = Label(
    aboutWindow,
    text="This program demonstrates how to use buttons in tkinter"
  )
  aboutText.pack()

  authorText = Label(
    aboutWindow,
    text="Author: Anton Koetzler-Faust"
  )



# Widgets #
sampleButton = Button(
  root,
  text="This button does nothing",
  bg="#EDE6D6"
)
# Placing the button on the window
sampleButton.pack()

aboutButton = Button(
  root,
  text="About this program",
  bg="#e0a0fa",
  command=displayAbout
)
aboutButton.pack()

quitButton = Button(
  root,
  text="Quit",
  bg="#11706d",
  command=exit
)
quitButton.pack()



# Main loop
root.mainloop()
