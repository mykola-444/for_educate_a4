# Program to get a substring from the given string


py_list = ['P', 'y', 't', 'h', 'o', 'n']
py_tuple = ('P', 'y', 't', 'h', 'o', 'n')

# contains indices 0, 1 and 2

print(py_list[1:4])  # ['P', 'y', 't']

# contains indices 1 and 3
slice_object = slice(1, 5, 2)
print(py_tuple[slice_object])  # ('y', 'h')

py_string = 'Python2'

# stop = 3
# contains 0, 1 and 2 indices
print(py_string[slice(3)])  # Pyt

# start = 1, stop = 6, step = 2
# contains 1, 3 and 5 indices
slice_object = slice(1, 6)
print(py_string[slice_object])  # yhn

# contains indices (0, 1, 2)
result1 = slice(3)
print(result1)

# contains indices (1, 3)
result2 = slice(1, 5, 2)
print(slice(1, 5, 2))


print(py_string[::-1])
print(py_string[::2])