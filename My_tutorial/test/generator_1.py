def fun_1(x):
    print('calculation')
    return 10 * x


a = (1, 2, 3, 4)
print(a)
b = (fun_1(x) for x in a)  # це тільки заготовка вона нічого не вичисляє

for y in b:
    print(y)

print(fun_1(a))


def double_performer(f, x):
    print("yyyyyy", f, x)
    return f(f(x))


def f1(x):
    print('f1')
    return x * 10


def f2(x):
    print("f2")
    return x * x


def f3(x):
    print('f3')
    return -x


fz = f1
print(fz(3))
print('START')
for f in f1, f2, f3:
    print(double_performer(f, 7))
