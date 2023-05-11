f = open ('new.txt')
print (f.read (5))
 
 
f = open ('new.txt')
for line in f:
    print (line)

f = open ('new.txt', 'w')
f.write ('Hi, it\'s me!')
f.close()


