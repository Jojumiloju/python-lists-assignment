a = [1,2,3]
b = a

b[0] = 100

print(a)
print(b)
print(id(a))
print(id(b))

#Then answer in comments:

#Why did both lists change?
#the variable name b and a are labels to the same data or object in memory. Any of the variable names can be used to make changes to the data object in memory.

#Why are ids same?
#The ids are the same because they point to the same object in memory

#What does this mean?
#Assignment operators do not perform a copy of the variables contents in python, unlike in other programming languages like c++