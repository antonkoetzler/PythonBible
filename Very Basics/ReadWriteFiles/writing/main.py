# Opening writeToHere.txt with read & write permissions
file = open("writeToHere.txt", "r+")

# Inserts a string into the file
file.write("I really like the programming language Python")
# An example of adding multiple lines using write(...)
file.write("\n\nMy favourite TV show is Mr. Robot\n\nI like cheese")

# Inserts said array into the file
arr = ["\n\n", "On ", "the ", "same ", "line", "\nOn another line"]
file.writelines(arr)

print("writeToHere.txt:")
file.seek(0)
print(file.read())
