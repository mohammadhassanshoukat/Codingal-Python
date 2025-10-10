actualcost=float(input("Enter the actual cost:"))
salecost=float(input("Enter the sale cost:"))



if salecost>actualcost:
    amount=salecost-actualcost
    print("toatal profit={0}".format(amount))
else:
        print("no profit")