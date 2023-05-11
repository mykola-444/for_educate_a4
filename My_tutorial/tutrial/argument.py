def myFun(arg1, *argv):
    print("First argument :", arg1)
    for arg in argv:
        print("Next argument through *argv :", arg)


myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')


def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))


myFun(first='Geeks', mid='for', last='Geeks')


def myFun(*args, **kwargs):
    print("args: ", args)
    print("kwargs: ", kwargs)


myFun('geeks', 'for', 'geeks', first="Geeks", mid="for", last="Geeks")


def myFun(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)


args = ("Geeks", "for", "Geeks")
myFun(*args)

kwargs = {"arg1": "Geeks", "arg2": "for", "arg3": "Geeks"}
myFun(**kwargs)
