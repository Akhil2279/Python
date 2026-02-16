
# read mode - "r"

f = open("c:\\Users\\akhil\\OneDrive\\Desktop\\example1.txt.txt", "r")
print(f.read())  # This code opens a file located at "c:\Users\akhil\OneDrive\Desktop\example1.txt.txt" in read mode ("r") and prints its contents to the console.

# readline() method - reads a single line from the file and returns it as a string. If the end of the file has been reached, it returns an empty string.

f = open("c:\\Users\\akhil\\OneDrive\\Desktop\\example1.txt.txt", "r")
print(f.readline())   # This code opens the same file in read mode and prints the first 7 characters of the first line of the file to the console.and it will print the first line of the file.
print(f.readline(5))  # This code reads the next line from the file, but only returns the first 5 characters of that line. If the line has fewer than 5 characters, it will return the entire line.it will count the spaces as well.
print(f.readlines())   # This code reads all lines from the file and returns them as a list of strings. Each string in the list represents a line from the file.

#write mode - "w"

f = open("c:\\Users\\akhil\\OneDrive\\Desktop\\example1.txt.txt", "w")
print(f.write("This is a new line added to the file."))  
# This code opens the same file in write mode ("w") and writes the string "This is a new line added to the file." to it. The write() method returns the number of characters written to the file, which is printed to the console. 
# Note that opening a file in write mode will overwrite any existing content in the file.

f = open("c:\\Users\\akhil\\OneDrive\\Desktop\\example1.txt.txt", "r")
print(f.read())

# append mode - "a"
f = open("c:\\Users\\akhil\\OneDrive\\Desktop\\example1.txt.txt", "a")
print(f.write("\nThis line is appended to the file."))

f = open("c:\\Users\\akhil\\OneDrive\\Desktop\\example1.txt.txt", "r")
print(f.read())

#x mode - "x"
f = open("example3.txt", "x")
print(f.write("This file is created using x mode."))
# This code creates a new file named "example3.txt" in the current working directory using exclusive creation mode ("x"). 
# If the file already exists, a FileExistsError will be raised. If the file is created successfully, the string "This file is created using x mode."

#A mode - "a"
f = open("example3.txt", "a")
print(f.write("\nThis line is appended to the file using a mode."))
# This code opens the "example3.txt" file in append mode ("a") and appends the string "\nThis line is appended to the file using a mode." to it.
