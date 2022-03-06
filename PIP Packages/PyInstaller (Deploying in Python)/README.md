# Deploying packages with PyInstaller
1. Install PyInstaller: pip install pyinstaller
2. For a simple console program that is an executable file in windows
	- Clone my simple matrix class program: ```git clone git@github.com:antonkoetzler/PythonMatrixClass.git; cd PythonMatrixClass```
	- pyinstaller --onefile main.py
	- In the dist directory, you can place in executable anywhere on any pc
