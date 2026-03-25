#program to count number of lines in this file
#opneing a file
file =open("Codingal.txt", "r")
counter = 0

#reading from the file
Content = file.read()
#spliting content in two lines
# and storing them in a list
CoList = Content.split("\n")


for i in CoList:
    counter += 1


print("These are how many lines are there in the file")
print(counter)