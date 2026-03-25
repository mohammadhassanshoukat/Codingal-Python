#program to append contents of file in another file

#entwring file names
firstfile = input("Enter the name of the first file: ")
secondfile = input("Enter the name of the second file: ")

#opening the both files in reading mode to read its contents
f1 = open(firstfile, "r")
f2 = open(secondfile, "r")

#printing the contents of the file before appending them
print("The contents of the first file before appending - \n", f1.read())
print("The contents of the second file before appending - \n", f2.read())

#closing the file