def print_codingal(n):
    if n <= 0:
        return


    print("Codingal")
    print_codingal(n//2)
    print_codingal(n//2)


#call the function
print_codingal(8)