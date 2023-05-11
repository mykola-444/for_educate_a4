from collections import defaultdict

defdict = {'a', 'r', 'o', 's', 'e', 'i'}
print(defdict)

a = defaultdict(lambda: defdict)
print(a['A'])

defdict1 = defaultdict(list)
defdict2 = defaultdict(list)
print(defdict1)

for i in range(6, 10):
    defdict1[i].append(i)
print(defdict1)

for i in defdict:
    defdict2[i].append(i)
print(defdict2)
