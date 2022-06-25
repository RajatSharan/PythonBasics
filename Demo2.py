

values = [1, 2, "Rajat", 4, 5]
#List is a datatype that allows multiple values and can be different data types

print(values[0])
print(values[3])
#print(values[9])
print(values[-1])
print(values[1:4])
values.insert(3, "Sharan")
print(values)
values.append("End")
print(values)

values[2]='RAJAT'
print(values)

del values[0]
print(values)