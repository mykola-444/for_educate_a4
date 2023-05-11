i = 1000
while i > 100:
    print (i)
    i /= 2

for j in 'Hellow world':
    if j == 'w':
        continue 
    print(j * 3, end = '')

for j in 'Hellow world':
    if j == 'w':
        break
    print(j * 3, end = '')
