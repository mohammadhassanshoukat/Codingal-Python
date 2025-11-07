def shutdown(answer):
    if answer == "yes":
        return "Shutting down"
    elif answer == "no":
        return "cant shutdown"
    else:
        return "Sorry"


user_input = input("Do you want to shut down the system? (Yes/no): ")
print(shutdown(user_input))
