import math


# сруктура ініціалізації
class Struct:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)


class MyStruct(Struct):
    pass


ms = MyStruct(foo=10, bar="abc", dot=3.5)
print(ms.dot)


# артибут з одним підкресленням не використовуються поза класом
class Circle:
    def __init__(self, radius):
        self.__radius = radius
        self._area = math.pi * radius ** 2


c1 = Circle(10)
print(c1._area)

c2 = Circle(10.0)
#print(c2.__radius)
print(c2._Circle__radius)
