lst = [4, 5]
print(lst)


def foo(lst):
    lst.append("str")
    print(lst)


def foo1(lst):
    lst = [1, 4, 6]
    print(lst)


foo(lst)

foo1(lst)


class MyClass:
    attr = 1234

    def too(self):
        return "Hellow world"


print(MyClass.attr)

print(MyClass.too(1))
