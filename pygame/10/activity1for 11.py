#open file and read its contents 
file = open('Codingal.txt','r')
print(file.read())
file.close()

#open the file and read its begning 8 characters
file = open  ('Codingal.txt','r')
print("\n Read the in parts \n")
print(file.read(8))
file.close()

#append your name and age in the file
file = open ('Codingal.txt','a')
file.write("Hi! i am penguin and i am 1 year old")
file.close()