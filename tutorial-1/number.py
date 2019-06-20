# Numbers in Python, we have Int's and Floats

# Prints 5
print(5)

# Since everything in Python is an object, we can use type() to check what type of Number Ojbect

# Prints <class 'int'> , as this is an Int or Integer Object
print(type(5))  

# Print <class 'float'> , as this is a Float Object
print(type(5.0))

# You can perform the following mathematical operation on Integer Objects

print(5 + 5)  # 10
print(5 - 1)  # 4
print(5 * 5)  # 25

# With the exception of the / operator. This will actually return a float
print(5 / 5)  # 1.0

# In order to return an Integer, you must use the // operator, but in actually this is actually rounding the number down, or flooring
print(5 // 5) # 1
print(5 // 2) # 2.5 => Rounded down to 2

# We can use the ** to get the 'power of'
print(5 ** 5) # 3125

# We can also use the % to get the remainder
print (10 % 3) # 1

# In Python there is also an order of operations
print (5 + 5 * 3) # 20
print ((5 + 5) * 3) # 30

# we can store numbers in a variable also
age = 5
print(age)

# we can perform mathematical operation on variables containins number also
print(age + 1)