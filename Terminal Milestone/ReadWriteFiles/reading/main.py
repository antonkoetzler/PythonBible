# Opening information.txt, read only
file = open("information.txt", "r")



# Returns the file as an array of strings
filecontents_arr = file.readlines()

print("filecontents_arr: ", filecontents_arr)

# Formatting our information (removing the \n on each element)
for x in range(len(filecontents_arr)):
  filecontents_arr[x] = filecontents_arr[x][0:3]
  print(filecontents_arr[x])



print()

# Places file handle at line 0 again (resetting eof)
file.seek(0)

# Returns the file as a string
filecontents_str = file.read()
print(filecontents_str)



file.seek(0)

# Returns one line from the file
filecontents_line = file.readline(1)
print(filecontents_line)



# Always close the file
file.close()
