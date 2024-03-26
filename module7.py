# Read all the text in the file
a = open("demo.txt", "r")
print(a.read())
print("--------------------------------------------\n")
# Read a line of text
a = open("demo.txt", "r")
print(a.readline())
a.close()

# Read a character
print("--------------------------------------------\n")
a = open("demo.txt", "r")
print(a.read(3))
a.close()