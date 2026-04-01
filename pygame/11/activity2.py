#create a new file
newfile = open('newfile.txt','x')
newfile.close()


#check if file exist
import os
print("Checking if myfile exist or not.......")
if os.path.exists('myfile.txt'):
    os.remove('myfile.txt')
else:
    print ("The file does not exist")


#create the file if it does not exist
myfile = open('myfile.txt', 'w')
myfile.write('I am penguin and i am not 1 years old')
myfile.close()


#delete the file named codingal
os.remove('Codingal.txt')
print("The file named COdingal is succesfuly deleted")

#dlete the folder
os.rmdir('Folder')