#open the file in read mode
file_read = open('Codingal.txt','r')
print("File in read mode - ")
print(file_read.read())
file_read.close()

#open the file in write mode
file_write = open('Codingal.txt','w')
#write in the file
file_write.write("file in write mode - ")
file_write.write('Hi i am penguin and i am 2 years old')
file_write.close()

#open the file in append mode
file_append = open('Codingal.txt','a')
#append in the file
file_append.write("\nfile in append mode - ")
file_append.write('Hi i am penguin and i am 3 years old')
file_append.close()