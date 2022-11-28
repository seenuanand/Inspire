import sys

# Different types of tuples
# Empty tuple
my_tuple = ()
print(my_tuple)

# Tuple having integers
my_tuple = (1, 2, 3)
print(my_tuple)

# tuple with mixed datatypes
my_tuple = (1, "Hello", 3.4)
print(my_tuple)

# nested tuple
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(my_tuple)

# packaging
my_tuple = 3, 4.6, "dog"
print(my_tuple)

# tuple unpacking is also possible
a, b, c = my_tuple

print(a)      # 3
print(b)      # 4.6
print(c)      # dog

my_tuple = ("hello")
print(type(my_tuple))  # <class 'str'>

# Creating a tuple having one element
my_tuple = ("hello",)
print(type(my_tuple))  # <class 'tuple'>

# Parentheses is optional
my_tuple = "hello",
print(type(my_tuple))  # <class 'tuple'>

# Accessing tuple elements using indexing
my_tuple = ('p','e','r','m','i','t')

print(my_tuple[0])   # 'p'
print(my_tuple[5])   # 't'

# IndexError: list index out of range
# print(my_tuple[6])

# Index must be an integer
# TypeError: list indices must be integers, not float
# my_tuple[2.0]

# nested tuple
n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))

# nested index
print(n_tuple[0][3])       # 's'
print(n_tuple[1][1])       # 4

# Negative indexing for accessing tuple elements
my_tuple = ('p', 'e', 'r', 'm', 'i', 't')

# Output: 't'
print(my_tuple[-1])

# Output: 'p'
print(my_tuple[-6])

# Accessing tuple elements using slicing
my_tuple = ('p','r','o','g','r','a','m','i','z')

# elements 2nd to 4th
# Output: ('r', 'o', 'g')
print(my_tuple[1:4])

# elements beginning to 2nd
# Output: ('p', 'r')
print(my_tuple[:-7])

# elements 8th to end
# Output: ('i', 'z')
print(my_tuple[7:])

# elements beginning to end
# Output: ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
print(my_tuple[:])

# Changing tuple values
my_tuple = (4, 2, 3, [6, 5])


# TypeError: 'tuple' object does not support item assignment
# my_tuple[1] = 9

# However, item of mutable element can be changed
my_tuple[3][0] = 9    # Output: (4, 2, 3, [9, 5])
print(my_tuple)

# Tuples can be reassigned
my_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')

# Output: ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
print(my_tuple)

# Concatenation
# Output: (1, 2, 3, 4, 5, 6)
print((1, 2, 3) + (4, 5, 6))

# Repeat
# Output: ('Repeat', 'Repeat', 'Repeat')
print(("Repeat",) * 3)

# Deleting tuples
my_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')

# can't delete items
# TypeError: 'tuple' object doesn't support item deletion
# del my_tuple[3]

# Can delete an entire tuple
del my_tuple

# NameError: name 'my_tuple' is not defined
# print(my_tuple)

my_tuple = ('a', 'p', 'p', 'l', 'e',)

print(my_tuple.count('p'))  # Output: 2
print(my_tuple.index('l'))  # Output: 3

# Membership test in tuple
my_tuple = ('a', 'p', 'p', 'l', 'e',)

# In operation
print('a' in my_tuple)
print('b' in my_tuple)

# Not in operation
print('g' not in my_tuple)

# Using a for loop to iterate through a tuple
for name in ('John', 'Kate'):
    print("Hello", name)

# Zipping

first_names = ('Simon', 'Sarah', 'Mehdi', 'Fatime')
last_names = ('Sinek', 'Smith', 'Lotfinejad', 'Lopes')
ages = (49, 55, 39, 33)
zipped = zip(first_names, last_names,ages)
print(zipped)


a_list = ['abc', 'xyz', 123, 231, 13.31, 0.1312]
a_tuple = ('abc', 'xyz', 123, 231, 13.31, 0.1312)
print('The list size:', sys.getsizeof(a_list), 'bytes')
print('The tuple size:', sys.getsizeof(a_tuple), 'bytes')

# Swapping
x = 19
y = 91
print('Before swapping:')
print(f'x = {x}, y = {y}')
(x, y) = (y, x)
print('After swapping:')
print(f'x = {x}, y = {y}')

def sum_and_avg(x, y, z):
    s = x + y + z
    a = s/3
    return(s, a)
(S, A) = sum_and_avg(3, 8, 5)
print('Sum =', S)
print('Avg =', A)



# Since tuples are quite similar to lists, both of them are used in similar situations.
# However, there are certain advantages of implementing a tuple over a list.
# Below listed are some of the main advantages:
#
# We generally use tuples for heterogeneous (different) data types and
# lists for homogeneous (similar) data types.
# Since tuples are immutable, iterating through a tuple is faster than with list.
# So there is a slight performance boost.
# Tuples that contain immutable elements can be used as a key for a dictionary.
# With lists, this is not possible.
# If you have data that doesn't change, implementing it as tuple will guarantee that it remains
# write-protected.
#
