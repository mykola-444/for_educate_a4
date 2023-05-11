def func (x, a):
    res = x + a   
    return res
print (func('78',' number'))


def func (x):
    def add (a):
        return x + a   
    return add
test = func(100)
print (test(33))


def func ():
    pass
print (func())

def func (r, w, y=2):
    res = r+w
    res *=y
    return res
print (func(5, 10))


def func (*args):
    return args
print (func(5, 10, 45))

def func (**args):
    return args
print (func(a=5, b=10, c=45))


add = lambda x, y: x*y
print (add (5,4))
print (add ('q',4))

print ((lambda x, y: x*y)('rt',4))


fun = lambda *args: args
print ( fun(2,56,78.56))

