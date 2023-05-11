class A:
    pass


class B(object):
    pass


a = A()
b = B()


print(b.__class__.__name__)  # <class '__main__.B'>
print(type(b))  # <class '__main__.B'>

print(a.__class__)  # <class '__main__.B'>
print(type(a))  # <class '__main__.B'>
print(dir(b))  # <class '__main__.B'>


class Bird:
    def fly(self):
        print("fly with wings")
class Airplane:
    def fly(self):
        print("fly with fuel")
class Fish:
    def swim(self):
        print("fish swim in sea")


# Attributes having same name are
# considered as duck typing
for obj in Bird(), Airplane(), Fish():
    obj.swim()