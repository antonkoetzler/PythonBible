from wx import *

# Our application
app = App()

# Our (main) window
mainWindow = Frame(parent=None, title="Hello World")
mainWindow.Show(True)

app.MainLoop()
