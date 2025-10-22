dec=int(input("Enter a decimal number: "))
bin=""   
num=dec

while num>0:
    num=num% 2
    bin=str(num)+bin
    num=num // 2
print("The binary number is", bin)
