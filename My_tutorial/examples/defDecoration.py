def decorator(func):
    def wrapper():
        print("Cod befor func")
        func()
        print("Cod run after func")
    return wrapper

def test(func):
    def wrapper():
        print("Cod befor func2")
        func()
        print("Cod run after func2")
    return wrapper

def show (line):
    print(line)
show(" I common func-9")



def decorator(func):
    def wrapper():
        print("Cod befor func")
        func()
        print("Cod run after func")
    return wrapper
def show ():
    print(" I common func -show")
    
show()
dec = decorator(show)
dec()


def decorator(func):
    def wrapper():
        print("Cod befor func")
        func()
        print("Cod run after func")
    return wrapper

@decorator
@test
def show ():
    print(" I common func -show")

#swow = decorator(show)
show()
