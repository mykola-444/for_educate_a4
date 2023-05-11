myDictionary = {"two": "2", "one": "1", "five": "5", "four": "9"}

newDictionary = {}
newDictionary1 = {}
sortedList = sorted(myDictionary.values())

for sortedKey in sortedList:
    for key, value in myDictionary.items():
        if value == sortedKey:
            newDictionary[key] = value

print(newDictionary)

sortedLis1 = sorted(myDictionary.keys())
print(sortedLis1)
for sortedKey in sortedLis1:
    for key, value in myDictionary.items():
        if key == sortedKey:
            newDictionary1[key] = value

print(newDictionary1)
