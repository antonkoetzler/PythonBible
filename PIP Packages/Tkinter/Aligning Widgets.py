from tkinter import *

root = Tk()
root.title("Aligning Widgets in Tkinter")
root.geometry("500x500")
root.configure(bg="#FFE4C4")

def showGrid():
  gridWindow = Toplevel(root)
  gridWindow.title("grid() sample")
  gridWindow.configure(bg="#FFE4C4")

  gridButton1 = Button(
    gridWindow,
    text="Button #1",
    bg="#FFCCCB",
    command=lambda: congratulations(gridWindow)
  )
  gridButton1.grid(row=0, column=0)

  gridButton2 = Button(
    gridWindow,
    text="Button #2",
    bg="#90EE90",
    command=lambda: congratulations(gridWindow)
  )
  gridButton2.grid(row=0, column=1)

  gridButton3 = Button(
    gridWindow,
    text="Button #3",
    bg="#FFFFE0",
    command=lambda: congratulations(gridWindow)
  )
  gridButton3.grid(row=1, column=0)

  gridButton4 = Button(
    gridWindow,
    text="Button #4",
    bg="#FFD580",
    command=lambda: congratulations(gridWindow)
  )
  gridButton4.grid(row=1, column=1)

def congratulations(parent):
  congratsWindow = Toplevel(parent)
  congratsWindow.title("Congratulations!")
  congratsWindow.geometry("150x0")
  congratsWindow.configure(bg="#FFE4C4")

# Using pack() without any arguments
label1 = Label(
  root,
  text="pack() automatically gets placed where it seems best",
  bg="white"
)
label1.pack()

# Using pack(side)
label2 = Label(
  root,
  text="pack(side) places this to the left now",
  bg="white"
)
label2.pack(side=LEFT)

# Using place()
label3 = Label(
  root,
  text="place() places a widget into specified x, y coordinates",
  bg="white"
)
label3.place(x=50, y=50)

# Button to show grid() example
gridButton = Button(
  root,
  text="Click to show grid() example",
  bg="white",
  command=showGrid
)
gridButton.pack()

root.mainloop()
