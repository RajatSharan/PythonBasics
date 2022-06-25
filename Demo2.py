

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

a = (1, 2, 3, 4)
print(a)
print(a[0])

#tuple having multiple type of data.
b=("hello", 1,2,3,"go")
print(b) #prints the whole tuple


a = {1:"first name",2:"last name", "age":33}

#print value having key=1
print(a[1])
#print value having key=2
print(a[2])
#print value having key="age"
print(a["age"])

#How to Create Dictionaries at run time and add data into it

dic = {}

dic["FirstName"] = "Rajat"
dic["LastName"] = "Sharan"

print(dic)