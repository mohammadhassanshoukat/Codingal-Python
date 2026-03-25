#open the file in reading mode
file_read =open('Codingal.txt','r')
print("File in reading mode - ")
print(file_read.read())
file_read.close()

#open the file in writing mode
file_write = open('Codingal.txt','w')
#write in the file
file_write.write("File in writing mode........ ")
file_write.write("This is Penguin, I am 1 year old")
file_write.close()

#open the file in append mode
file_append = open ('Codingal.txt','a')
#append in the file
file_append.write("\n File in append mode......... ")
file_append.write("This penguin i am 12 mmonths old")
file_append.close()