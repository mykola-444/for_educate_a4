from collections import Counter
from collections import OrderedDict
from pprint import pprint

test_line = "To use Terraform you will need to install it. HashiCorp distributes Terraform as a binary package. You can also install Terraform using popular package managers."

leter_count = {letter: test_line.count(letter) for letter in test_line}
leter_count1 = {letter: test_line.count(letter) for letter in set(test_line)}
# print(leter_count)
# print()
# print(leter_count1)

# for sort_ABC in sorted(leter_count1.keys()):
#     print(sort_ABC)


d1 = Counter(test_line)

print(Counter(test_line))
print()
print(Counter(test_line).most_common(6))
print()
print(sum(Counter(test_line).values()))
print()
print(Counter(test_line.split()))
print()  # sort words by ABS
print(OrderedDict(sorted(Counter(test_line.split()).items(), key=lambda w: w[0])))

print(OrderedDict(sorted(Counter(test_line.split()).items(), key=lambda t: t[1])))

print(OrderedDict(sorted(Counter(test_line.split()).items(), key=lambda t: len(t[0]))))

pprint(Counter(test_line))

