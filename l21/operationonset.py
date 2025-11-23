my_set={1,2,2,3,4,4,4}
print("set : ",my_set)


my_set.add(5)
print("updated set : ",my_set)


set_1=my_set
set2={2,4,4,6}


print("\nSet 1",set_1)
print("Set 2",set2)
print("Difference")
print(set_1.difference(set2))
print("symmetric difference")
print(set_1.symmetric_difference(set2))
