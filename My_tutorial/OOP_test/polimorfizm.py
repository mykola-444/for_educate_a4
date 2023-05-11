class list2(list):
    def __add__(self, other):
        return list2([i[0] + i[1] for i in zip(self, other)])

    def __sub__(self, other):
        return list2([i[0] - i[1] for i in zip(self, other)])


a = list2([1, 2, 3])
b = list([7, 4, 1])
c = a + b
c1 = a - b
print(c)
print(c1)


class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def __eq__(self, other):
        return self.r == other.r


o1 = Circle(0, 0, 2)
o2 = Circle(1, 0, 2)
print(o1 == o2)

