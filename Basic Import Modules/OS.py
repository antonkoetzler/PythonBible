import os

# nt = Windows
os.system("CLS" if os.name == "nt" else "clear")

print("Your operating system is: ", end="", flush=True)
if (os.name == "posix"): print("Linux")
else: print("Windows")
