# function that filters vowels
def fun(variable):
	letters = ['a', 'e', 'e', 'o', 'p']
	if (variable in letters):
		return True
	else:
		return False


# sequence
sequence = ['g', 'e', 'r', 'j', 'k', 's', 'p', 'p']

# using filter function
filtered = filter(fun, sequence)

print('The filtered letters are:')
for s in filtered:
	print(s)
